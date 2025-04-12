<template lang="html">
    <div class="grid place-content-center h-screen grid-cols-1 px-6">
        <div class="rounded-lg bg-slate-50 text-indigo-700 py-2 px-8 mb-8 ring-indigo-700 ring-1" v-if="message">
            {{message}}
        </div>
        <input type="text" class="w-full rounded-lg px-8 py-8 text-4xl" placeholder="Your name" v-model="name">
        <div class="grid grid-cols-2 gap-2" v-if="mode == 'wagerAnswer'">
            <button style="touch-action: manipulation;" class="rounded-lg bg-sky-600 text-slate-100 px-20 py-20 mt-10 font-bold text-2xl" 
                @click="sendAnswer(100)">
                100
            </button>
            <button style="touch-action: manipulation;" class="rounded-lg bg-sky-600 text-slate-100 px-20 py-20 mt-10 font-bold text-2xl" 
                @click="sendAnswer(200)">
                200
            </button>
            <button style="touch-action: manipulation;" class="rounded-lg bg-sky-600 text-slate-100 px-20 py-20 mt-10 font-bold text-2xl" 
                @click="sendAnswer(400)">
                400
            </button>
            <button style="touch-action: manipulation;" class="rounded-lg bg-sky-600 text-slate-100 px-20 py-20 mt-10 font-bold text-2xl" 
                @click="sendAnswer(600)">
                600
            </button>
        </div>
        <button style="touch-action: manipulation;" class="rounded-lg bg-sky-600 text-slate-100 px-20 py-20 mt-10 font-bold text-8xl"
            v-if="mode == 'answer'"
            @click="sendAnswer()">
            Buzz
        </button>
        <div v-if="mode == 'verse'">
            <MemoryVerseClient :name="name" :verse="verse" @message="displayMessage" @versesCleared="clearVerse"/>
        </div>
    </div>
</template>

<script>
import {socket} from '../../socket.js'
import { useBaseUrlStore } from '@/stores/baseUrl'
import axios from 'axios'
import dayjs from 'dayjs'
import MemoryVerseClient from './MemoryVerseClient.vue'

export default {
    data () {
        return {
            name: '',
            mode: 'answer',
            message: '',
            socket: undefined,
            baseUrl: useBaseUrlStore().baseUrl,
            delay: 0,
            verse: null
        }
    },
    components: {
        MemoryVerseClient
    },
    methods: {
        displayMessage (message) {
            var vm = this
            vm.message = message
            setTimeout(function () {
                vm.message = ''
            }, 3000)
        },
        clearVerse () {
            var vm = this
            vm.verse = null
            vm.mode = 'answer'
        },
        checkForVerse () {
            var vm = this
            axios.get(`${vm.baseUrl}/api/v1/game-verses?retrieveActiveVerse=true`).then(function (response) {
                if (response.data.verse) {
                    vm.verse = response.data.verse
                    vm.mode = 'verse'
                }
            })
        },
        sendAnswer (points) {
            var vm = this
            if (vm.name == '') {
                vm.message = 'Please enter your name'
                setTimeout(function () {
                    vm.message = ''
                }, 3000)
                return
            }
            var time = dayjs().valueOf()
            axios.get(`${vm.baseUrl}/client/api?answer=true&name=${vm.name}&timestamp=${time}&points=${points}`).then(function (data) {
            })
        }
    },
    mounted () {
        var vm = this

        vm.checkForVerse()

        socket.bind('memoryVerse', function(data) {
            vm.verse = data.verse
            vm.mode = 'verse'
        })
        socket.bind('connect', function() {
            console.log('client connected')
            socket.emit('my-event', {
                data: 'I\'m connected!'
            })
        })
    }
}
</script>



