import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useBaseUrlStore = defineStore('baseUrl', () => {
    var baseUrl = ref('')
    if (location.hostname === "localhost" || location.hostname === "127.0.0.1") {
        baseUrl = ref(`http://127.0.0.1:5000`)
    } else {
        baseUrl = ref(`${location.protocol}//${location.hostname}`)
    }

  return { baseUrl }
})
