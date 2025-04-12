<template>
    <div>
        <h2 class="text-center text-2xl my-2">{{verse.reference}}</h2>
        <div class="bg-slate-100 rounded-lg p-2 mb-2">
            <h5 class="text-slate-900 block text-xl text-center">Answer</h5>
            <div class="flex flex-wrap gap-1 justify-center mb-10">
                <TransitionGroup name="list">
                    <span @click="moveToBank(index)" 
                        class="bg-green-300 text-green-900 rounded-md px-4 py-1" 
                        v-for="(word, index) in answerWords" :key="word">
                        {{word}}
                    </span>
                </TransitionGroup>
            </div>
        </div>
        <div class="bg-slate-100 rounded-lg p-2">
            <h5 class="text-slate-900 block text-xl text-center">Word Bank</h5>
            <div class="flex flex-wrap gap-3 justify-center">
                <TransitionGroup name="list">
                    <span @click="moveFromBank(index)" 
                    class="bg-slate-300 text-slate-900 rounded-md px-4 py-1 mr-1" 
                    v-for="(word, index) in bankWords" :key="word">
                    {{word}}
                    </span>
                </TransitionGroup>
            </div>
        </div>
    </div>
</template>

<script>
import {socket} from '../../socket.js'
import { useBaseUrlStore } from '@/stores/baseUrl'
import axios from 'axios'
import {debounce, sortBy} from 'lodash-es'

export default {
    name: 'MemoryVerseClient',
    data() {
        return {
            answerWords: [],
            bankWords: [],
            baseUrl: useBaseUrlStore().baseUrl,
        }
    },
    props: {
        verse: {
            type: Object,
            default: {}
        },
        name: {
            type: String,
            default: ''
        }
    },
    computed: {
        userInput() {
            return this.answerWords.join(' ') + ' ' + this.bankWords.join(' ')
        }
    },
    watch: {
        userInput: function () {
            var vm = this
            // remove blanks
            vm.answerWords = vm.answerWords.filter(word => word != undefined)
            vm.bankWords = vm.bankWords.filter(word => word != undefined)
        }
    },
    methods: {
        moveToBank (index) {
            var vm = this
            vm.bankWords = vm.bankWords.concat(vm.answerWords.slice(index - vm.answerWords.length))
            vm.answerWords = vm.answerWords.slice(0, index)
            vm.sendAnswer()
        },
        moveFromBank (index) {
            var vm = this
            vm.answerWords.push(vm.bankWords[index])
            vm.bankWords.splice(index, 1)
            vm.sendAnswer()
        },
        sendAnswer: debounce (function () {
            var vm = this
            if (vm.name == '') {
                vm.$emit('message', 'Please enter your name')
            }
            axios.post(`${vm.baseUrl}/api/v1/game-verses?answer=true`, {
                verseId: vm.verse.id,
                name: vm.name,
                words: vm.answerWords
            }).then(function (data) {
            })
        }, 400)
    },
    mounted () {
        var vm = this
        vm.bankWords = sortBy(vm.verse.bank_words.map(word => word.word), (word) => word)
        socket.bind('versesCleared', function(data) {
            vm.$emit('versesCleared')
        })
    }
}
</script>
<style scoped>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.2s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
</style>
