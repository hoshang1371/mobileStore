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
                v-for="(orderDetail, index) in orderDetails"
                v-bind:key="orderDetail.id" v-bind:orderDetail="orderDetail"
                />
            </table>

            
    </div>
</template>


<script>
import axios from 'axios'


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

        }
    },

    mixins: [ mixin ],

    components: {
        cart_order,
    },



    mounted() {
        document.title = "سبد خرید"
        window.scroll(0, 0);
    },
    methods: {
        
        removeItem(index){
            console.log(index)
            this.orderDetails.splice(index,1);   


            // this.totalCount = 0
            // this.totalPrice = 0
            // for(let orderDetail in this.orderDetails){
            //             this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
            //             this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
            //         }
            //         this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
            //         this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())

        },
    },



}
</script>

<style>
@import "@/assets/css/cart.css"
</style>
