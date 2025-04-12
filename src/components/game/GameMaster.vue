<template lang="html">
    <div class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 h-screen overflow-hidden">
        <div class="flex justify-center text-slate-100 text-8xl py-8 bg-slate-900/20 shadow-2xl border-b-2 border-slate-600/50 " v-show="mode == 'gm'">
            <h1 v-if="name">Hotseat: <span class="text-yellow-300">{{ name }}</span> <span v-if="points !== 'undefined'">{{points}}</span></h1>
            <h1 v-else>waiting...</h1>
        </div>
        <div class="h-full my-8 py-8"  v-show="mode == 'gm'">
            <!-- <button class="ui red button" @click="incorrectAnswer()">Wrong!</button>
            <button class="ui green button" @click="correctAnswer()">Right!</button>
            <button class="ui purple button" @click="playGame()">Play!</button>
            <button class="ui grey button" type="button" name="button" @click="clearAnswer()">Clear</button> -->
            <div class="flex justify-center flex-wrap">
                <div @click="selectTeam(index)" class="m-10 bg-slate-900/10 rounded-xl shadow-2xl border-2 border-slate-600/10 px-10" v-for="(player, index) in players">
                    <div class="text-yellow-300 -mb-10 text-center" :style="pointStyle">
                        {{ formatNumber(player.points) }}
                    </div>
                    <div class="text-white" :style="nameStyle">
                        {{ truncate(player.name) }}
                    </div>
                </div>
            </div>
        </div>
        <div class="" v-show="mode == 'MemoryVerse'">
            <MemoryVerseGM @goBack="mode = 'gm'"/>
        </div>
        <div class="" v-show="mode == 'Zonk'">
            <Zonk :teamName="name" :team="team" @playDone="stopPlay"/>
        </div>
    </div>
</template>

<script>
import {socket} from './../../socket.js'
import { useBaseUrlStore } from '@/stores/baseUrl'
import {find, orderBy} from 'lodash-es'
import Zonk from './Zonk.vue'
import MemoryVerseGM from './MemoryVerseGM.vue'
import Mousetrap from 'mousetrap'

export default {
    data () {
        return {
            name: '',
            points: 0,
            team: null,
            socket: undefined,
            baseUrl: useBaseUrlStore().baseUrl,
            players: [],
            mode: 'gm',
            possiblePlayers: []
        }
    },
    components: {
        Zonk,
        MemoryVerseGM
    },
    computed: {
        nameStyle() {
            var fontSize = this.players.length > 6 ? 50 : 50
            return {
                'font-size': fontSize + 'px !important'
            }
        },
        pointStyle() {
            var fontSize = this.players.length > 6 ? 100 : 100
            return {
                'font-size': fontSize + 'px !important'
            }
        }
    },
    methods: {
        formatNumber (number) {
            return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
        playGame () {
            this.mode = 'Zonk'
        },
        selectTeam (index) {
            this.name = this.players[index].name
        },
        stopPlay (points, doublers, unzonks) {
            this.mode = 'gm'
            this.correctAnswer(points, doublers, unzonks)
        },
        truncate (name) {
            if (name.length > 8) {
                return name.substring(0, 12) + '...'
            } else {
                return name
            }
        },
        clearAnswer: function () {
            var vm = this
            if (vm.name === '') {
                return
            }
            if (find(vm.players, {name: vm.name.toLowerCase()})) {
                vm.players.map(function (each) {
                    // do nothing if the player exists
                })
            } else {
                // add the player if not exists
                vm.players.push({
                    name: vm.name.toLowerCase(),
                    points: 0,
                    doublers: 0,
                    unzonks: 0
                })
            }
            this.name = ''
        },
        correctAnswer: function (points, doublers, unzonks) {
            var vm = this
            if (find(vm.players, {name: vm.name})) {
                vm.players.map(function (each) {
                    if (each.name === vm.name) {
                        each.points += points
                        each.doublers += doublers
                        each.unzonks += unzonks
                    }
                })
            } else {
                vm.players.push({
                    name: vm.name,
                    points: points,
                    doublers: doublers,
                    unzonks: unzonks
                })
            }
            vm.name = ''
        },
        incorrectAnswer: function () {
            var vm = this
            if (find(vm.players, {name: vm.name})) {
                vm.players.map(function (each) {
                    if (each.name === vm.name) {
                        if (each.points > 0) {
                            each.points = parseInt(each.points / 2)
                        } else {
                            each.points -= 1000
                        }
                    }
                })
            } else {
                vm.players.push({
                    name: vm.name,
                    points: -1000
                })
            }
            vm.name = ''
        }
    },
    mounted: function () {
        var vm = this
        Mousetrap.bind('d d', function () {
            vm.players.splice(vm.players.indexOf(vm.name), 1)
            vm.name = ''
        })
        Mousetrap.bind('m m', function () {
            vm.mode = 'MemoryVerse'
        })
        Mousetrap.bind('p', function () {
            vm.playGame()
        })
        Mousetrap.bind('c', function () {
            vm.clearAnswer()
        })
        Mousetrap.bind('n', function () {
            vm.incorrectAnswer()
        })
        Mousetrap.bind('up', function () {
            if (vm.name) {
                vm.players.map(function (each) {
                    if (each.name === vm.name) {
                        each.points += 100
                    }
                })
            }  
        })
        Mousetrap.bind('down', function () {
            if (vm.name) {
                vm.players.map(function (each) {
                    if (each.name === vm.name) {
                        each.points -= 100
                    }
                })
            } 
        })
        socket.bind('answer', function (data) {
            if (!vm.name) {
                vm.possiblePlayers.push(data)
                var timeout = setTimeout(function () {
                    // pick a winner from the group
                    // and put him in the hot seat
                    vm.possiblePlayers = orderBy(vm.possiblePlayers, [function(o) { return o.timestamp; }])
                    if (!vm.name) {
                        var alert = new Audio(`${vm.baseUrl}/static/alert.wav`)
                        alert.play()
                        vm.name = vm.possiblePlayers[0].name
                        vm.team = vm.possiblePlayers[0]
                        vm.points = vm.possiblePlayers[0].points
                        vm.possiblePlayers = []
                    }
                }, 500)
            }
        })
    }
}
</script>


