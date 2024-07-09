<template>
    <tr>
        <td><img :src="orderDetail.product.get_thumbnail" alt=""></td>
        <td>
            <div>
                <a href="">{{ orderDetail.product.title }}</a>
                <span class="error" v-if="orderDetail.error != ''"><p>{{orderDetail.error}}</p></span>
                <span v-else></span>
            </div>
        </td>
        
        <td style="
        display: flex;
        justify-content: center;
        align-items: center;
        ">
            <div class="number">
                <input 
                type="text" id="numberProduct" 
                name="first_name" class="toPe" 
                @keyup="
                KeyUpFunction($event);
                conectToOrderDetails($event);
                " 
                @keyup.enter="sendToOrderDetails()"
                v-model="number"
                >
                <a class="up">
                    <div class='BCup' 
                    @click="
                        BCupClick(); 
                        sendToOrderDetails();
                        " 
                    >+</div>
                    <div class='BCdown' 
                    @click="
                        BCdownClick(); 
                        sendToOrderDetails();
                    " 
                    >-</div>
                </a>
            </div>

            <div class="orderDetail_remove">
                <svg 
                @click="removeThisItem(orderDetail.id)"
                xmlns="http://www.w3.org/2000/svg" id="delete" x="0" y="0" version="1.1" viewBox="0 0 29 29" xml:space="preserve">
                    <path d="M19.795 27H9.205a2.99 2.99 0 0 1-2.985-2.702L4.505 7.099A.998.998 0 0 1 5.5 6h18a1 1 0 0 1 .995 1.099L22.78 24.297A2.991 2.991 0 0 1 19.795 27zM6.604 8 8.21 24.099a.998.998 0 0 0 .995.901h10.59a.998.998 0 0 0 .995-.901L22.396 8H6.604z"></path><path d="M26 8H3a1 1 0 1 1 0-2h23a1 1 0 1 1 0 2zM14.5 23a1 1 0 0 1-1-1V11a1 1 0 1 1 2 0v11a1 1 0 0 1-1 1zM10.999 23a1 1 0 0 1-.995-.91l-1-11a1 1 0 0 1 .905-1.086 1.003 1.003 0 0 1 1.087.906l1 11a1 1 0 0 1-.997 1.09zM18.001 23a1 1 0 0 1-.997-1.09l1-11c.051-.55.531-.946 1.087-.906a1 1 0 0 1 .905 1.086l-1 11a1 1 0 0 1-.995.91z"></path><path d="M19 8h-9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1zm-8-2h7V4h-7v2z"></path>
                </svg>
            </div>
        </td>

        <td>
            <!-- !takhfif lahaz shavad -->
            <p :class="{
                'product__price_kh': orderDetail.product.priceOff != null,
            }"
            style="margin-top: auto;"
            >
            {{ orderDetail.product.price }} تومان</p>
            <h3 v-if="orderDetail.product.priceOff != null">تخفیف</h3>
            <h4 v-if="orderDetail.product.priceOff != null">{{ orderDetail.product.priceOff }} تومان</h4>
        </td>

        <td>
            <p>{{ price }} تومان</p>
        </td>
    </tr>
</template>



<script>

import mixin  from "../mixins.js"
import axios from 'axios';

import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()
import useComp from '../compositionMixin.js'
import { ref,watch,getCurrentInstance  } from 'vue';

export default {
    name: 'cart_order',
    props: {
        orderDetail: Object,
    },
    mixins: [ mixin ],
    data() {
        return {
            number: "۱",
            price: "۱"
        }
    },
    mounted() {
        this.number = this.toPersinaDigit((parseInt(this.orderDetail.count)).toString())
        this.price = (this.toPersinaDigit(parseInt(this.orderDetail.price).toString()));
    },
    setup(props) {
        const {toPersinaDigit} = useComp()

        const vm = getCurrentInstance()
        watch(props.orderDetail , ()=>{
            console.log(props.orderDetail.error)
            vm.data.number= toPersinaDigit(parseInt(props.orderDetail.count).toString())

            vm.data.price= toPersinaDigit(parseInt(props.orderDetail.price).toString())
        }
    )

    },
    methods: {
        conectToOrderDetails(k){

            this.orderDetail.count =this.toEnglishDigit(this.number);
        },
        async removeThisItem(id) {
            this.$store.commit('setIsLoading', true)

            await axios
                .delete(`/order/Delete_product_orderDetail/${id}/`)
                .then(response => {

                    if (response.status == 204) {
                        this.$emit("remove")
                    }

                    notify({
                            title: " .محصول از سبد خرید شما حذف شد ",
                            type: "success",
                            });

                    this.$store.commit('setIsLoading', false)

                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        },

        async sendToOrderDetails(){
            const formData = {
                id: this.orderDetail.id,
                count: this.number,
            }
            this.$store.commit('setIsLoading', true)
            await axios
                .put('/order/update_for_buy/', formData)
                .then(response => {

                    if( response.status == 200 ){
                        this.number = this.toPersinaDigit((parseInt(response.data.count)).toString());
                        this.price = (this.toPersinaDigit(parseInt(response.data.price).toString()));
                        this.orderDetail.count=response.data.count
                        this.orderDetail.price=response.data.price
                        this.orderDetail.error=response.data.error
    
                        this.$emit("orderDetail",this.orderDetail)
                        notify({
                                title: "محصول به سبد خرید اضافه شد",
                                type: "success",
                                });
                    }
                    else if(response.status == 201){

                        this.number = this.toPersinaDigit((parseInt(response.data.number)).toString());
                        console.log(response.data)
                        this.orderDetail.count=response.data.number
                        this.orderDetail.error=""
                        notify({
                        title: " این تعداد در انبار موجود نیست ",
                        type: "warn",
                        });  
                    }
                    //! toDO: edame be product list
                    this.$store.commit('setIsLoading', false)
                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        }
    },

}
</script>