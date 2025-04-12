<template>
    <div class="min-h-full">
        <div class="py-10">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div id="quick-books">
                    <Button backgroundColor="slate" textColor="white" class="mt-2" @click="update">Update</Button>
                    <Button backgroundColor="slate" textColor="white" class="mt-2" @click="downloadCsv">CSV Download</Button>
                    <div class="ui labeled input" id="startDate" style="margin-right: 20px">
                        <div class="ui label">Start Date</div>
                        <input type="date" v-model="reportStart" class="ui input" id="endDate">
                    </div>
                    <div class="ui labeled input" id="endDate" style="margin-right: 20px">
                        <div class="ui label">End Date</div>
                        <input type="date" v-model="reportEnd" class="ui input" id="endDate">
                    </div>
                    <div class="ui toggle checkbox">
                        <input type="checkbox" v-model="onlyFaithfulSteward">
                        <label>Only Faithful Steward</label>
                    </div>
                    <div class="ui toggle checkbox">
                        <input type="checkbox" v-model="onlyUncheckedFaithfulSteward">
                        <label>Faithful Steward NOT Checked</label>
                    </div>
                    <Table>
                        <template v-slot:header>
                            <tr>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Payout Arrival</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Payout ID</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx ID</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Created</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Desc</th>
                                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Meta</th>
                                <th style="text-align:right" scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Amount</th>
                                <th style="text-align:right" scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Fee</th>
                                <th style="text-align:right" scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Tx Net</th>
                            </tr>
                        </template>
                        <template v-slot:body>
                            <tr v-for="(result, index) in results" :class="{'positive': result['tx_description'] == 'STRIPE PAYOUT'}">
                                <td class=" px-3 py-4 text-sm text-gray-500">{{ formatDate(result['payout_arrival_date']) }}</td>
                                <!-- <td>{{ result['payout_description'] }}</td> -->
                                <!-- <td>{{ result['payout_status'] }}</td> -->
                                <td class=" px-3 py-4 text-sm text-gray-500">{{ result['payout_id'].slice(-5) }}</td>
                                <td class=" px-3 py-4 text-sm text-gray-500">{{ result['tx_id'].slice(-5) }}</td>
                                <td class=" px-3 py-4 text-sm text-gray-500">{{ formatDate(result['tx_created']) }}</td>
                                <td class=" px-3 py-4 text-sm text-gray-500">{{ result['tx_description'] }}</td>
                                <td class=" px-3 py-4 text-sm text-gray-500">
                                    <ul class="mt-3 grid grid-cols-1 gap-5" style="min-width: 130px" v-if="!isEmpty(result['tx_meta']) && result['tx_meta']['faithful_steward']">
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['tithe'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Tithe</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['tithe']).toFixed(2) }} (${{(result['tx_meta']['tithe'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['missions'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Missions</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['missions']).toFixed(2) }} (${{(result['tx_meta']['missions'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['alms'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Alms</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['alms']).toFixed(2) }} (${{(result['tx_meta']['alms'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['building'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Building</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['building']).toFixed(2) }} (${{(result['tx_meta']['building'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['special_speaker'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Speaker</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['special_speaker']).toFixed(2) }} (${{(result['tx_meta']['special_speaker'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['other'] != '0.00'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Other</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['other']).toFixed(2) }} (${{(result['tx_meta']['other'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                    <br>{{ result['tx_meta']['other_desc'] }}
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta'] && result['tx_meta']['final_tip'] != '0.00' && result['tx_meta']['final_tip'] !== undefined">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Tip</a>
                                                <p class="text-gray-500">
                                                    ${{ parseFloat(result['tx_meta']['final_tip']).toFixed(2) }} (${{(result['tx_meta']['final_tip'] / result['tx_amount'] * result['tx_fee']).toFixed(2)}})
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_meta']">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Faithful Steward</a>
                                                <p class="text-gray-500">
                                                    <i class="fa fa-check" style="cursor:pointer; color:green" @click="toggleFaithfulSteward(index)" v-if="result['tx_meta']['faithful_steward'] == 1"></i>
                                                    <i class="fa fa-close" style="cursor:pointer; color:red" @click="toggleFaithfulSteward(index)" v-else></i>
                                                </p>
                                            </div>
                                        </div>
                                        <div class="col-span-1 flex rounded-md shadow-sm" v-if="result['tx_description'] != 'STRIPE PAYOUT'">
                                            <div class="flex-1 truncate px-4 py-2 text-sm">
                                                <a href="#" class="font-medium text-gray-900 hover:text-gray-600">Quick Books</a>
                                                <p class="text-gray-500">
                                                    <i class="fa fa-check" style="cursor:pointer; color:green" @click="toggleQuickBooks(index)" v-if="result['tx_meta']['quick_books'] == 1"></i>
                                                    <i class="fa fa-close" style="cursor:pointer; color:red" @click="toggleQuickBooks(index)" v-else></i>
                                                </p>
                                            </div>
                                        </div>
                                    </ul>
                                </td>
                                <td style="text-align:right" class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">${{ result['tx_amount'].toFixed(2) }}</td>
                                <td style="text-align:right" class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">${{ result['tx_fee'].toFixed(2) }}</td>
                                <td style="text-align:right" class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">${{ result['tx_net'].toFixed(2) }}</td>
                            </tr>
                        </template>
                    </Table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Table from '@/components/utility/Table.vue'
import Button from '@/components/utility/Button.vue'
import axios from 'axios'
import dayjs from 'dayjs'
import Papa from 'papaparse'

export default {
    name: 'QuickBooks',
    data: function() {
        return {
            loading: false,
            results: [],
            reportStart: dayjs().subtract(7, 'day').format('YYYY-MM-DD'),
            reportEnd: dayjs().format('YYYY-MM-DD'),
            onlyFaithfulSteward: false,
            onlyUncheckedFaithfulSteward: false,
        }
    },
    components: {
        Table,
        Button
    },
    watch: {
        onlyFaithfulSteward() {
            this.update()
        },
        onlyUncheckedFaithfulSteward() {
            this.update()
        },
        reportEnd() {
            this.update()
        },
        reportStart() {
            this.update()
        }
    },
    methods: {
        isEmpty(obj) {
            return Object.keys(obj).length === 0
        },
        update() {
            var vm = this
            vm.loading = true
            axios.post(`/church/admin/quick-books`, {
                startDate: vm.reportStart,
                endDate: vm.reportEnd,
                onlyFaithfulSteward: vm.onlyFaithfulSteward,
                onlyUncheckedFaithfulSteward: vm.onlyUncheckedFaithfulSteward
            }).then(function(response) {
                    console.log(response.data)
                    vm.results = response.data.results
                    vm.loading = false
                }).catch(function(error) {
                    vm.loading = false
                })
        },
        toggleFaithfulSteward(index) {
            var vm = this
            let charge = vm.results[index].source_id
            axios.post(`/church/admin/quick-books`, {
                faithfulSteward: charge
            }).then(function(response) {
                    console.log(response.data)
                    vm.results[index].tx_meta.faithful_steward = response.data.faithful_steward
                }).catch(function(error) {})
        },
        toggleQuickBooks(index) {
            var vm = this
            let charge = vm.results[index].source_id
            axios.post(`/church/admin/quick-books`, {
                quickBooks: charge
            }).then(function(response) {
                    console.log(response.data)
                    vm.results[index].tx_meta.quick_books = response.data.quick_books
                }).catch(function(error) {})
        },
        downloadCsv() {
            var vm = this
            let data = vm.results.map(element => ({
                payout_arrival: element.payout_arrival_date,
                payout_description: element.payout_description,
                payout_status: element.payout_status,
                payout_id: element.payout_id,
                tx_id: element.tx_id,
                tx_created: element.tx_created,
                tx_desc: element.tx_description,
                tx_meta: JSON.stringify(element.tx_meta),
                tx_faithful_steward: element.tx_meta ? element.tx_meta.faithful_steward : '',
                tx_alms: element.tx_meta && element.tx_meta.alms != '0.00' ? element.tx_meta.alms : '',
                tx_building: element.tx_meta && element.tx_meta.building != '0.00' ? element.tx_meta.building : '',
                tx_missions: element.tx_meta && element.tx_meta.missions != '0.00' ? element.tx_meta.missions : '',
                tx_other: element.tx_meta && element.tx_meta.other != '0.00' ? element.tx_meta.other : '',
                tx_special_speaker: element.tx_meta && element.tx_meta.special_speaker != '0.00' ? element.tx_meta.special_speaker : '',
                tx_tithe: element.tx_meta && element.tx_meta.tithe != '0.00' ? element.tx_meta.tithe : '',
                tx_amount: element.tx_amount,
                tx_fee: element.tx_fee,
                tx_net: element.tx_net,
            }))
            var csv = Papa.unparse(data)
            var csvData = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            var csvURL = null;
            csvURL = window.URL.createObjectURL(csvData)
            var tempLink = document.createElement('a')
            tempLink.href = csvURL
            tempLink.setAttribute('download', 'download.csv')
            tempLink.click()
        },
        formatDate(date, fmt) {
            return dayjs(date).format(fmt ? fmt : 'MM/DD/YYYY hh:mm A')
        }
    },
    mounted() {
        this.update()
    },
}
</script>
<style scoped>
.positive {
    background: #e8ffe8;
}
</style>
