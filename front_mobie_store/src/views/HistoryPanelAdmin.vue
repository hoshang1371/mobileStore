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
                    console.log(this.historyOrder)
                    console.log(this.historyOrder[0].PostAddressDetail[0].confirmedPayment)
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
    },
}
</script>

<style>
@import "@/assets/css/HistoryPanelAdmin.css";
</style>