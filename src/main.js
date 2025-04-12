import '../myground/static/css/output.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import MultipleChoiceClient from './components/MultipleChoiceClient.vue'
import ComponentPicker from './ComponentPicker.vue'
import Editor from './components/utility/Editor.vue'
import TextAlert from './components/TextAlert.vue'
import GameMaster from './components/game/GameMaster.vue'
import Client from './components/game/Client.vue'
import Camp from './components/camp/Camp.vue'
import SeeTheGift from './components/events/SeeTheGift.vue'
import Camelot from './components/events/Camelot.vue'
import EventManager from './components/events/EventManager.vue'
import QuickBooks from './components/church/QuickBooks.vue'

const app = createApp(App)
const mutlipleChoiceClient = createApp(MultipleChoiceClient)
const editor = createApp(Editor)
const componentPicker = createApp(ComponentPicker)
const textAlert = createApp(TextAlert)
const gameMaster = createApp(GameMaster)
const client = createApp(Client)
const camp = createApp(Camp)
const seeTheGift = createApp(SeeTheGift)
const camelot = createApp(Camelot)
const eventManager = createApp(EventManager)
const quickBooks = createApp(QuickBooks)

app.use(createPinia())

app.mount('#app')
mutlipleChoiceClient.mount('#trivia')
editor.mount('#editor')
componentPicker.mount('#component-picker')
textAlert.mount('#text-alert')
gameMaster.mount('#game-master')
client.mount('#client')
camp.mount('#camp')
seeTheGift.mount('#stg')
camelot.mount('#camelot')
eventManager.mount('#event-manager')
quickBooks.mount('#quick-books')
