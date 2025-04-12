<template>
    <div id="vue-gift">
        <div class="g-grid">
            <div class="g-block box-red size-100">
                <div class="g-content" style="position: relative;">
                    <h1>Reserve Your Spot!<span class="fa fa-clock-o fa-fw"></span></h1>
                    <div style="background: white;
                    color: #ef4a44;
                    border-radius: 10px;
                    padding: 5px 10px;">Need Help? Call or Text 585-388-0850!</div>
                    <p class="my-6">Due to limited availability, reservations are required for each Walk Through Camelot. Create a reservation below:</p>
                    <!-- <a class="ui red button" href="/static/uploads/see_the_gift_poster.pdf">Download Flyer (PDF)</a> -->
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-8">

            <div class="g-block box1 size-33-3">
                <div class="g-content">
                    <h3 class="text-2xl text-sky-500">Saturday, June 22nd (30 Minute Quest)</h3>
                    <p class="my-6">From: <strong>1:00pm</strong> <br> To: <strong>5:00pm</strong></p>
                    <!-- <p style="color:#011301; padding: 10px; background: rgb(206, 192, 22); border-radius: 10px;">Going fast!</p> -->
                    <button class="block w-full rounded-md bg-slate-600 px-3.5 py-2.5 text-center text-sm font-semibold text-slate-100 shadow-sm  disabled:bg-slate-100" @click="reserve(0)" style="cursor:pointer">Reserve Tickets</button>
                </div>
            </div>
            <div class="g-block box1 size-33-3">
                <div class="g-content">
                    <h3 class="text-2xl text-sky-500">Sunday, June 23rd  (30 Minute Quest)</h3>
                    <p class="my-6">From: <strong>1:00pm</strong> <br> To: <strong>5:00pm</strong></p>
                    <!-- <p style="color:#011301; padding: 10px; background: #16ce16; border-radius: 10px;">Spots still available</p> -->
                    <button class="block w-full rounded-md bg-slate-600 px-3.5 py-2.5 text-center text-sm font-semibold text-slate-100 shadow-sm  disabled:bg-slate-100" @click="reserve(1)" style="cursor:pointer">Reserve Tickets</button>
                </div>
            </div>
        </div>
        <div class="ui container" style="padding: 8px !important">
            <div class="ui message" v-if="activeForm.attendees.length > 0" ref="afterform">
                You have reserved {{activeForm.attendees.length}} spot<span v-if="activeForm.attendees.length !== 1">s</span>! Add another spot using the form below!
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-8">
                <div class="bg-sky-100 p-3 rounded-lg" v-for="(attendee, index) in activeForm.attendees" :key="index">
                    <div class="g-content">
                        <h3 class="text-2xl text-sky-500">Spot Reserved for: {{ attendee.first }} {{ attendee.last}} (Finalize Below!)</h3>
                        <p class="my-6">Phone: {{ attendee.phone }}, Address: {{attendee.address}} {{attendee.city}} {{attendee.state}} {{attendee.zip}}</p>
                        <p v-if="attendee.email">Email: {{ attendee.email}}</p>
                    </div>
                </div>
            </div>
            <div class="ui message" v-if="activeForm.attendees.length > 0">
                Add another spot using the form below!
            </div>
            <div v-if="showForm" class="ui segment" style="margin-bottom: 25px;" ref="stgform">
                <h1><span v-if="activeForm.attendees.length == 0">Reserving spots</span><span v-else>Add another</span> for the {{ activeForm.performance.date }} quest:</h1>
                <div class="ui message" v-if="activeForm.attendees.length === 0">Enter the information for the first person in your group below</div>
                <div class="ui message">
                    <h3 class="ui header">What time will your group arrive?</h3>
                    <div class="ui form">
                        <div class="ui fields">
                            <div class="ui field" :class="{'error': formErrors.includes('time')}">
                                <select name="" id="" v-model="attendee.time" style="    margin-bottom: 0px; appearance: auto;
                                margin-top: 10px;">
                                    <option value=""></option>
                                    <option :value="time" v-for="time in activeForm.performance.times">{{time}} (Still Available)</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
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
                    <div class="ui blue button" @click="addAttendee()">Reserve <span v-if="activeForm.attendees.length > 0">Another</span> Spot <span v-if="attendee.first">for {{attendee.first}} {{ attendee.last}}</span></div>
                </div>
                <div class="ui divider"></div>
                <div class="ui positive message" v-if="activeForm.attendees.length > 0">
                    After reserving spots for your group, press finalize below to finish the ticketing process for your Walk Through Camelot!
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
                <div class="ui green button" :class="{'loading': loading}" @click="finish()" v-if="activeForm.attendees.length > 0">Finalize Registration for {{ activeForm.attendees.length }} Spot<span v-if="activeForm.attendees.length !== 1">s</span> </div>
            </div>

            <div class="ui success message" v-if="showSuccess" style="margin-bottom: 25px;" ref="successmsg">
                <div class="big header">
                    Congrats!
                </div>
                <p class="my-6">Your spots have been reserved. You will get an email confirmation within a few minutes. <strong>The email is your ticket!</strong>. You can either print it out or have it ready on your phone when you arrive for the quest.</p>
                <p class="my-6">If you didn't receive the email or if you have any questions, please email ds<span style="display:none">asdfasdf</span>@<span style="display:none">asdfasdf</span>myground.org and we will be happy to assist!</p>
            </div>
            <div class="ui message" style="margin-bottom: 20px" v-if="showSuccess && !invite">
                <h3 class="text-2xl text-sky-500">Don't come alone!</h3>
                <p class="my-6">Invite others to attend our presentation of the Search for the Holy Book.</p>
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
                        <button class="ui blue button" :class="{'loading': loading}" :disabled="!friends" @click="sendInvitation">Invite Friends</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
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
                    date: 'Saturday, June 22nd',
                    times: [
                    ]
                },
                {
                    date: 'Sunday, June 23rd',
                    times: [
                        '3:00 PM',
                        '4:00 PM',
                    ]
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
                first: '',
                last: '',
                email: attendee.email ? attendee.email : '',
                address: attendee.address ? attendee.address : '',
                city: attendee.city ? attendee.city : '',
                state: attendee.state ? attendee.state : '',
                zip: attendee.zip ? attendee.zip : '',
                phone: attendee.phone ? attendee.phone : '',
                time: attendee.time ? attendee.time : ''
            }
        },
        validate: function() {
            if (!this.attendee.first) {
                this.formErrors.push('first')
            }
            if (!this.attendee.time) {
                this.formErrors.push('time')
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
            axios.post(`/camelot`, {
                    reservation: vm.activeForm,
                    sendReminder: vm.sendReminder
                })
                .then(function() {
                    vm.activeForm = {
                        performance: '',
                        attendees: [],
                    }
                    vm.loading = false
                    vm.showForm = false
                    vm.showSuccess = true
                    vm.$nextTick(function() {
                        this.$refs['successmsg'].scrollIntoView({ behavior: 'smooth' });
                    })
                }).catch(function (error) {
                    vm.loading = false
                })
        },
        sendInvitation: function() {
            var vm = this
            vm.loading = true
            axios.post(`/camelot?sendinvite=true`, {
                    friends: vm.friends
                })
                .then(function() {
                    vm.friends = ''
                    vm.friendSuccess = true
                    vm.loading = false
                    setTimeout(() => {
                        vm.friendSuccess = false
                    }, 5000);
                }).catch(function (error) {
                    vm.loading = false
                })
        }
    }
}
</script>

