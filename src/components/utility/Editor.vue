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
                <Button backgroundColor="sky" textColor="white" class="mt-2" @click="clearMessage">Ok!</Button>
            </div>
        </div>
    </div>    
    <div class="my-2 ">
        <div v-if="editor" class="my-4">
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200  rounded-l-lg" @click="editor.chain().focus().toggleBold().run()" :disabled="!editor.can().chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
                <i class="fa-sharp fa-solid fa-bold"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleItalic().run()" :disabled="!editor.can().chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }">
                <i class="fa-solid fa-italic"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleStrike().run()" :disabled="!editor.can().chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }">
                <i class="fa-solid fa-strikethrough"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().setParagraph().run()" :class="{ 'is-active': editor.isActive('paragraph') }">
                <i class="fa-duotone fa-paragraph"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleHeading({ level: 1 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
                <i class="fa-solid fa-h1"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleHeading({ level: 2 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
                <i class="fa-solid fa-h2"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleHeading({ level: 3 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
                <i class="fa-solid fa-h3"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
                <i class="fa-solid fa-list"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleOrderedList().run()" :class="{ 'is-active': editor.isActive('orderedList') }">
                <i class="fa-solid fa-list-ol"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 " @click="editor.chain().focus().toggleBlockquote().run()" :class="{ 'is-active': editor.isActive('blockquote') }">
                <i class="fa-solid fa-square-quote"></i>
            </button>
            <button class="disabled:bg-gray-400 disabled:text-gray-200 bg-slate-900 px-2 py-1 text-sky-200 rounded-r-lg mr-2" @click="editor.chain().focus().setHorizontalRule().run()">
                <i class="fa-regular fa-horizontal-rule"></i>
            </button>
        </div>
        <div class="editor block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6"></div>
        <div class="my-4">
            <legend class="sr-only">Recipients</legend>
            <div class="space-y-2">
                <div class="relative flex items-start">
                    <div class="flex h-6 items-center">
                        <input id="comments" aria-describedby="comments-description" name="comments" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-sky-600 focus:ring-sky-600" v-model="recipients.staff">
                    </div>
                    <div class="ml-3 text-sm leading-6">
                        <label for="comments" class="font-medium text-gray-900">SECA Staff</label>
                    </div>
                </div>
                <div class="relative flex items-start">
                    <div class="flex h-6 items-center">
                        <input id="candidates" aria-describedby="candidates-description" name="candidates" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-sky-600 focus:ring-sky-600" v-model="recipients.parents">
                    </div>
                    <div class="ml-3 text-sm leading-6">
                        <label for="candidates" class="font-medium text-gray-900">SECA Parents</label>
                    </div>
                </div>
                <div class="relative flex items-start">
                    <div class="flex h-6 items-center">
                        <input id="offers" aria-describedby="offers-description" name="offers" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-sky-600 focus:ring-sky-600" v-model="recipients.homeschool">
                    </div>
                    <div class="ml-3 text-sm leading-6">
                        <label for="offers" class="font-medium text-gray-900">Homeschool Parents</label>
                    </div>
                </div>
            </div>
        </div>
        <Button backgroundColor="sky" textColor="white" class="my-2 w-full" :disabled="loading" @click="sendMemo">
            <i class="fa-duotone fa-spinner-third fa-spin text-xl" v-if="loading"></i>
            <span v-else>Send Memo</span>
        </Button>
    </div>
</template>

<script setup>
import { Editor } from '@tiptap/core'
import { useBaseUrlStore } from '@/stores/baseUrl'
import Button from './Button.vue'
import StarterKit from '@tiptap/starter-kit'
import { onMounted, ref, toRaw } from 'vue'



const location = window.location.pathname
var editor = ref(null)
var loading = ref(false)
var recipients = ref({
    staff: false,
    parents: false,
    homeschool: false
})
var message = ref('')
var baseUrl = useBaseUrlStore()

// clear msg
function clearMessage() {
    message.value = ''
}

const sendMemo = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/${location}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            memo: editor.getHTML(),
            staff: recipients.value.staff,
            parents: recipients.value.parents,
            homeschool: recipients.value.homeschool
        })
    })
        .then(data => {
            console.log(data)
            loading.value = false
            message.value = 'Memo sent successfully.'
            editor.commands.clearContent(true)
            window.scrollTo({ top: 0, behavior: 'smooth' });
        })
        .catch(error => {
            console.log(error)
            loading.value = false
        })
}

onMounted(() => {
    editor.value = new Editor({
        editorProps: {
            attributes: {
                class: 'prose prose-lg mx-auto my-10 focus:outline-none min-h-fit',
            },
        },
        element: document.querySelector('.editor'),
        extensions: [
            StarterKit,
        ],
        content: '<h1>Title</h1><p>It has come to my attention that...</p>',
    })
    editor = toRaw(editor.value)
})


</script>

