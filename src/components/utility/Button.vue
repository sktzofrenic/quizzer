<template>
    <button class="
        flex
        justify-center
        rounded-md
        px-3
        py-1.5
        text-sm
        font-semibold
        leading-6
        shadow-sm
        focus-visible:outline
        focus-visible:outline-2
        focus-visible:outline-offset-2"
        :class="`text-${textColor} bg-${backgroundColor}-600 hover:bg-${backgroundColor}-500 focus-visible:outline-${backgroundColor}-600`" >
        <slot></slot>
    </button>
</template>

<script setup>
defineProps({
    textColor: {
        type: String,
        required: true
    },
    backgroundColor: {
        type: String,
        required: true
    }
})
</script>


