import '../quizzer/static/css/output.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import ComponentPicker from './ComponentPicker.vue'
import GameMaster from './components/game/GameMaster.vue'
import Client from './components/game/Client.vue'

const app = createApp(App)
const componentPicker = createApp(ComponentPicker)
const gameMaster = createApp(GameMaster)
const client = createApp(Client)

app.use(createPinia())

app.mount('#app')
componentPicker.mount('#component-picker')
gameMaster.mount('#game-master')
client.mount('#client')
