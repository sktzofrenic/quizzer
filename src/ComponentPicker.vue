<template>
    <div class="bg-slate-900  px-2 py-2  shadow-lg">
        <select name="" id="" v-model="currentComponent">
            <option value=""></option>
            <option value="EventManager">EventManager</option>
            <option value="Editor">Editor</option>
            <option value="TextAlert">TextAlert</option>
            <option value="Client">Client</option>
            <option value="GameMaster">GameMaster</option>
            <option value="Camp">Camp</option>
            <option value="CampManager">CampManager</option>
            <option value="SeeTheGift">SeeTheGift</option>
            <option value="MemoryVerseGM">MemoryVerseGM</option>
            <option value="MemoryVerseClient">MemoryVerseClient</option>
            <option value="Login">Login</option>
            <option value="QuickBooks">QuickBooks</option>
            <option value="">Login</option>
        </select>
    </div>
    <div class="container mx-auto px-4">
        <component :is="componentMapper[currentComponent]"></component>
    </div>
</template>


<script setup>
import Editor from './components/utility/Editor.vue'
import TextAlert from './components/TextAlert.vue'
import Client from './components/game/Client.vue'
import MemoryVerseGM from './components/game/MemoryVerseGM.vue'
import MemoryVerseClient from './components/game/MemoryVerseClient.vue'
import GameMaster from './components/game/GameMaster.vue'
import Camp from './components/camp/Camp.vue'
import CampManager from './components/camp/CampManager.vue'
import SeeTheGift from './components/events/SeeTheGift.vue'
import EventManager from './components/events/EventManager.vue'
import Login from './components/Login.vue'
import QuickBooks from './components/church/QuickBooks.vue'
import { ref } from 'vue'

var componentMapper = {
    'Editor': Editor,
    'TextAlert': TextAlert,
    'Client': Client,
    'GameMaster': GameMaster,
    'Camp': Camp,
    'CampManager': CampManager,
    'SeeTheGift': SeeTheGift,
    'EventManager': EventManager,
    'MemoryVerseGM': MemoryVerseGM,
    'MemoryVerseClient': MemoryVerseClient,
    'Login': Login,
    'QuickBooks': QuickBooks
}

const currentComponent = ref('')
currentComponent.value = 'QuickBooks'

</script>
