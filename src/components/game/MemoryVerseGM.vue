<template>
    <div class="flex flex-row">
        <div class="basis-1/6 bg-slate-600/30 px-2 text-2xl">
            <Button textColor="white" backgroundColor="sky" @click="toggleRevealNames" class="my-2" style="font-size: 20px">Toggle Names</Button>
            <Button textColor="white" backgroundColor="red" @click="clearVerses" class="my-2" style="font-size: 20px">Clear Verses</Button>
            <Button textColor="white" backgroundColor="gray" @click="lockAnswers" class="my-2" style="font-size: 20px">
                <span v-if="locked">Unlock Answers</span>
                <span v-else class="text-zinc-200">Lock Answers</span>
            </Button>
            <audio controls>
                <source src="https://drx-myground.us-east-1.linodeobjects.com/drx-myground/music_64e40fe8.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
            </audio>
            <Button textColor="white" backgroundColor="indigo" @click="goBack" class="my-2" style="font-size: 20px">Go Back</Button>
            <div v-if="verses.length">
                <h2 class="text-xl font-bold">Available Verses</h2>
                <ul class="mt-4">
                    <li class="bg-slate-200 rounded-md px-2 py-2 my-1 cursor-pointer" 
                        @click="chooseActiveVerse(verse.id)"
                        v-for="verse in verses" :key="verse.id">
                        <button >{{verse.reference}}</button>
                    </li>
                </ul>
            </div>
        </div>
        <div class="basis-5/6 px-2">
            <div v-if="memoryVerse">
                <h2 class="text-center text-5xl text-slate-300 my-5 text-bold">{{memoryVerse.reference}}</h2>
            </div>
            <div class="flex justify-center flex-wrap" v-if="answers.length > 2">
                <div class="m-10 bg-slate-900/10 rounded-xl shadow-2xl border-2 border-slate-600/10 px-10 relative" 
                     v-for="answer in answers" :key="answer.name">
                    <div class="text-yellow-300 -mb-8 text-center" :style="pointStyle">
                        {{ formatNumber(answer.score) }}
                    </div>
                    <transition name="slide-fade">
                        <i class="fa-solid fa-lock text-4xl absolute text-red-400 -top-4 -left-4 shadow-xl" v-if="locked"></i>
                    </transition>
                    <div class="text-white text-center" :style="nameStyle">
                        <span v-if="revealNames">
                            {{ truncate(answer.name) }}
                        </span>
                        <span v-else>
                            Player
                        </span>
                    </div>
                    <span class="text-white text-xl absolute left-0 text-center">
                        Exact {{answer.exact_correct_words}},
                        Close {{answer.close_correct_words}},
                        Wrong {{answer.incorrect_words}},
                        Missed {{answer.missed_words}}
                    </span>
                </div>
            </div>
            <div v-else-if="answers.length > 0">
                <h2 class="text-center text-5xl text-slate-300 my-5 text-bold">{{answers.length}} player<span v-if="answers.length != 1">s</span></h2>
            </div>
        </div>
    </div>
</template>

<script>
import {socket} from '../../socket.js'
import { useBaseUrlStore } from '@/stores/baseUrl'
import Button from '@/components/utility/Button.vue'
import axios from 'axios'

export default {
    name: 'MemoryVerseGM',
    data() {
        return {
            memoryVerse: null,
            verses: [],
            answers: [],
            locked: false,
            revealNames: false,
            baseUrl: useBaseUrlStore().baseUrl,
        }
    },
    computed: {
        nameStyle() {
            var fontSize = 50
            return {
                'font-size': fontSize + 'px !important'
            }
        },
        pointStyle() {
            var fontSize = 80
            return {
                'font-size': fontSize + 'px !important'
            }
        }
    },
    components: {
        Button
    },
    methods: {
        lockAnswers () {
            var vm = this
            vm.locked = !vm.locked
        },
        truncate (name) {
            if (name.length > 8) {
                return name.substring(0, 12) + '...'
            } else {
                return name
            }
        },
        formatNumber (number) {
            number = parseInt(number)
            return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        },
        goBack() {
            this.$emit('goBack')
        },
        clearVerses () {
            var vm = this
            axios.get(`${vm.baseUrl}/api/v1/game-verses?clearVerses=true`)
                .then(function(response) {
                    vm.memoryVerse = null
                    vm.answers = []
                    vm.revealNames = false
                })
                .catch(function(error) {
                    console.log('error', error)
                })
        },
        chooseActiveVerse (id) {
            var vm = this
            axios.get(`${vm.baseUrl}/api/v1/game-verses?sendVerse=${id}`)
                .then(function(response) {
                    vm.memoryVerse = response.data.verse
                    vm.revealNames = false
                    vm.locked = false
                })
                .catch(function(error) {
                    console.log('error', error)
                })
        },
        getAvailableVerses() {
            var vm = this
            axios.get(`${vm.baseUrl}/api/v1/game-verses?getAllAvailableVerses=true`)
                .then(function(response) {
                    vm.verses = response.data.verses
                })
                .catch(function(error) {
                    console.log('error', error)
                })
        },
        toggleRevealNames() {
            this.revealNames = !this.revealNames
        },
    },
    mounted () {
        var vm = this
        vm.getAvailableVerses()
        socket.bind('memoryVerseAnswer', function(data) {
            if (vm.locked) {
                return
            }
            var existing = vm.answers.find(function(answer) {
                return answer.name === data.answer.name
            })
            if (existing) {
                if (existing.score > data.answer.score) {
                    var audio = new Audio('https://drx-myground.us-east-1.linodeobjects.com/drx-myground/Glitch_01_bfd07100.mp3')
                    audio.play()

                } else {
                    var audio = new Audio('https://drx-myground.us-east-1.linodeobjects.com/drx-myground/Coin_Bling_1b5dbcb3.mp3')
                    audio.play()
                }
                vm.answers.splice(vm.answers.indexOf(existing), 1, data.answer)
            } else {
                vm.answers.push(data.answer)
            }
        })
    }
}
</script>
<style>
/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.15s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.4s ease-in;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}</style>
