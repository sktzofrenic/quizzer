<template>
    <div>
        <h1 class="text-3xl font-bold text-gray-900 mb-4">Register for Camp</h1>
        <div class="mx-auto max-w-lg" v-if="view == 'register'">
            <div class="text-center">
                <i class="fa-solid fa-church text-5xl"></i>
                <h2 class="mt-2 text-base font-semibold leading-6 text-gray-900">Registration Details</h2>
            </div>
            <div class="mt-6 bg-slate-200 rounded-lg px-4 pt-1 pb-4">
                <h2 class="mt-2 text-base font-semibold leading-6 text-gray-900">Church Info</h2>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.name">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Address</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.address">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">City</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.city">
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="mt-4">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">State</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.state">
                        </div>
                    </div>
                    <div class="mt-4">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Zip Code</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.zip_code">
                        </div>
                    </div>
                </div>
                <div class="mt-4">
                    <label for="phone-number" class="block text-sm font-medium leading-6 text-gray-900">Phone Number</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" name="phone-number" id="phone-number" class="block w-full rounded-md border-0 py-1.5  text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="+1 (555) 987-6543" v-model="registration.camp_church.church_phone">
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="mt-4">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Pastor First Name</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.senior_pastor_first_name">
                        </div>
                    </div>
                    <div class="mt-4">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Pastor Last Name</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.senior_pastor_last_name">
                        </div>
                    </div>
                </div>
                <h5 class="col-span-16 text-sm font-semibold mt-4 text-gray-900">Group Leader</h5>
                <div class="grid grid-cols-12 gap-3 rounded-lg border-4 border-sky-500 bg-sky-400 pt-0 pb-3 px-2 mt-2">
                    <div class="mt-4 col-span-7">
                        <label for="phone-number" class="block text-sm font-medium leading-6 text-gray-900">First Name</label>
                        <div class="relative rounded-md shadow-sm">
                            <div class="absolute inset-y-0 left-0 flex items-center">
                                <label for="country" class="sr-only">Title</label>
                                <select class="h-full rounded-md border-0 bg-transparent py-0 pl-3 pr-7 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm"
                                 v-model="registration.camp_church.group_leader_title">
                                    <option value="Mr.">Mr.</option>
                                    <option value="Mrs.">Mrs.</option>
                                    <option value="Ms.">Ms.</option>
                                    <option value="Pastor">Pstr</option>
                                </select>
                            </div>
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pl-16 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.group_leader_first_name">
                        </div>
                    </div>
                    <div class="mt-4 col-span-5">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Last Name</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.group_leader_last_name">
                        </div>
                    </div>
                    <div class="col-span-6">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Phone</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.group_leader_phone">
                        </div>
                    </div>
                    <div class="col-span-6">
                        <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                        <div class="relative rounded-md shadow-sm">
                            <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.camp_church.group_leader_email">
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-6 bg-sky-200 rounded-lg px-4 pt-1 pb-4">
                <h2 class="mt-2 text-base font-semibold leading-6 text-gray-900">Week Info</h2>
                <div class="pt-4">
                    <label for="location" class="block text-sm font-medium leading-6 text-gray-900">Which Camp Week?</label>
                    <select id="location" name="location" class="block w-full rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-sky-600 sm:text-sm sm:leading-6" v-model="registration.camp_week_id">
                        <option v-for="week in campWeeks" :value="week.id">{{week.camp_year.year}} {{week.name}} ({{dayjs(week.start_date).format('M/D')}} to {{dayjs(week.end_date).format('M/D')}})</option>
                    </select>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Estimated # Male Counselors</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.estimated_number_of_male_counselors">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Estimated # Female Counselors</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.estimated_number_of_female_counselors">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Estimated # Male Campers</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.estimated_number_of_male_campers">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="account-number" class="block text-sm font-medium leading-6 text-gray-900">Estimated # Female Campers</label>
                    <div class="relative rounded-md shadow-sm">
                        <input type="text" class="block w-full rounded-md border-0 py-1.5 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6" placeholder="" v-model="registration.estimated_number_of_female_campers">
                    </div>
                </div>
                <div class="mt-4">
                    <label for="comment" class="block text-sm font-medium leading-6 text-gray-900">Additional Info</label>
                    <div class="">
                        <textarea rows="4" name="comment" id="comment" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-sky-600 sm:text-sm sm:leading-6"  v-model="registration.additional_information"></textarea>
                    </div>
                </div>
            </div>
            <div class="flex justify-between my-4">
                <Button backgroundColor="slate" textColor="white" class="mt-2" @click="cancelRegistration">Back</Button>
                <Button backgroundColor="sky" textColor="white" class="mt-2" @click="saveRegistration">Save</Button>
            </div>
        </div>
        <div class="mx-auto max-w-lg" v-if="view == 'home'">
            <div>
                <div class="text-center">
                    <i class="fa-solid fa-church text-5xl"></i>
                    <h2 class="mt-2 text-base font-semibold leading-6 text-gray-900">Add Registration</h2>
                    <p class="mt-1 text-sm text-gray-500">
                        Enter the name of the church you would like to register for camp.
                    </p>
                </div>
                <div class="mt-6 flex">
                    <label for="email" class="sr-only">Church Name</label>
                    <input type="text" name="churchName" id="churchName" v-model="churchName"
                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset 
                               ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset 
                               focus:ring-sky-600 sm:text-sm sm:leading-6" 
                        placeholder="Church Name">
                    <button type="submit" 
                        @click="startRegistration"
                        class="ml-4 flex-shrink-0 rounded-md bg-sky-600 px-3 py-2 text-sm 
                        font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline 
                        focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600">
                        New Registration
                    </button>
                </div>
            </div>
            <div class="text-center mt-8 border-t-2 border-gray-300 pt-8" v-if="registrations.length === 0">
                <i class="fa-thin fa-church text-5xl"></i>
                <h3 class="mt-2 text-sm font-semibold text-gray-900">No Church Registrations</h3>
                <p class="mt-1 text-sm text-gray-500">Get started by registering above.</p>
            </div>
            <div class="mt-10" v-else>
                <transition name="fade">
                    <div class="rounded-md bg-blue-50 p-4" v-if="message">
                        <div class="flex">
                            <div class="flex-shrink-0">
                                <svg class="h-5 w-5 text-blue-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M8.485 2.495c.673-1.167 2.357-1.167 3.03 0l6.28 10.875c.673 1.167-.17 2.625-1.516 2.625H3.72c-1.347 0-2.189-1.458-1.515-2.625L8.485 2.495zM10 5a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0v-3.5A.75.75 0 0110 5zm0 9a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                                </svg>
                            </div>
                            <div class="ml-3">
                                <h3 class="text-sm font-medium text-blue-800">Alert</h3>
                                <div class="mt-2 text-sm text-blue-700">
                                    <p>{{message}}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </transition>
                <h3 class="text-sm font-medium text-gray-500">Previous Church Registrations Submitted</h3>
                <ul role="list" 
                    class="mt-4 divide-y divide-gray-200  border-gray-200 rounded-lg border-2" 
                    v-for="reg in registrations">
                    <li class="flex items-center justify-between space-x-3 py-4">
                        <div class="flex min-w-0 flex-1 items-center space-x-3">
                            <div class="flex-shrink-0">
                            </div>
                            <div class="min-w-0 flex-1">
                                <p class="truncate text-sm font-medium text-gray-900">
                                    {{reg.camp_church.name}}
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500">
                                    {{reg.user.first_name}} {{reg.user.last_name}}
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500" v-if="reg.camp_week">
                                    <strong class="text-xl">{{reg.camp_week.camp_year.year}}</strong> {{reg.camp_week.name}} ({{dayjs(reg.camp_week.start_date).format('M/D')}} to {{dayjs(reg.camp_week.end_date).format('M/D')}})
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500">
                                    Male Counselors: {{reg.estimated_number_of_male_counselors}}
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500">
                                    Female Counselors: {{reg.estimated_number_of_female_counselors}}
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500">
                                    Male Campers: {{reg.estimated_number_of_male_campers}}
                                </p>
                                <p class="truncate text-sm font-medium text-gray-500">
                                    Female Campers: {{reg.estimated_number_of_female_campers}}
                                </p>
                            </div>
                        </div>
                        <div class="flex flex-row gap-1 pr-4">
                            <Button backgroundColor="sky" textColor="white" class="mt-2" @click="editRegistration(reg.id)">Edit</Button>
                            <Button 
                                backgroundColor="red"
                                textColor="white"
                                class="mt-2"
                                @click="deleteRegistration(reg.id)"
                                v-if="reg.registration_amount_paid === 0 || reg.registration_amount_paid === null">Delete</Button>
                        </div>
                    </li>
                    <div class="lg:col-start-3 lg:row-end-1">
                        <div class="bg-gray-50 shadow-sm ring-1 ring-gray-900/5" v-for="payment in reg.camp_registration_payments">
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
                    </div>

                    <dl class="mx-auto grid grid-cols-2 gap-px bg-gray-900/5 sm:grid-cols-2">
                        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2 bg-white px-4 py-10 sm:px-6 xl:px-8">
                            <dt class="text-sm font-medium leading-6 text-gray-500">Amount Due</dt>
                            <dd class="w-full flex-none text-3xl font-medium leading-10 tracking-tight text-gray-900">{{getDinero(reg.registration_amount_due)}}</dd>
                        </div>
                        <div class="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2 bg-white px-4 py-10 sm:px-6 xl:px-8">
                            <dt class="text-sm font-medium leading-6 text-gray-500">Amount Paid</dt>
                            <dd class="w-full flex-none text-3xl font-medium leading-10 tracking-tight text-gray-900">{{getDinero(reg.registration_amount_paid)}}</dd>
                        </div>
                    </dl>
                    <div class="bg-white shadow">
                        <div class="px-4 py-5 sm:p-6" v-if="reg.registration_amount_due < 0">
                            <h3 class="text-base font-semibold leading-6 text-gray-900">Get a Refund</h3>
                            <div class="mt-2 max-w-xl text-sm text-gray-500">
                                <p>You've overpaid for registration fees!</p>
                                <p class="text-red-700 text-2xl">Contact us for a refund.</p>
                            </div>
                        </div>
                        <div class="px-4 py-5 sm:p-6" v-else-if="reg.registration_amount_due > 0">
                            <h3 class="text-base font-semibold leading-6 text-gray-900">Make a Payment</h3>
                            <div class="mt-2 max-w-xl text-sm text-gray-500">
                                <p>It looks like you owe <strong class="text-2xl">{{getDinero(reg.registration_amount_due - couponDiscount)}}</strong></p>
                            </div>
                            <div class="mt-5 sm:flex sm:items-center" v-if="!readyToPay">
                                <div class="w-full sm:max-w-xs">
                                    <input type="email" name="email" id="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Coupon Code" v-model="couponCode">
                                </div>
                                <button @click="getCouponDiscount" type="submit" class="mt-3 inline-flex w-full items-center justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 sm:ml-3 sm:mt-0 sm:w-auto">Apply</button>
                            </div>
                            <div v-if="couponDiscount != 0" class="mt-2 px-2 py-2 bg-indigo-50 rounded-lg">
                                <h2 class="text-base font-semibold leading-6 text-gray-900">Coupon Change Applied: New Total</h2>
                                <div class="flex flex-row gap-1">
                                    <div class="flex-none text-3xl font-medium leading-10 tracking-tight text-gray-900">
                                        {{getDinero(reg.registration_amount_due)}}
                                    </div> 
                                    <div class="flex-none text-xl font-medium leading-10 tracking-tight text-gray-900">
                                        <i class="fa-solid fa-minus"></i>
                                    </div> 
                                    <div class="flex-none text-3xl font-medium leading-10 tracking-tight text-gray-900">{{getDinero(couponDiscount)}}</div>
                                    <div class="flex-none text-xl font-medium leading-10 tracking-tight text-gray-900">
                                        <i class="fa-solid fa-equals"></i>
                                    </div>
                                    <div class="flex-none text-3xl font-medium leading-10 tracking-tight text-gray-900">
                                        {{getDinero(reg.registration_amount_due - couponDiscount)}}
                                    </div>
                                </div>
                            </div>
                            <div class="mt-5" v-show="!readyToPay">
                                <button type="button" class="inline-flex rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500" @click="createPaymentIntent(reg.id)">Pay With Card</button>
                            </div>
                            <form id="payment-form" class="mt-2" v-show="readyToPay" @submit.prevent="handleSubmit(reg.id)">
                                <div id="payment-element">
                                    <!--Stripe.js injects the Payment Element-->
                                </div>
                                <button id="submit" class="inline-flex items-center rounded-md bg-indigo-600 w-full text-center px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500 mt-2">
                                    <div class="spinner hidden" id="spinner"></div>
                                    <span id="button-text">Pay now</span>
                                </button>
                                <div id="payment-message" class="hidden"></div>
                            </form>
                        </div>
                        <div class="px-4 py-5 sm:p-6" v-else-if="(reg.registration_amount_paid === reg.registration_amount_due) || reg.registration_amount_due === 0">
                            <h3 class="text-base font-semibold leading-6 text-gray-900">All set!</h3>
                            <div class="mt-2 max-w-xl text-sm text-gray-500">
                                <p class="text-green-700 text-2xl">You're paid up for camp!</p>
                            </div>
                        </div>
                    </div>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import Button from '../utility/Button.vue'
import { useBaseUrlStore } from '@/stores/baseUrl'
import { ref, onMounted, computed } from 'vue'
import dayjs from 'dayjs'
import getDinero from '@/components/utility/dinero.js'


const location = window.location.pathname
var loading = ref(false)
var baseUrl = useBaseUrlStore()

const genRegistration = () => {
    return {
        id: null,
        camp_week: {
            id: null,
            camp_year: {
                id: null,
                year: null,
            }
        },
        camp_church: {
            id: null,
            name: '',
            address: '',
            city: '',
            state: '',
            zip_code: '',
            church_phone: '',
            group_leader_title: 'Mr.',
            group_leader_first_name: '',
            group_leader_last_name: '',
            group_leader_phone: '',
            group_leader_email: '',
            senior_pastor_first_name: '',
            senior_pastor_last_name: '',

        },
        user: {
            id: null,
            first_name: '',
            last_name: '',
        },
        estimated_number_of_male_counselors: 0,
        estimated_number_of_female_counselors: 0,
        estimated_number_of_male_campers: 0,
        estimated_number_of_female_campers: 0,
        estimated_non_campers_children_attendees: 0,
        additional_information: '',
    }
}

const totalSteps = 9
const churchName = ref('')
const registration = ref(genRegistration())
const view = ref('home')
const step = ref(1)
const registrations = ref([])
const couponCode = ref('')
const couponDiscount = ref(0)
const campWeeks = ref([])
const userId = ref(null)
const paymentIntent = ref(null)
const readyToPay = ref(false)
const message = ref('')

console.log(window.STRIPE_PUBLIC_KEY)
var stripe = Stripe(window.STRIPE_PUBLIC_KEY);
let elements

if (window.USER_ID) {
    userId.value = window.USER_ID
}

// next step
const nextStep = () => {
    step.value++
}

// previous step
const prevStep = () => {
    step.value--
}

const cancelRegistration = () => {
    view.value = 'home'
    // scroll to top of page
    window.scrollTo(0, 0)
    getRegistrations()
}

const flashMessage = (msg) => {
    message.value = msg
    setTimeout(() => {
        message.value = ''
    }, 3000)
}

const createPaymentIntent = (registrationId) => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?paymentIntent=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            registrationId: registrationId,
            couponAmount: couponDiscount.value
        })
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            console.log(data)
            if (data.success === true) {

                console.log(1)
                const { clientSecret } = { clientSecret: data.client_secret}
                console.log(clientSecret, 'secrate')

                readyToPay.value = true

                const appearance = {
                    theme: 'flat',
                    variables: { colorPrimaryText: '#262626' }
                };
                const options = { /* options */ };
                elements = stripe.elements({ clientSecret, appearance });
                const paymentElement = elements.create('payment', options);
                paymentElement.mount('#payment-element');
        
            } else {
                flashMessage('Could not start the payment. Something went wrong.')
            }
        })
        .catch(error => {
            loading.value = false
        })
}

async function handleSubmit(registrationId) {
    loading.value = true
    console.log('called???')

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
            // Make sure to change this to your payment completion page
            return_url:`${baseUrl.baseUrl}/api/v1/camp?finished=true&registrationId=${registrationId}`,
        },
    })

    console.log(error)

    // This point will only be reached if there is an immediate error when
    // confirming the payment. Otherwise, your customer will be redirected to
    // your `return_url`. For some payment methods like iDEAL, your customer will
    // be redirected to an intermediate site first to authorize the payment, then
    // redirected to the `return_url`.
    if (error.type === "card_error" || error.type === "validation_error") {
        flashMessage(error.message)
    } else {
        flashMessage("An unexpected error occurred.")
    }
    loading.value = false
}

// get coupon couponDiscount
const getCouponDiscount = () => {
    fetch(`${baseUrl.baseUrl}/api/v1/camp?getCampCoupons=${couponCode.value}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(async data => {
            data = await data.json()
            if (data.camp_coupon && data.success === true) {
                couponDiscount.value = data.camp_coupon.discount_amount
            } else {
                flashMessage('Coupon code not found')
                couponDiscount.value = 0
            }
        })
        .catch(error => {
            couponDiscount.value = 0
        })
}

const startRegistration = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?startRegistration=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            churchName: churchName.value,
            userId: userId.value
        })
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            view.value = 'register'
            registration.value = data.registration
        })
        .catch(error => {
            loading.value = false
        })
}

const editRegistration = (registrationId) => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?getRegistration=${registrationId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            view.value = 'register'
            registration.value = data.registration
        })
        .catch(error => {
            loading.value = false
        })
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
            getRegistrations()
        })
        .catch(error => {
            loading.value = false
        })
}

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

const saveRegistration = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?saveRegistration=true`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(registration.value)
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            view.value = 'home'
            getRegistrations()
        })
        .catch(error => {
            loading.value = false
        })
}

const getRegistrations = () => {
    loading.value = true
    fetch(`${baseUrl.baseUrl}/api/v1/camp?getRegistrations=${userId.value}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(async data => {
            data = await data.json()
            loading.value = false
            registrations.value = data.registrations
        })
        .catch(error => {
            loading.value = false
        })
}

onMounted(() => {
    getRegistrations()
    getCampWeeks()
})
</script>
<style>
/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.15s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.4s ease-in;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}</style>
