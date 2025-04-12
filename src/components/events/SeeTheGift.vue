<template>
    <div class="g-container">
        <div class="g-grid">
            <div class="g-block flush g-roksprocket-tabs-style-1 size-100">
                <div class="g-content">
                    <div id="vue-gift">
                        <div class="g-grid">
                            <div class="g-block box-red size-100">
                                <div class="g-content">
                                    <h1 class="text-4xl text-sky-500">Reserve Your Spot!<span class="fa fa-clock-o fa-fw"></span></h1>
                                    <p class="my-6">Due to limited seating, tickets are required for each performance. Our Sunday performance will include interpretation for the Deaf. You may reserve tickets below:</p>
                                    <!-- <a class="ui red button" href="/static/uploads/see_the_gift_poster.pdf">Download Flyer (PDF)</a> -->
                                </div>
                            </div>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-8">

                            <div class="g-block box1 size-33-3">
                                <div class="g-content">
                                    <h3 class="text-2xl text-sky-500">December 8th</h3>
                                    <p class="my-6">Doors open: <strong>6:00pm</strong> <br> Performance: <strong>7:00pm</strong></p>
                                    <!-- <p class="px-4 py-4 text-yellow-600 my-4 text-xl font-bold">Filling up Fast!</p> -->
                                    <!-- <a class="block w-full rounded-md bg-sky-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600" @click="reserve(0)" style="cursor:pointer;">Reserve Tickets</a> -->
                                    <p class="px-4 py-4 text-slate-600 rounded-md my-4 text-xl font-bold">Sold Out!</p>
                                    <button class="block w-full rounded-md bg-slate-600 px-3.5 py-2.5 text-center text-sm font-semibold text-slate-600 shadow-sm  disabled:bg-slate-100" @click="" disabled  style="cursor:pointer">Reserve Tickets</button>
                                </div>
                            </div>
                            <div class="g-block box2 size-33-3">
                                <div class="g-content">
                                    <h3 class="text-2xl text-sky-500">December 9th</h3>
                                    <p class="my-6">Doors open: <strong>6:00pm</strong> <br> Performance: <strong>7:00pm</strong></p>
                                    <!-- <p class="px-4 py-4 text-red-600 my-4 text-xl font-bold">Almost Full - Seats Still Available</p> -->
                                    <!-- <a class="block w-full rounded-md bg-sky-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600" @click="reserve(1)" style="cursor:pointer;">Reserve Tickets</a> -->
                                    <p class="px-4 py-4 text-slate-600 rounded-md my-4 text-xl font-bold">Sold Out!</p>
                                    <button class="block w-full rounded-md bg-slate-600 px-3.5 py-2.5 text-center text-sm font-semibold text-slate-600 shadow-sm  disabled:bg-slate-100" @click="" disabled  style="cursor:pointer">Reserve Tickets</button>
                                </div>
                            </div>
                            <div class="g-block box2 size-33-3">
                                <div class="g-content">
                                    <h3 class="text-2xl text-sky-500">December 10th</h3>
                                    <p style="margin: 0px"><strong>Interpreted for the Deaf!</strong></p>
                                    <p style="margin-top: 0px">Doors open: <strong>5:00pm</strong> <br> Performance: <strong>6:00pm</strong></p>
                                    <!-- <p class="px-4 py-4 text-red-600 my-4 text-xl font-bold">Almost Full - Seats Still Available</p> -->
                                    <!-- <a class="block w-full rounded-md bg-sky-600 px-3.5 py-2.5 text-center text-sm font-semibold text-white shadow-sm hover:bg-sky-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600" @click="reserve(2)" style="cursor:pointer;">Reserve Tickets</a> -->
                                    <p class="px-4 py-4 text-slate-600 rounded-md my-4 text-xl font-bold">Sold Out!</p>
                                    <button class="block w-full rounded-md bg-slate-600 px-3.5 py-2.5 text-center text-sm font-semibold text-slate-600 shadow-sm  disabled:bg-slate-100" @click="" disabled  style="cursor:pointer">Reserve Tickets</button>
                                </div>
                            </div>
                        </div>
                        <div class="ui container" style="padding: 8px !important">
                            <div class="ui message" v-if="activeForm.attendees.length > 0" ref="afterform">
                                You have reserved {{activeForm.attendees.length}} seat<span v-if="activeForm.attendees.length !== 1">s</span>! Add another seat using the form below!
                            </div>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                                <div class="border-sky-200 px-8 py-8 rounded-md border-2" v-for="(attendee, index) in activeForm.attendees" :key="index">
                                    <div class="g-content">
                                        <h3 class="text-2xl text-sky-500">Seat Reserved for: {{ attendee.first }} {{ attendee.last}}</h3>
                                        <p class="my-2">Phone: {{ attendee.phone }}, Address: {{attendee.address}} {{attendee.city}} {{attendee.state}} {{attendee.zip}}</p>
                                        <p v-if="attendee.email">Email: {{ attendee.email}}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="ui message" v-if="activeForm.attendees.length > 0">
                                Add another seat using the form below!
                            </div>
                            <div v-if="showForm" class="ui segment" style="margin-bottom: 25px;" ref="stgform">
                                <h1><span v-if="activeForm.attendees.length == 0">Reserving seats</span><span v-else>Add another</span> for the {{ activeForm.performance.date }} performance:</h1>
                                <div class="ui message" v-if="activeForm.attendees.length === 0">Enter the information for the first person in your group below</div>
                                <div class="ui form">
                                    <div class="fields">
                                        <div class="field" :class="{'error': formErrors.includes('first')}">
                                            <label>First name</label>
                                            <input ref="firstName" type="text" v-model="attendee.first">
                                        </div>
                                        <div class="field" :class="{'error': formErrors.includes('last')}">
                                            <label>Last name</label>
                                            <input type="text" v-model="attendee.last">
                                        </div>
                                        <div class="field" :class="{'error': formErrors.includes('email')}">
                                            <label>Email</label>
                                            <input type="text" v-model="attendee.email">
                                        </div>
                                        <div class="field" :class="{'error': formErrors.includes('phone')}">
                                            <label>Phone</label>
                                            <input type="text" v-model="attendee.phone" maxlength="10">
                                        </div>
                                    </div>
                                    <div class="fields">
                                        <div class="eight wide field" :class="{'error': formErrors.includes('address')}">
                                            <label>Address One</label>
                                            <input type="text" v-model="attendee.address">
                                        </div>
                                    </div>
                                    <div class="fields">
                                        <div class="six wide field" :class="{'error': formErrors.includes('city')}">
                                            <label>City</label>
                                            <input type="text" v-model="attendee.city">
                                        </div>
                                        <div class="two wide field" :class="{'error': formErrors.includes('state')}">
                                            <label>State</label>
                                            <input type="text" v-model="attendee.state">
                                        </div>
                                        <div class=" four wide field" :class="{'error': formErrors.includes('zip')}">
                                            <label>Zip Code</label>
                                            <input type="text" v-model="attendee.zip" maxlength="5">
                                        </div>
                                    </div>
                                    <br>
                                    <div class="ui blue button" @click="addAttendee()">Reserve <span v-if="activeForm.attendees.length > 0">Another</span> Seat <span v-if="attendee.first">for {{attendee.first}} {{ attendee.last}}</span></div>
                                </div>
                                <div class="ui divider"></div>
                                <div class="ui positive message" v-if="activeForm.attendees.length > 0">
                                    After reserving seats for your group, press finalize below to finish the ticketing process for Love's Alive!
                                </div>
                                <div class="ui form" v-if="activeForm.attendees.length > 0">
                                    <div class="fields">
                                        <div class="field">
                                            <label>&nbsp;</label>
                                            <div class="ui checkbox">
                                                <input type="checkbox" name="example" v-model="sendReminder">
                                                <label>Send me a reminder closer to the event!</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="ui green button" @click="finish()" v-if="activeForm.attendees.length > 0">Finalize Registration for {{ activeForm.attendees.length }} Seat<span v-if="activeForm.attendees.length !== 1">s</span> </div>
                            </div>

                            <div class="ui success message" v-if="showSuccess" style="margin-bottom: 25px;" ref="successmsg">
                                <div class="big header">
                                    Congrats!
                                </div>
                                <p class="my-6">Your seats have been reserved. You will get an email confirmation within a few minutes. <strong>The email is your ticket!</strong>. You can either print it out or have it ready on your phone when you arrive for the performance.</p>
                                <p class="my-6">If you didn't receive the email or if you have any questions, please email ds<span style="display:none">asdfasdf</span>@<span style="display:none">asdfasdf</span>myground.org and we will be happy to assist!</p>
                            </div>
                            <div class="ui message" style="margin-bottom: 20px" v-if="showSuccess && !invite">
                                <h3 class="text-2xl text-sky-500">Don't come alone!</h3>
                                <p class="my-6">Invite others to attend our presentation of Christ's gift to the world.</p>
                                <button class="ui blue button" @click="invite = true">Invite a Friend!</button>
                            </div>
                            <div class="ui success message" v-if="friendSuccess">
                                We sent those invitations! Feel free to send others as well!
                            </div>
                            <div class="ui form" v-if="invite">
                                <div class="fields">
                                    <div class="field">
                                        <label>Add email addresses <strong>separated by commas</strong></label>
                                        <textarea name="" id="" cols="30" rows="4" v-model="friends"></textarea>
                                    </div>
                                </div>
                                <div class="ui fields">
                                    <div class="field">
                                        <label>&nbsp;</label>
                                        <button class="ui blue button" :disabled="!friends" @click="sendInvitation">Invite Friends</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    el: '#vue-gift',
    data: function() {
        return {
            showForm: false,
            showSuccess: false,
            sendReminder: true,
            friends: '',
            friendSuccess: false,
            invite: false,
            loading: false,
            activeForm: {
                performance: '',
                attendees: [],

            },
            attendee: this.newAttendee(),
            formErrors: [],
            performances: [{
                    date: 'December 8th, 7:00pm',
                    event_id: 81
                },
                {
                    date: 'December 9th, 7:00pm',
                    event_id: 80
                },
                {
                    date: 'December 10th, 6:00pm',
                    event_id: 82 
                }
            ]
        }
    },
    methods: {
        reserve: function(index) {
            var vm = this
            this.showForm = true
            this.invite = false
            this.activeForm.performance = this.performances[index]
            vm.showSuccess = false
            this.$nextTick(function() {
                this.$refs['stgform'].scrollIntoView({ behavior: 'smooth' });
            })
        },
        newAttendee: function(attendee) {
            attendee = attendee ? attendee : {}
            return {
                event_id: null,
                first: '',
                last: '',
                email: attendee.email ? attendee.email : '',
                address: attendee.address ? attendee.address : '',
                city: attendee.city ? attendee.city : '',
                state: attendee.state ? attendee.state : '',
                zip: attendee.zip ? attendee.zip : '',
                phone: attendee.phone ? attendee.phone : ''
            }
        },
        validate: function() {
            if (!this.attendee.first) {
                this.formErrors.push('first')
            }
            if (!this.attendee.last) {
                this.formErrors.push('last')
            }
            if (!this.attendee.email) {
                this.formErrors.push('email')
            }
            if (!this.attendee.address) {
                this.formErrors.push('address')
            }
            if (!this.attendee.city) {
                this.formErrors.push('city')
            }
            if (!this.attendee.state) {
                this.formErrors.push('state')
            }
            if (!this.attendee.zip) {
                this.formErrors.push('zip')
            }
            if (!this.attendee.phone) {
                this.formErrors.push('phone')
            }
        },
        addAttendee: function() {
            this.formErrors = []
            this.validate()
            if (this.formErrors.length > 0) {
                return
            } else {
                this.activeForm.attendees.push(this.attendee)
                this.attendee = this.newAttendee(this.attendee)
                this.$nextTick(function() {
                    this.$refs['afterform'].scrollIntoView({ behavior: 'smooth' });
                })
            }
        },
        finish: function() {
            var vm = this
            vm.loading = true
            axios.post(`/see_the_gift`, {
                    reservation: vm.activeForm,
                    sendReminder: vm.sendReminder
                })
                .then(function() {
                    vm.activeForm = {
                        performance: '',
                        attendees: [],
                    }
                    vm.showForm = false
                    vm.showSuccess = true
                    vm.$nextTick(function() {
                        this.$refs['successmsg'].scrollIntoView({ behavior: 'smooth' });
                    })
                })
        },
        sendInvitation: function() {
            var vm = this
            vm.loading = true
            axios.post(`/see_the_gift?sendinvite=true`, {
                    friends: vm.friends
                })
                .then(function() {
                    vm.friends = ''
                    vm.friendSuccess = true
                    setTimeout(() => {
                        vm.friendSuccess = false
                    }, 5000);
                })
        }
    }
}
</script>
