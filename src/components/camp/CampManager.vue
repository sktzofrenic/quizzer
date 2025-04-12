<template>
    <div class="grid grid-cols-1 sm:grid-cols-9 gap-10">
        <div class="sm:col-span-2">
            <div class="bg-slate-300 rounded-lg p-5">
                <div class="-my-2">
                    <div class="flex gap-x-4 py-2 text-lg font-semibold leading-6 text-slate-500 disabled">
                        Camp Menu
                    </div>
                    <a class="flex gap-x-4 py-2 text-sm font-semibold leading-6 text-slate-900 pl-5" 
                        :class="{'bg-slate-50 rounded-lg': view == 'years'}" 
                        style="cursor: pointer;"
                        @click="view = 'years'">
                        Camp Years
                    </a>
                    <a class="flex gap-x-4 py-2 text-sm font-semibold leading-6 text-slate-900 pl-5 mt-2" 
                        :class="{'bg-slate-50 rounded-lg': view == 'coupons'}" 
                        style="cursor: pointer;"
                        @click="view = 'coupons'">
                        Camp Coupons
                    </a>
                    <a class="flex gap-x-4 py-2 text-sm font-semibold leading-6 text-slate-900 pl-5 mt-2" 
                        :class="{'bg-slate-50 rounded-lg': view == 'registrations'}" 
                        style="cursor: pointer;"
                        @click="view = 'registrations'">
                        Registrations
                    </a>
                </div>
            </div>
        </div>
        <div class="sm:col-span-7" >
            <div class="sm:flex sm:items-center">
                <div class="sm:flex-auto">
                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Filter</label>
                    <div class="mb-2 max-w-sm">
                        <input  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="Church Name..." v-model="searchTerm">
                    </div>
                    <!-- year selection drop down -->
                    <div v-if="view == 'registrations'" class="mb-2  grid-cols-2 grid gap-1">
                        <select v-model="weekFilter" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6">
                            <option value="">Select Week</option>
                            <option v-for="week in campWeeks" :value="week.id">
                                {{ week.camp_year.year}} -  {{dayjs(week.start_date).format('MM/DD')}} to {{dayjs(week.end_date).format('MM/DD')}} {{week.name}}
                            </option>
                        </select>
                        <div>
                            Counselors
                            <div 
                                class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block mr-2">
                                <strong>
                                    {{ totalMaleCounselors }}
                                </strong> 
                            </div>
                            <div 
                                class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                <strong>
                                    {{ totalFemaleCounselors }}
                                </strong> 
                            </div>
                            Campers
                            <div 
                                class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block mr-2">
                                <strong>
                                    {{ totalMaleCampers}}
                                </strong> 
                            </div>
                            <div 
                                class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                <strong>
                                    {{ totalFemaleCampers}}
                                </strong> 
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none grid grid-cols-2 gap-1">
                    <button type="button" class="block rounded-md bg-sky-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600" @click="addNew">Add New</button>
                    <button type="button" class="block rounded-md bg-gray-300 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outlibg-gray-600" @click="addNew">Print</button>
                    <button type="button" class="block rounded-md bg-slate-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-slate-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-slate-600" @click="addNew">Export</button>
                </div>
            </div>
            <Table v-if="view == 'years'">
                <template v-slot:header>
                    <tr>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Year</th>
                        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                            <span class="sr-only">Edit</span>
                        </th>
                    </tr>
                </template>
                <template v-slot:body>
                    <tr v-for="year in filteredYears">
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ year.year }}
                        </td>
                        <td class="whitespace nowrap  text-sm text-gray-500">
                            <Button @click="editRegistration(registration)" backgroundColor="slate" textColor="white" class="mt-2">Edit</Button>
                        </td>
                    </tr>
                </template>
            </Table>
            <Table v-if="view == 'coupons'">
                <template v-slot:header>
                    <tr>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Code</th>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Year</th>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Discount</th>
                        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                            <span class="sr-only">Edit</span>
                        </th>
                    </tr>
                </template>
                <template v-slot:body>
                    <tr v-for="coupon in filteredCoupons">
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ coupon.coupon_code }}
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ coupon.camp_year.year }}
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ coupon.discount_amount }}
                        </td>
                        <td class="whitespace nowrap  text-sm text-gray-500">
                            <Button @click="deleteCoupon(coupon.id)" backgroundColor="red" textColor="white" class="mt-2">Delete</Button>
                        </td>
                    </tr>
                </template>
            </Table>
            <Table v-if="view == 'registrations'">
                <template v-slot:header>
                    <tr>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Church</th>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Week</th>
                        <th scope="col" colspan="2" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Counselors</th>
                        <th scope="col" colspan="2" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Campers</th>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Non-Campers</th>
                        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 ">Amt Paid</th>
                        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                            <span class="sr-only">Edit</span>
                        </th>
                    </tr>
                </template>
                <template v-slot:body>
                    <tr v-for="registration in filteredRegistrations">
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ registration.camp_church.name }} 
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">

                            {{registration.camp_week && registration.camp_week.camp_year ? registration.camp_week.camp_year.year : ''}}
                            {{ registration.camp_week ? registration.camp_week.name : '' }}
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            <div v-if="registration.estimated_number_of_male_counselors" 
                                class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block">
                                <strong>
                                    {{ registration.estimated_number_of_male_counselors}}
                                </strong> 
                            </div>
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            <div v-if="registration.estimated_number_of_female_counselors" 
                                class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                <strong>
                                    {{ registration.estimated_number_of_female_counselors}}
                                </strong> 
                            </div>
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            <div v-if="registration.estimated_number_of_male_campers" 
                                class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block">
                                <strong>
                                    {{ registration.estimated_number_of_male_campers}}
                                </strong> 
                            </div>
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            <div v-if="registration.estimated_number_of_female_campers"
                                class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                <strong>
                                    {{ registration.estimated_number_of_female_campers}}
                                </strong> 
                            </div>
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            <div v-if="registration.estimated_non_campers_children_attendees" 
                                class="bg-slate-400 rounded-lg px-2 text-slate-100 inline-block">
                                <strong>
                                    {{ registration.estimated_non_campers_children_attendees}}
                                </strong> 
                            </div>
                        </td>
                        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {{ getDinero(getPaymentSum(registration.camp_registration_payments)) }}
                        </td>
                        <td class="whitespace-nowrap text-sm text-gray-500" >
                            <Button @click="editRegistration(registration)" backgroundColor="slate" textColor="white" class="">Edit</Button>
                        </td>
                    </tr>
                </template>
            </Table>
        </div>
        <transition name="fade">
            <Modal v-if="showRegistrationModal">
                <template v-slot:content >
                    <div class="max-h-[80vh] overflow-y-auto p-8">
                        <div class="px-4 sm:px-0 flex flex-wrap">
                            <div>
                                <h3 class="text-base font-semibold leading-7 text-gray-900">
                                    {{activeRegistration.camp_church.name}}
                                </h3>
                                <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
                                <div>
                                    Pastor: 
                                    {{ activeRegistration.camp_church.senior_pastor_first_name }} 
                                    {{ activeRegistration.camp_church.senior_pastor_last_name }}
                                </div>
                                {{ activeRegistration.camp_church.address }}
                                <div v-if="activeRegistration.camp_church.city">
                                    {{ activeRegistration.camp_church.city }}, {{ activeRegistration.camp_church.state }} {{ activeRegistration.camp_church.zip }}
                                </div>
                                </p>
                            </div>
                            <div class="ml-auto">
                                <div>
                                    Counselors
                                    <div 
                                        class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block mr-2">
                                        <strong>
                                            {{ activeRegistration.estimated_number_of_male_counselors}}
                                        </strong> 
                                    </div>
                                    <div 
                                        class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                        <strong>
                                            {{ activeRegistration.estimated_number_of_female_counselors || 0 }}

                                        </strong> 
                                    </div>
                                    Campers
                                    <div 
                                        class="bg-blue-400 rounded-lg px-2 text-blue-100 inline-block mr-2">
                                        <strong>
                                            {{ activeRegistration.estimated_number_of_male_campers || 0}}
                                        </strong> 
                                    </div>
                                    <div 
                                        class="bg-pink-400 rounded-lg px-2 text-pink-100 inline-block">
                                        <strong>
                                            {{ activeRegistration.estimated_number_of_female_campers || 0}}
                                        </strong> 
                                    </div>
                                </div>
                            </div>
                            <div class="ml-auto">
                                <div>
                                    Non-Campers
                                    <div 
                                        class="bg-slate-400 rounded-lg px-2 text-slate-100 inline-block mr-2">
                                        <strong>
                                            {{ activeRegistration.estimated_non_campers_children_attendees || 0}}
                                        </strong> 
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="mt-6 border-t border-gray-100">
                            <dl class="divide-y divide-gray-100">
                                <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                                    <dt class="text-sm font-medium leading-6 text-gray-900">Group Leader</dt>
                                    <dd class="mt-1 flex text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                                        <span class="flex-grow">
                                            {{ activeRegistration.camp_church.group_leader_title }} 
                                            {{ activeRegistration.camp_church.group_leader_first_name }} 
                                            {{ activeRegistration.camp_church.group_leader_last_name }}
                                            <div>
                                                <strong>Phone:</strong>   {{ activeRegistration.camp_church.group_leader_phone }}
                                            </div>
                                            <div>
                                                <strong>Email:</strong>   {{ activeRegistration.camp_church.group_leader_email }}
                                            </div>
                                        </span>
                                        <span class="ml-4 flex-shrink-0">
                                            <button type="button" class="rounded-md bg-white font-medium text-indigo-600 hover:text-indigo-500">Update</button>
                                        </span>
                                    </dd>
                                </div>
                                <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                                    <dt class="text-sm font-medium leading-6 text-gray-900">Camp Week</dt>
                                    <dd class="mt-1 flex text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                                        <span class="flex-grow text-lg font-bold" v-if="activeRegistration.camp_week">
                                            {{activeRegistration.camp_week && activeRegistration.camp_week.camp_year ? activeRegistration.camp_week.camp_year.year : ''}}
                                            {{activeRegistration.camp_week.name}}
                                            <div>
                                                From
                                                {{dayjs(activeRegistration.camp_week.start_date).format('MM/DD')}} to {{dayjs(activeRegistration.camp_week.end_date).format('MM/DD')}}
                                            </div>
                                        </span>
                                        <span class="ml-4 flex-shrink-0">
                                            <button type="button" class="rounded-md bg-white font-medium text-indigo-600 hover:text-indigo-500">Update</button>
                                        </span>
                                    </dd>
                                </div>
                                <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                                    <dt class="text-sm font-medium leading-6 text-gray-900">Payments</dt>
                                    <dd class="mt-1 flex flex-col text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                                        <div class="bg-gray-50 shadow-sm ring-1 ring-gray-900/5" v-for="payment in activeRegistration.camp_registration_payments">
                                            <dl class="flex flex-wrap">
                                                <div class="flex-auto pl-6 pt-4">
                                                    <dt class="text-sm font-semibold leading-6 text-gray-900">Amount</dt>
                                                    <dd class="mt-1 text-base font-semibold leading-6 text-gray-900">{{getDinero(payment.amount)}} for {{payment.number_of_people}} 
                                                        <span v-if="payment.number_of_people === 1">person</span> 
                                                        <span v-else>people</span> 
                                                    </dd>
                                                </div>
                                                <div class="flex-none self-end px-6 pt-4">
                                                    <dt class="sr-only">Status</dt>
                                                    <dd class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">Paid</dd>
                                                </div>
                                                <div class="mt-4 flex w-full flex-none gap-x-4 px-6">
                                                    <dt class="flex-none">
                                                        <span class="sr-only">Paid On</span>
                                                        <i class="fa-solid fa-calendar-days"></i>
                                                    </dt>
                                                    <dd class="pb-3 text-sm leading-6 text-gray-500">
                                                        <time datetime="2023-01-31">{{dayjs(payment.created_at).format('MMM D, YYYY')}}</time>
                                                    </dd>
                                                </div>
                                            </dl>
                                        </div>
                                    </dd>
                                </div>
                                <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                                    <dt class="text-sm font-medium leading-6 text-gray-900">Additional Info</dt>
                                    <dd class="mt-1 flex text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                                        <span class="flex-grow">
                                            {{ activeRegistration.additional_information }}
                                        </span>
                                        <span class="ml-4 flex-shrink-0">
                                            <button type="button" class="rounded-md bg-white font-medium text-indigo-600 hover:text-indigo-500">Update</button>
                                        </span>
                                    </dd>
                                </div>
                                <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                                    <dt class="text-sm font-medium leading-6 text-gray-900">Misc</dt>
                                    <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                                        <ul role="list" class="divide-y divide-gray-100 rounded-md border border-gray-200">
                                            <li class="flex items-center justify-between py-4 pl-4 pr-5 text-sm leading-6">
                                                <div class="flex w-0 flex-1 items-center">
                                                    <div class="ml-4 flex min-w-0 flex-1 gap-2">
                                                        <span class="truncate font-medium">Created At</span>
                                                        <span class="flex-shrink-0 text-gray-400">
                                                            {{dayjs(activeRegistration.created_at).format('MMM D, YYYY')}}
                                                        </span>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="flex items-center justify-between py-4 pl-4 pr-5 text-sm leading-6">
                                                <div class="flex w-0 flex-1 items-center">
                                                    <div class="ml-4 flex min-w-0 flex-1 gap-2">
                                                        <span class="truncate font-medium">Updated At</span>
                                                        <span class="flex-shrink-0 text-gray-400">
                                                            {{dayjs(activeRegistration.updated_at).format('MMM D, YYYY')}}
                                                        </span>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="flex items-center justify-between py-4 pl-4 pr-5 text-sm leading-6">
                                                <div class="flex w-0 flex-1 items-center">
                                                    <div class="ml-4 flex min-w-0 flex-1 gap-2">
                                                        <Button @dblclick="deleteRegistration(activeRegistration.id)" backgroundColor="red" textColor="white">Delete</Button>
                                                    </div>
                                                    <p class="text-red-600 text-lg">All (double) Clicks are Final! Cannot be undone!</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </dd>
                                </div>
                            </dl>
                        </div>
                    </div>
                </template>
                <template v-slot:actions>
                    <div class="flex justify-end">
                        <Button @click="showRegistrationModal = false" backgroundColor="slate" textColor="white">Close</Button>
                    </div>
                </template>
            </Modal>
        </transition>
        <transition name="fade">
            <Modal v-if="showModal">
                <template v-slot:content>
                    <div class="text-lg font-semibold text-slate-900">Add Coupon</div>
                    <div class="mt-4">
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="church" class="block text-sm font-medium leading-6 text-gray-900">Coupon Code</label>
                                <input type="text" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" v-model="couponCode">
                            </div>
                            <div>
                                <label for="week" class="block text-sm font-medium leading-6 text-gray-900">Discount Amount</label>
                                <input type="text" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" v-model="discountAmount">
                            </div>
                            <div>
                                <label for="week" class="block text-sm font-medium leading-6 text-gray-900">Camp Year</label>
                                <input type="text" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" v-model="couponCampYear">
                            </div>
                        </div>
                    </div>
                </template>
                <template v-slot:actions>
                    <div class="flex justify-end">
                        <Button @click="closeModal" backgroundColor="slate" textColor="white">Close</Button>
                        <Button @click="saveCoupon" backgroundColor="sky" textColor="white" class="ml-2">Save</Button>
                    </div>
                </template>
            </Modal>
        </transition>
    </div>
</template>

<script setup>
import { useBaseUrlStore } from '@/stores/baseUrl'
import { ref, onMounted, computed, watch} from 'vue'
import Button from '../utility/Button.vue'
import Table from '@/components/utility/Table.vue'
import Modal from '@/components/utility/Modal.vue'
import getDinero from '@/components/utility/dinero.js'
import dayjs from 'dayjs'

var loading = ref(false)
var baseUrl = useBaseUrlStore()
var view = ref('registrations')

var weekFilter = ref('')

const registrations = ref([])
const activeRegistration = ref(null)
const showRegistrationModal = ref(false)
const coupons = ref([])
const years = ref([])
const userId = ref(null)
const searchTerm = ref('')
const showModal = ref(false)
const couponCode = ref('')
const discountAmount = ref('')
const couponCampYear = ref('')
const campWeeks = ref([])

const saveRegistration = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?saveRegistration=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            registration: activeRegistration.value
        })
    }).then(async data => {
        data = await data.json()
        loading.value = false
        showRegistrationModal.value = false
        getRegistrations()
    }).catch(error => {
        loading.value = false
    })
}

const editRegistration = (registration) => {
    activeRegistration.value = registration
    showRegistrationModal.value = true
}

const closeModal = () => {
    showModal.value = false
}


const addNew = () => {
    if (view.value == 'years') {
    } else if (view.value == 'coupons') {
        showModal.value = true
    } else if (view.value == 'registrations') {
    }
}

const deleteRegistration = (registrationId) => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?deleteRegistration=${registrationId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(async data => {
            loading.value = false
            showRegistrationModal.value = false
            getRegistrations()
        })
        .catch(error => {
            loading.value = false
        })
}

if (window.USER_ID) {
    userId.value = window.USER_ID
}

// compute filtered registrations
const filteredRegistrations = computed(() => {
    return registrations.value.filter(registration => {
        if (weekFilter.value) {
            return (
                registration.camp_week !== null &&
                registration.camp_week.id == weekFilter.value && 
                registration.camp_church.name.toLowerCase().includes(searchTerm.value.toLowerCase())
            )
        } else {
            return registration.camp_church.name.toLowerCase().includes(searchTerm.value.toLowerCase())
        }
    })
})

// compute filtered coupons
const filteredCoupons = computed(() => {
    return coupons.value.filter(coupon => {
        return coupon.coupon_code.toLowerCase().includes(searchTerm.value.toLowerCase())
    })
})

const totalFemaleCampers = computed(() => {
    let sum = 0
    filteredRegistrations.value.forEach(registration => {
        sum += registration.estimated_number_of_female_campers 
    })
    return sum 
})

const totalMaleCampers = computed(() => {
    let sum = 0
    filteredRegistrations.value.forEach(registration => {
        sum += registration.estimated_number_of_male_campers
    })
    return sum
})

const totalMaleCounselors = computed(() => {
    let sum = 0
    filteredRegistrations.value.forEach(registration => {
        sum += registration.estimated_number_of_male_counselors
    })
    return sum
})

const totalFemaleCounselors = computed(() => {
    let sum = 0
    filteredRegistrations.value.forEach(registration => {
        sum += registration.estimated_number_of_female_counselors
    })
    return sum
})


const getCampWeeks = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?getCampWeeks=true`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            campWeeks.value = data.camp_weeks
        })
        .catch(error => {
            loading.value = false
        })
}

// compute filtered Years
const filteredYears = computed(() => {
    return years.value.filter(year => {
        if (!searchTerm.value) {
            return true
        } else {
            return year.year == parseInt(searchTerm.value.toLowerCase())
        }
    })
})

const getPaymentSum = (payments) => {
    let sum = 0
    payments.forEach(payment => {
        sum += payment.amount
    })
    return sum
}

const saveCoupon = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?saveCoupon=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            coupon_code: couponCode.value,
            discount_amount: discountAmount.value,
            camp_year: couponCampYear.value
        })
    }).then(async data => {
        data = await data.json()
            console.log(data)
        loading.value = false
        showModal.value = false
        getCoupons()
    }).catch(error => {
        loading.value = false
    })
}

const getYears = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?allYears=true`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(async data => {
        data = await data.json()
        loading.value = false
        years.value = data.years
    }).catch(error => {
        loading.value = false
    })
}

const getCoupons = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?allCoupons=true`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(async data => {
        data = await data.json()
        loading.value = false
        coupons.value = data.coupons
    }).catch(error => {
        loading.value = false
    })
}

const deleteCoupon = (couponId) => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?deleteCoupon=${couponId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(async data => {
        data = await data.json()
        loading.value = false
        getCoupons()
    }).catch(error => {
        loading.value = false
    })
}

const getRegistrations = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?allRegistrations=true`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(async data => {
        data = await data.json()
        loading.value = false
        registrations.value = data.registrations
    }).catch(error => {
        loading.value = false
    })
}

watch(view, (newValue) => {
    if (newValue == 'years') {
        getYears()
    } else if (newValue == 'coupons') {
        getCoupons()
    } else if (newValue == 'registrations') {
        getRegistrations()
    }
})

onMounted(() => {
    getRegistrations()
    getCampWeeks()
})

</script>
