<template>
<div class="table fac">
    <h3>صورتحساب</h3>
    <table >
        <tr>
            <th><a>نام کالا</a></th>
            <th><a>تعداد</a></th>
            <th><a>قیمت واحد</a></th>
            <th><a>جمع قیمت</a></th>
        </tr>
        <tr v-for="peyment in peyments" :key="peyment.id">
                <td class="nameKala">
                    <div>
                        <img :src="peyment.product.get_thumbnail" alt="">
                        <a> کد کالا:<span>{{toPersinaDigit(peyment.product.code.toString())}}</span> </a>
                    </div>
                    <a>{{ peyment.product.title }}</a>
                </td>
                <td>
                    <div>
                        <a>{{toPersinaDigit(peyment.count.toString())}}</a>
                    </div>
                </td>
                <td>
                    <div>
                        <a :class="{
                            'product__price_kh': peyment.product.priceOff != null,
                        }">
                        <span>{{toPersinaDigit(peyment.product.price.toString())}}</span>تومان</a>
                        <a v-if="peyment.product.priceOff != null"><span>{{toPersinaDigit(peyment.product.priceOff.toString())}}</span>تومان</a>
                    </div>
                </td>
                <td>
                    <div>
                        <a>
                            <span>
                                {{toPersinaDigit(peyment.price.toString())}}
                            </span>
                            تومان
                        </a>
                    </div>
                </td>
        </tr>

        <tr class="total_price">
            <td><h3>مجموع قیمت کالا</h3></td>
            <td></td>
            <td></td>
            <td>
                <h3>
                    <span>
                        {{ toPersinaDigit(totalPrice) }}
                    </span>
                    تومان
                </h3>
            </td>
        </tr>
        <tr class="total_price">
            <td><h3>حمل‌و‌نقل</h3></td>
            <td></td>
            <td></td>
            <td>
                <h3>
                    <span>
                        {{ toPersinaDigit(postPrice.toString()) }}
                    </span>
                    تومان
                </h3>
            </td>
        </tr>
        <tr class="total_price">
            <td><h3>جمع کل</h3></td>
            <td></td>
            <td></td>
            <td>
                <h3>
                    <span>
                        {{ toPersinaDigit(totalPriceAddpostPrice) }}
                    </span>
                    تومان
                </h3>
            </td>
        </tr>

    </table>
</div>

<div class="butt" @click="downloadFactorPdf()">
    <button>دانلود فاکتور</button>
</div>

<div class="table">
    <h3>جزئیات حامل‌ها</h3>
    <table>
        <tr>
            <th><a>تاریخ</a></th>
            <th><a>حامل</a></th>
            <th><a>هزينه ارسال</a></th>
            <th><a>شماره پیگیری</a></th>
        </tr>
        <tr>
            <td>
                <div>
                    <a>{{carryDate}}</a>
                </div>
            </td>
            <td>
                <div>
                    <a>{{carryTitle}}</a>
                </div>
            </td>
            <td>
                <div>
                    <a>{{toPersinaDigit(carryPrice.toString())}}</a>
                </div>
            </td>
            <td>
                <div>
                    <a>{{toPersinaDigit(carryTrackingNumber)}}</a>
                </div>
            </td>
        </tr>
    </table>
</div>

<div class="table">
    <h3>
        جزئیات پرداخت‌ها
    </h3>
    <table>
        <!-- toPersinaDigit(this.peymentDetails[0].peymentDate.split('T')[0]) -->
        <tr>
            <th><a>تاریخ</a></th>
            <th><a>روش پرداخت</a></th>
            <th><a>	شماره تراکنش</a></th>
            <th><a>مبلغ</a></th>
        </tr>
        <tr>
            <td>
                <div>
                    <a>
                        {{peymentDetailsDate}}
                    </a>
                </div>
            </td>
            <td>
                <div>
                    <a>
                        {{PaymentDetails}}
                    </a>
                </div>
            </td>
            <td>
                <div>
                    <a>
                        {{ toPersinaDigit(peymentCode) }}
                    </a>
                </div>
            </td>
            <td>
                <h3>
                    <span>
                        {{ toPersinaDigit(totalPriceAddpostPrice) }}
                    </span>
                    تومان
                </h3>
            </td>
        </tr>
    </table>
</div>

<div class="table">
    <h3>
        تحویل به نشانی    
    </h3>
    <table>
        <tr>
            <th><a>نشانی من</a></th>
        </tr>
        <tr>
            <td>
                <div>
                    <a>
                        {{ addressSelected.address }}
                    </a>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <div>
                    <a>
                        <span>کد پستی :</span>
                        {{ addressSelected.post_code }}
                    </a>
                </div>
            </td>
        </tr>
    </table>
</div>
</template>


<script>
// import { VueHtml2pdf } from 'vue-html2pdf' carried
// import { VueHtml2pdf } from "@kyvg/vue-html2pdf";
import Vue3Html2pdf from 'vue3-html2pdf'
import html2pdf from 'html2pdf.js'

import mixin  from "../mixins.js"

import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";

export default{
    name: "peymentPdf",
    mixins: [ mixin ],

    data() {
        return {
            peyments: [],         
            CarrierDetails: [],
            peymentDetails: [],
            totalPrice: "",
            postPrice: "",
            totalPriceAddpostPrice: "",
            carryDate: "",
            carryTitle: "",
            carryPrice: "",
            carryTrackingNumber: "",
            peymentDetailsDate: "",
            PaymentDetails: "",
            peymentCode: "",
            addressSelected: "",
        }
    },
    components: {
        Vue3Html2pdf
    },
    mounted() {
        document.title = ' صورت حساب ' + ' | موبایل'
        window.scroll(0, 0);
        this.getOrderPeyment();
        // this.getpostprice();

        // const product_id = this.$route.params.product_id
        // console.log(this.$route.params.peyment_id)
        // console.log(document.querySelector('.kkkkkkkk'))
        // console.log(peyment_id)
        // html2pdf((document.querySelector('.kkkkkkkk')),{
        //     margin :1,
        //     filename :'h.pdf',
        // })

        
        // this.getHistoryPanelAdmin();
        // this.generateReport();
    },
    methods: { 
        generateReport () {
            this.$refs.html2Pdf.generatePdf()
        },
        async getOrderPeyment() {
            const peyment_id = this.$route.params.peyment_id
            axios
                .get(`/order/product_order_by_id/${peyment_id}/`)
                .then(response => {
                    this.$store.commit('setIsLoading', true)
                    this.peyments = response.data
                    // console.log(this.peyments)
                    var total=0;
                    for(let pri in this.peyments){
                        total=total+parseInt(this.peyments[pri].price)
                    }
                    this.totalPrice=total.toString();
                    this.getpostprice();
                    this.$store.commit('setIsLoading', false)   
                })
        },

        async getpostprice() {
            const peyment_id = this.$route.params.peyment_id
            axios
                .get(`/post_information/PostAddressDetail_selected/${peyment_id}/`)
                .then(response => {
                    this.$store.commit('setIsLoading', true)
                    // console.log(response.data.price)
                    this.postPrice = response.data.price;
                    this.totalPriceAddpostPrice = (parseInt(this.postPrice)+parseInt(this.totalPrice)).toString()
                    // console.log(this.totalPriceAddpostPrice)
                    this.$store.commit('setIsLoading', false);
                    this.getCarrierDetails(); 
                })
        },
        async getCarrierDetails() {
            const peyment_id = this.$route.params.peyment_id
            axios
                .get(`/post_information/PostAddressDetail_peyment/${peyment_id}/`)
                .then(response => {
                    this.$store.commit('setIsLoading', true); 
                    // console.log(response.data);
                    this.CarrierDetails =response.data;
                    // console.log((this.CarrierDetails[0].addressSelected))
                    // 
                    this.addressSelected = this.CarrierDetails[0].addressSelected
                    // console.log(this.addressSelected.address)
                    this.carryTrackingNumber = this.CarrierDetails[0].trackingNumber
                    this.carryPrice = this.CarrierDetails[0].PostPriceSelected.price
                    this.carryTitle = this.CarrierDetails[0].PostPriceSelected.title
                    this.carryDate  = this.toPersinaDigit(this.CarrierDetails[0].carried.split("T")[0])
                    this.$store.commit('setIsLoading', false);
                    this.getpeymentDetails();
                })
        },
        async getpeymentDetails() {
            const peyment_id = this.$route.params.peyment_id
            axios
                .get(`/post_information/PaymentMethodeDetail_peyment/${peyment_id}/`)
                .then(response => {
                    this.$store.commit('setIsLoading', true); 
                    // console.log(response.data);
                    this.peymentDetails = response.data
                    // console.log((this.peymentDetails[0].peymentDate.split('T'))) 
                    // console.log(typeof(this.peymentDetails[0].peymentDate.split('T')))
                    this.peymentDetailsDate = this.toPersinaDigit(this.peymentDetails[0].peymentDate.split('T')[0])
                    this.PaymentDetails = this.peymentDetails[0].PaymentDetails
                    this.peymentCode = this.peymentDetails[0].peymentCode
                    // console.log(this.peymentDetails[0].PaymentDetails)
                    this.$store.commit('setIsLoading', false);
                })
        },
        downloadFactorPdf(){
            const peyment_id = this.$route.params.peyment_id
            html2pdf((document.querySelector('.fac')),{
            margin :1,
            filename :`${peyment_id}.pdf`,
        })
        }

},
}
</script>

<style>
@import "@/assets/css/peymentPdf.css";
</style>