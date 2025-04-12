<template>
    <div class="bg-slate-900  px-2 py-2  shadow-lg">
        <select name="" id="" v-model="currentComponent">
            <option value=""></option>
            <option value="Client">Client</option>
            <option value="GameMaster">GameMaster</option>
        </select>
    </div>
    <div class="container mx-auto px-4">
        <component :is="componentMapper[currentComponent]"></component>
    </div>
</template>


<script setup>
import Client from './components/game/Client.vue'
import MemoryVerseGM from './components/game/MemoryVerseGM.vue'
import MemoryVerseClient from './components/game/MemoryVerseClient.vue'
import GameMaster from './components/game/GameMaster.vue'
import { ref } from 'vue'

var componentMapper = {
    'Client': Client,
    'GameMaster': GameMaster,
    'MemoryVerseGM': MemoryVerseGM,
    'MemoryVerseClient': MemoryVerseClient,
}


</script>
