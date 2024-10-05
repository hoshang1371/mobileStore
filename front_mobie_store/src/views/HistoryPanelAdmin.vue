<template>
    <div>
        <div class="content">
            <panelAdminRight/>

            <div class="container_left">
                <table>
                    <tr>
                        <th>مرجع سفارش</th>
                        <th>تاریخ</th>
                        <th>جمع قیمت</th>
                        <th>روش پرداخت</th>
                        <th>وضعیت</th>
                        <th>شماره پیگیری</th>
                        <th>عملیات</th>
                    </tr>
                    <tr v-for="hisOrd in historyOrder" :key="historyOrder.id">
                        <td>
                            <!-- <a>{{(hisOrd.id)}}</a> -->
                            <a>{{toPersinaDigit(hisOrd.id.toString())}}</a>
                            <!-- <a>{{toPersinaDigit("10")}}</a> -->
                        </td>
                        <td>
                            <!-- <a>{{hisOrd.j_create_date}}</a> -->
                            <a>{{spliteDate(hisOrd.j_create_date)}}</a>
                        </td>
                        <td>
                            <a>{{toPersinaDigit(hisOrd.get_All_detail_sum.toString())}}</a>
                        </td>
                        <td>
                            <a v-if="hisOrd.PaymentMethode[0]!=undefined">{{hisOrd.PaymentMethode[0].PaymentDetails}}</a>
                        </td>
                        <td>
                            <!-- <a v-if="hisOrd.PostAddressDetail[0].confirmedPayment != null">{{hisOrd.PostAddressDetail}}</a> -->
                            <a 
                                v-if="(hisOrd.PostAddressDetail[0]!=undefined) &&
                                (hisOrd.PostAddressDetail[0].confirmedPayment != null) &&
                                (hisOrd.PostAddressDetail[0].collected == null)"
                              >در حال پردازش</a>
                            <a 
                                v-if="(hisOrd.PostAddressDetail[0]!=undefined) &&
                                (hisOrd.PostAddressDetail[0].collected != null) &&
                                (hisOrd.PostAddressDetail[0].carried == null)
                                "
                             >در حال جمع اوری</a>
                            <a 
                                v-if="(hisOrd.PostAddressDetail[0]!=undefined) &&
                                (hisOrd.PostAddressDetail[0].collected != null) &&
                                (hisOrd.PostAddressDetail[0].carried != null)"
                             > حمل شده </a>
                        </td>
                        <td>
                            <a v-if="hisOrd.PaymentMethode[0]!=undefined">{{toPersinaDigit(hisOrd.PaymentMethode[0].peymentCode.toString())}}</a>
                        </td>
                        <td>
                            <a @click="goToPdfView(hisOrd.orderDetails[0].id)">صورت حساب</a>
                            <svg @click="goToPdfView(hisOrd.orderDetails[0].id)" height="20px" width="20px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
	                            viewBox="0 0 370.32 370.32" xml:space="preserve">
                                <g>
                                    <path style="fill:#020202;" d="M148.879,85.993H95.135c-8.284,0-15,6.716-15,15c0,8.284,6.716,15,15,15h53.744
                                        c8.284,0,15-6.716,15-15C163.879,92.709,157.163,85.993,148.879,85.993z"/>
                                    <path style="fill:#020202;" d="M148.879,148.327H95.135c-8.284,0-15,6.716-15,15c0,8.284,6.716,15,15,15h53.744
                                        c8.284,0,15-6.716,15-15C163.879,155.043,157.163,148.327,148.879,148.327z"/>
                                    <path style="fill:#020202;" d="M211.944,253.354v14.608h7.717c9.359,0,9.359-5.599,9.359-7.439c0-1.775,0-7.17-9.359-7.17H211.944z
                                        "/>
                                    <path style="fill:#020202;" d="M325.879,225.752h-24.41V73.703c0-3.934-1.56-7.705-4.344-10.484l-58.876-58.88
                                        C235.465,1.561,231.699,0,227.765,0H50.58C34.527,0,21.469,13.059,21.469,29.112v312.095c0,16.054,13.059,29.113,29.111,29.113
                                        h221.777c16.052,0,29.111-13.06,29.111-29.113v-30.048h24.41c12.687,0,22.973-10.285,22.973-22.973v-39.462
                                        C348.852,236.038,338.566,225.752,325.879,225.752z M269.855,337.906H53.082V32.414H207.17V75.99
                                        c0,10.555,8.554,19.107,19.105,19.107h43.58v130.655h-74.178c-12.688,0-22.973,10.286-22.973,22.973v39.462
                                        c0,12.688,10.285,22.973,22.973,22.973h74.178V337.906z M238.51,260.523c0,10.441-7.224,16.928-18.85,16.928h-7.717v8.977
                                        c0,2.316-1.877,4.197-4.195,4.197h-1.097c-2.319,0-4.197-1.881-4.197-4.197v-38.366c0-2.316,1.878-4.197,4.197-4.197h13.009
                                        C231.287,243.864,238.51,250.246,238.51,260.523z M262.305,290.625H247.21c-2.319,0-4.197-1.881-4.197-4.197v-38.366
                                        c0-2.316,1.877-4.197,4.197-4.197h15.095c13.148,0,23.845,10.5,23.845,23.409C286.15,280.15,275.454,290.625,262.305,290.625z
                                        M322.455,249.156c0,2.32-1.878,4.197-4.197,4.197h-17.045v10.053h14.521c2.317,0,4.197,1.875,4.197,4.195v1.099
                                        c0,2.316-1.88,4.197-4.197,4.197h-14.521v13.53c0,2.316-1.877,4.197-4.196,4.197h-1.096c-2.32,0-4.197-1.881-4.197-4.197v-38.366
                                        c0-2.316,1.877-4.197,4.197-4.197h22.337c2.319,0,4.197,1.881,4.197,4.197V249.156z"/>
                                    <path style="fill:#020202;" d="M262.305,253.354h-9.803v27.782h9.803c7.915,0,14.355-6.222,14.355-13.862
                                        C276.661,259.598,270.221,253.354,262.305,253.354z"/>
                                </g>
                            </svg>
                        </td>
                    </tr>
    
            </table>
            </div>
        </div>
    </div>
</template>

<script>
import panelAdminRight from '@/components/panelAdminRight.vue'
import mixin  from "../mixins.js"

import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";
import productListBox from '@/components/productListBox.vue'
import ProductBox from '@/components/productBox.vue'

const { notify } = useNotification()
export default{
    name:"HistoryPanelAdmin",
    mixins: [ mixin ],
    components:{
        panelAdminRight,    
    },
    data() {
        return {
            historyOrder : [],
            statusOrder : [],
        }
    },
    mounted() {
        document.title = ' تاریخچه سفارشات ' + ' | موبایل'
        window.scroll(0, 0);
        this.getHistoryPanelAdmin();
    },
    methods: {
        async getHistoryPanelAdmin() {
            axios
                .get("/order/All_product_order/")
                .then(response => {
                    this.$store.commit('setIsLoading', true)
                    this.historyOrder = response.data
                    // console.log(this.historyOrder)
                    // console.log(this.historyOrder[0].PostAddressDetail[0].confirmedPayment)
                    // console.log(typeof(this.historyOrder[0].PaymentMethode[0]))
                    // if(response.status == 200){
                    //     notify({
                    //     title: " رمز عبور تغییر کرد ",
                    //     type: "success",
                    //     });
                    // }
                    this.$store.commit('setIsLoading', false)   
                })
        },
        spliteDate(date){
            return (this.toPersinaDigit(date.split("T")[0])).replaceAll("-", "/")
        },
        goToPdfView(id){
            console.log(id);
            this.$router.push(`/peymentPdf/${id}`)
        }
    },
}
</script>

<style>
@import "@/assets/css/HistoryPanelAdmin.css";
</style>