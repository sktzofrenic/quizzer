<template>
    <div class="border-l-4 border-blue-400 bg-blue-50 p-4 mb-6" v-if="message">
        <div class="flex">
            <div class="flex-shrink-0">
                <svg class="h-5 w-5 text-blue-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                    <path fill-rule="evenodd" d="M8.485 2.495c.673-1.167 2.357-1.167 3.03 0l6.28 10.875c.673 1.167-.17 2.625-1.516 2.625H3.72c-1.347 0-2.189-1.458-1.515-2.625L8.485 2.495zM10 5a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0v-3.5A.75.75 0 0110 5zm0 9a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                </svg>
            </div>
            <div class="ml-3">
                <p class="text-sm text-blue-700">
                    {{ message }}
                </p>
                <Button backgroundColor="sky" textColor="white" class="mt-2" @click="message = ''">Ok!</Button>
            </div>
        </div>
    </div>    
    <div class="my-2">
        <h2 class="text-2xl font-bold">Send an Alert</h2>
        <div>
            <input type="text" class="block  rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" v-model="textAlert">
        </div>
        <Button backgroundColor="sky" textColor="white" class="mt-6" @click="sendAlert">
            <i class="fa-duotone fa-spinner-third fa-spin text-xl" v-if="loading"></i>
            <span v-else>Send Alert</span>
        </Button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBaseUrlStore } from '@/stores/baseUrl'
import Button from '@/components/utility/Button.vue'

const location = window.location.pathname
var loading = ref(false)
var baseUrl = useBaseUrlStore()
var textAlert = ref('')
var message = ref('')

const sendAlert = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}${location}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            textAlert: textAlert.value
        })
    })
        .then(data => {
            loading.value = false
            message.value = 'Text Alert sent successfully.'
        })
        .catch(error => {
            loading.value = false
        })
}

</script>
