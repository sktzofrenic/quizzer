<template>
    <div class="min-h-full">
        <nav class="border-b border-gray-200 bg-white">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="flex h-16 justify-between">
                    <div class="flex">
                        <div class="hidden sm:-my-px sm:ml-6 sm:flex sm:space-x-8">
                            <a @click="currentView = 'Events'" :class="{'border-b-2': currentView == 'Events'}" 
                                 class="border-sky-500 text-gray-900 inline-flex items-center  px-1 pt-1 text-sm font-medium cursor-pointer">Events</a>
                            <a @click="currentView = 'campManager'" :class="{'border-b-2': currentView == 'campManager'}" 
                                 class="border-sky-500 text-gray-900 inline-flex items-center  px-1 pt-1 text-sm font-medium cursor-pointer">Camp Manager</a>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
        <div class="py-10">
            <main>
                <div class="mx-auto max-w-7xl sm:px-6 lg:px-8" v-if="currentView == 'Events'">
                    <div class="sm:flex sm:items-center">
                        <div class="sm:flex-auto">
                            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Filter</label>
                            <div class="mb-2 max-w-sm">
                                <input  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="Search..." v-model="searchTerm">
                            </div>
                        </div>
                        <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
                            <button type="button" class="block rounded-md bg-sky-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600" @click="addNew">Add New</button>
                        </div>
                    </div>
                    <Table>
                        <template v-slot:header>
                            <tr>
                                <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Name</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Desc.</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Image</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Start</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">End</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Signups</th>
                                <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                                    <span class="sr-only">Edit</span>
                                </th>
                            </tr>
                        </template>
                        <template v-slot:body>
                            <tr v-for="event in filteredEvents">
                                <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">{{truncate(event.title)}}</td>
                                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{truncate(event.body)}}</td>
                                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                    <a :href="event.image" class="text-sky-400 underline-offset-2 underline" target="_blank">
                                        {{truncate(event.image)}}
                                    </a>
                                </td>
                                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{dayjs(event.date_start).format('M/D/YYYY')}}</td>
                                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{dayjs(event.date_end).format('M/D/YYYY')}}</td>
                                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                                    <span @click="viewSignups(event)" class="text-sky-600 hover:text-sky-900 cursor-pointer">
                                        {{event.signups}}
                                    </span>
                                </td>
                                <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                                    <a @click="editEvent(event)" class="text-sky-600 hover:text-sky-900 cursor-pointer">Edit</a>
                                </td>
                            </tr>
                        </template>
                    </Table>
                </div>
                <div class="mx-auto max-w-7xl sm:px-6 lg:px-8" v-if="currentView == 'campManager'">
                    <CampManager />
                </div>
                <Transition name="fade">
                    <Modal v-if="signupsId != null">
                        <template v-slot:content>
                            <h5 class="font-bold text-xl mb-2">
                                {{getEventById(events, signupsId).title}} <i class="fa-solid fa-arrow-right"></i>  Net Total: {{countTotal(signups) - countCancelled(signups)}} Checked In: {{countConfirmed(signups)}} ({{parseInt(countConfirmed(signups) / (countTotal(signups) - countCancelled(signups)) * 100)}}%)
                            </h5>
                            <div class="mb-2 max-w-sm">
                                <input  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="Search..." v-model="eventSearchTerm">
                            </div>
                            <Table height="72vh">
                                <template v-slot:header>
                                    <tr>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Last</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">First</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Email</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Time Slot</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Address</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">City</th>
                                        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Phone</th>
                                        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                                        </th>
                                    </tr>
                                </template>
                                <template v-slot:body>
                                    <tr v-for="signup in filteredSignups" :class="{'bg-gray-200': signup.canceled, 'text-gray-200': signup.canceled, 'bg-sky-100': signup.arrived}">
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                                            {{truncate(signup.last_name)}}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{truncate(signup.first_name)}}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{truncate(signup.email_address)}}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{ dayjs(signup.arrival_time).format('M/D ddd h:mm A') }}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{truncate(signup.address)}}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{truncate(signup.city)}}
                                        </td>
                                        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-6">
                                            {{truncate(signup.phone)}}
                                        </td>
                                        <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                                            <a class="hover:text-sky-600 text-gray-400 cursor-pointer m-2 rounded-l p-2 bg-gray-100" :title="signup.arrived"
                                                @click="toggleArrived(signup)" 
                                                :class="{'text-sky-900': signup.arrived, 'bg-sky-200': signup.arrived}">
                                                <i class="fa-solid fa-shield-check"></i>
                                            </a>
                                            <a class="hover:text-sky-600 text-gray-400 cursor-pointer m-2 rounded-l p-2 bg-gray-100" 
                                                @click="toggleCancelled(signup)" 
                                                :class="{'text-red-900': signup.canceled, 'bg-red-400': signup.canceled}">
                                                <i class="fa-solid fa-ban"></i>
                                            </a> 
                                        </td>
                                    </tr>
                                </template>
                            </Table>
                        </template>
                        <template v-slot:actions>
                            <div class="flex flex-row-reverse">
                                <Button textColor="white" backgroundColor="red" @click="signupsId = null" class="mr-2">Close</Button>
                            </div>
                        </template>
                    </Modal>
                </Transition><Transition name="fade">
                    <Modal v-if="Object.keys(event).length > 0">
                        <template v-slot:content>
                            <div class="grid grid-cols-9 gap-4">
                                <div class="class col-span-3">
                                    <label for="title" class="block text-sm font-medium leading-6 text-gray-900">Title</label>
                                    <div class="mt-1">
                                        <input type="text" name="title" id="title" class="block w-full shadow-sm sm:text-sm focus:ring-sky-500 focus:border-sky-500 border-gray-300 rounded-md" v-model="event.title">
                                    </div>
                                </div>
                                <div class="class col-span-3">
                                    <label for="body" class="block text-sm font-medium leading-6 text-gray-900">Body</label>
                                    <div class="mt-1">
                                        <input type="text" name="body" id="body" class="block w-full shadow-sm sm:text-sm focus:ring-sky-500 focus:border-sky-500 border-gray-300 rounded-md" v-model="event.body">
                                    </div>
                                </div>
                                <div class="class col-span-3">
                                </div>
                                <div class="class col-span-3">
                                    <label for="date_start" class="block text-sm font-medium leading-6 text-gray-900">Start</label>
                                    <div class="mt-1">
                                        <input type="datetime-local" name="date_start" id="date_start" class="block w-full shadow-sm sm:text-sm focus:ring-sky-500 focus:border-sky-500 border-gray-300 rounded-md" v-model="event.date_start">
                                    </div>
                                </div>
                                <div class="class col-span-3">
                                    <label for="date_end" class="block text-sm font-medium leading-6 text-gray-900">End</label>
                                    <div class="mt-1">
                                        <input type="datetime-local" name="date_end" id="date_end" class="block w-full shadow-sm sm:text-sm focus:ring-sky-500 focus:border-sky-500 border-gray-300 rounded-md" v-model="event.date_end">
                                    </div>
                                </div>
                                <div class="class col-span-3">
                                </div>
                                <div class="class col-span-3">
                                    <label for="image" class="block text-sm font-medium leading-6 text-gray-900">Image</label>
                                    <div class="mt-1">
                                        <img :src="event.image" alt="" class="max-w-xs rounded-md m-3 border-2 border-slate-100 max-h-24">
                                        <input type="file" name="image" id="image" @change="uploadFile($event, event)" accept="image/*"
                                            class="block w-full shadow-sm sm:text-sm focus:ring-sky-500 focus:border-sky-500 border-gray-300 rounded-md" ref="file">
                                    </div>
                                </div>
                            </div>
                        </template>
                        <template v-slot:actions>
                            <div class="flex flex-row-reverse">
                                <Button textColor="white" backgroundColor="red" @click="event = {}" class="mr-2">Close</Button>
                                <Button textColor="white" backgroundColor="sky" @click="save" class="mr-2">Save</Button>
                            </div>
                        </template>
                    </Modal>
                </Transition>
            </main>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useBaseUrlStore } from '@/stores/baseUrl'
import axios from 'axios'
import Table from '@/components/utility/Table.vue'
import Modal from '@/components/utility/Modal.vue'
import Button from '@/components/utility/Button.vue'
import CampManager from '@/components/camp/CampManager.vue'
import { truncate } from 'lodash-es'
import dayjs from 'dayjs'

const baseUrlStore = useBaseUrlStore()
let currentView = ref('Events')
let searchTerm = ref('')
let eventSearchTerm = ref('')
let events = ref([])
let event = ref({})
let file = ref(null)
let signups = ref([])
let signupsId = ref(null)

const fileName = computed(() => file.value?.name)
const fileExtension = computed(() => fileName.value?.substr(fileName.value?.lastIndexOf(".") + 1))
const fileMimeType = computed(() => file.value?.type)

let filteredSignups = computed(() => {
    var filtered = signups.value.filter(signup => {
        return signup.last_name.toLowerCase().includes(eventSearchTerm.value.toLowerCase()) || 
            signup.first_name.toLowerCase().includes(eventSearchTerm.value.toLowerCase()) ||
            signup.email_address.toLowerCase().includes(eventSearchTerm.value.toLowerCase()) ||
            signup.city.toLowerCase().includes(eventSearchTerm.value.toLowerCase()) ||
            signup.phone.toLowerCase().includes(eventSearchTerm.value.toLowerCase())
    })
    // sort by arrival time
    return filtered.sort((a, b) => {
        return new Date(a.arrival_time) - new Date(b.arrival_time)
    })
})

let countConfirmed = (signups) => {
    return signups.filter(signup => {
        return signup.arrived
    }).length
}

let countCancelled = (signups) => {
    return signups.filter(signup => {
        return signup.canceled
    }).length
}

let countTotal = (signups) => {
    return signups.length
}

let filteredEvents = computed(() => {
    return events.value.filter(event => {
        return event.title.toLowerCase().includes(searchTerm.value.toLowerCase())
    })
})

let editEvent = (incomingEvent) => {
    event.value = Object.assign({}, incomingEvent)
}

const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = () => resolve(reader.result.split(',')[1])
    reader.onerror = reject
})

let getEventById = (events, id) => {
    return events.find(event => event.id == id)
}

let toggleCancelled = (signup) => {
    axios.post(`${baseUrlStore.baseUrl}/api/v1/signups/${signup.id}/cancel`, {})
        .then((response) => {
            signup.canceled = response.data.canceled
        })
        .catch(error => {
            console.log(error)
        })
}
let toggleArrived = (signup) => {
    axios.post(`${baseUrlStore.baseUrl}/api/v1/signups/${signup.id}/arrived`, {})
        .then((response) => {
            signup.arrived = response.data.arrived
        })
        .catch(error => {
            console.log(error)
        })
}

let viewSignups = (event) => {
    axios.get(`${baseUrlStore.baseUrl}/api/v1/events/${event.id}`)
        .then(response => {
            signups.value = response.data.signups
            signupsId.value = event.id
        })
        .catch(error => {
            console.log(error)
        })
}

let addNew = () => {
    event.value = {
        id: null,
        title: '',
        body: '',
        image: '',
        date_start: '',
        date_end: '',
    }
}

let uploadFile = async ($event, event) => {
    file.value = $event.target.files[0]
    const encodedFile = await toBase64(file.value)

    const data = {
        file: encodedFile,
        fileName: fileName.value,
        fileExtension: fileExtension.value,
        fileMimeType: fileMimeType.value,
    }
    try {
        const endpoint = `${baseUrlStore.baseUrl}/api/v1/events`
        const response = await axios.post(endpoint, data)
        event.image = response.data.url
    } catch (error) {
        console.error(error)
    }
}

let save = () => {
    axios.post(`${baseUrlStore.baseUrl}/api/v1/events`, {
        id: event.value.id,
        title: event.value.title,
        body: event.value.body,
        image: event.value.image,
        date_start: event.value.date_start,
        date_end: event.value.date_end,
    })
        .then(response => {
            event.value = {}
            update()
        })
        .catch(error => {
            console.log(error)
        })
}


let update = () => {
    axios.get(`${baseUrlStore.baseUrl}/api/v1/events`)
        .then(response => {
            events.value = response.data.events
        })
        .catch(error => {
            console.log(error)
        })
}

onMounted(() => {
    update()
})

</script>
