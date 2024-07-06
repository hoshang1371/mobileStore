<template>
    <div class="titleUp">
        <h2>سبد خرید</h2>
    </div>
    <div class="order">
        <table>
                <tr>
                    <th>تصویر</th>
                    <th>نام</th>
                    <th>تعداد</th>
                    <th>قیمت هر عدد</th>
                    <th>مجموع</th>
                </tr>
               

                <cart_order
                @remove="removeItem(index)"
                @orderDetail="setorderDetail($event,index)"
                v-for="(orderDetail, index) in orderDetails"
                v-bind:key="orderDetail.id" v-bind:orderDetail="orderDetail"
                />

            </table>
            <div class="update">
                <button @click="sendOrderDetails()">به روز رسانی</button>
            </div>
            <p> کالا در سبد خرید شما &nbsp;<span>{{ persianTotalCount }}</span> </p>
            <div class="product_price_sum">
                <a>جمع محصولات</a>
                <p>تومان &nbsp;<span>{{persianTotalPrice}}</span> </p>
            </div>
            <div>
                <!-- ! اگر ارور داشت غیر فعال شود -->
                <button>ادامه</button>
            </div>
            
    </div>
</template>


<script>
import axios from 'axios'

import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()

import mixin  from "../mixins.js"
import cart_order from '@/components/cart_order.vue'

export default{
    name: 'Cart',
    props: {
        orderDetails: Object,
    },
    data() {
        return {
            number: "۱",
            errors: 0
        }
    },

    mixins: [ mixin ],

    components: {
        cart_order,
    },



    mounted() {

        document.title = "سبد خرید"
        window.scroll(0, 0);
        if(this.orderDetails.length == 0){
            console.log("tohi")
            this.getOrderDetails()
        }
        this.totalPrice = 0
        this.totalCount = 0
        for(let orderDetail in this.orderDetails){
            this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
            this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
        }
        this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
        this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())

    },
    // updated() {
    //     console.log("updated=",this.orderDetails)
    // },

    methods: {

        async getOrderDetails() {
            await axios
                .get('/order/product_order/')
                .then(response => {
                    for(var a in response.data){
                            if (response.data[a].error != ""){
                                ++this.errors;
                            }
                            this.orderDetails[a].error = response.data[a].error
                            this.orderDetails[a].price = response.data[a].price
                            this.orderDetails[a].count = response.data[a].count
                        }
                        console.log(this.orderDetails)
                        for(let orderDetail in this.orderDetails){
                            this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                            this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
                        }
                        this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
                        this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())
                    // this.orderDetails = response.data

                })
                // .catch((err) => {
                //     notify({
                //         title: "مشکلی بوجود امده است",
                //         type: "warn",
                //     });    
                // })
        },
        removeItem(index){
            this.orderDetails.splice(index,1);   
        },
        // ! inja eshtebah ast bayad tamam sabad kharid be roz resani shavad
        async sendOrderDetails() {
            const formData = {
                orderDetails: this.orderDetails

            }
            this.errors =0
            this.$store.commit('setIsLoading', true)
            await axios
                .put('/order/product_orders_details_List_buy/',formData)
                .then(response => {
                    console.log((response.data))
                    if( response.status == 200 ){
                        for(var a in response.data){
                            if (response.data[a].error != ""){
                                ++this.errors;
                            }
                            this.orderDetails[a].error = response.data[a].error
                            this.orderDetails[a].price = response.data[a].price
                            this.orderDetails[a].count = response.data[a].count
                        }

                        if(this.errors==0){
                            notify({
                                    title: "محصول به سبد خرید اضافه شد",
                                    type: "success",
                                });
                        }
                        else{
                            notify({
                            title: "تعداد محصولات صحیح نیست",
                            type: "warn",
                        });   
                        }
                    this.setorderDetail()
                    }
                    else{
                        notify({
                            title: "تعداد صحیح نییست",
                            type: "warn",
                        });    
                    }
                    // else if( response.status == 201 ){
                        
                    //     this.errors = response.data
                    //     console.log(this.errors)
                    // }
                })
                // ! todo: azafe shavad
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
                this.$store.commit('setIsLoading', false)
        },
        setorderDetail(){
                    this.totalPrice = 0
                    this.totalCount = 0
                    for(let orderDetail in this.orderDetails){
                        this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                        this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
                    }
                    this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
                    this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())
        }
    },



}
</script>

<style>
@import "@/assets/css/cart.css"
</style>
