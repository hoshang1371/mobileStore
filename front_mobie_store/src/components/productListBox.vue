<template>
    <div class="product" @click="toProductDitails()" @click.middle ="newTabProductDitails()" @mousedown.middle.prevent.stop>
        <div class="product__header">
            <img :src="product.get_thumbnail" alt="">
        </div>
        <div class="product__footer">
            <!-- product.average_rating -->
            <h3>{{ product.title }}</h3>
            <div class="rating">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                    id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                    enable-background="new 0 0 122.88 116.864" xml:space="preserve" v-for="star in  5 " :key="star" :class="{
                        'active': star <= product.int_average_rating,
                        'deactive': star > product.int_average_rating
                    }">
                    <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                            points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0"
                            :style="[
                                (star == product.int_average_rating + 1) && (product.float_average_rating) ? { 'opacity': product.float_average_rating, 'background-color': 'red', 'fill': 'var(--yellow)' } : '',
                            ]" />
                    </g>
                </svg>


            </div>

            <div class="product__price">
                <h4 :class="{
                    'product__price_kh': product.priceOff != null,
                }">
                    {{ product.price }} تومان</h4>
                <h3 v-if="product.priceOff != null">تخفیف</h3>
                <h4 v-if="product.priceOff != null">{{ product.priceOff }} تومان</h4>
                <button class="product__btn" @click.prevent.stop @click="addToOrder()">اضافه به سبد خرید</button>
            </div>

            <!-- <ul>

                <a href="#" data>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                        version="1.1" id="Capa_1" width="800px" height="800px" viewBox="0 0 442.04 442.04"
                        xml:space="preserve">
                        <g>
                            <g>
                                <path
                                    d="M221.02,341.304c-49.708,0-103.206-19.44-154.71-56.22C27.808,257.59,4.044,230.351,3.051,229.203    c-4.068-4.697-4.068-11.669,0-16.367c0.993-1.146,24.756-28.387,63.259-55.881c51.505-36.777,105.003-56.219,154.71-56.219    c49.708,0,103.207,19.441,154.71,56.219c38.502,27.494,62.266,54.734,63.259,55.881c4.068,4.697,4.068,11.669,0,16.367    c-0.993,1.146-24.756,28.387-63.259,55.881C324.227,321.863,270.729,341.304,221.02,341.304z M29.638,221.021    c9.61,9.799,27.747,27.03,51.694,44.071c32.83,23.361,83.714,51.212,139.688,51.212s106.859-27.851,139.688-51.212    c23.944-17.038,42.082-34.271,51.694-44.071c-9.609-9.799-27.747-27.03-51.694-44.071    c-32.829-23.362-83.714-51.212-139.688-51.212s-106.858,27.85-139.688,51.212C57.388,193.988,39.25,211.219,29.638,221.021z" />
                            </g>
                            <g>
                                <path
                                    d="M221.02,298.521c-42.734,0-77.5-34.767-77.5-77.5c0-42.733,34.766-77.5,77.5-77.5c18.794,0,36.924,6.814,51.048,19.188    c5.193,4.549,5.715,12.446,1.166,17.639c-4.549,5.193-12.447,5.714-17.639,1.166c-9.564-8.379-21.844-12.993-34.576-12.993    c-28.949,0-52.5,23.552-52.5,52.5s23.551,52.5,52.5,52.5c28.95,0,52.5-23.552,52.5-52.5c0-6.903,5.597-12.5,12.5-12.5    s12.5,5.597,12.5,12.5C298.521,263.754,263.754,298.521,221.02,298.521z" />
                            </g>
                            <g>
                                <path
                                    d="M221.02,246.021c-13.785,0-25-11.215-25-25s11.215-25,25-25c13.786,0,25,11.215,25,25S234.806,246.021,221.02,246.021z" />
                            </g>
                        </g>
                    </svg> </a>
                <a href="#" data>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                        height="800px" width="800px" version="1.1" id="Capa_1" viewBox="0 0 471.701 471.701"
                        xml:space="preserve">
                        <g>
                            <path
                                d="M433.601,67.001c-24.7-24.7-57.4-38.2-92.3-38.2s-67.7,13.6-92.4,38.3l-12.9,12.9l-13.1-13.1   c-24.7-24.7-57.6-38.4-92.5-38.4c-34.8,0-67.6,13.6-92.2,38.2c-24.7,24.7-38.3,57.5-38.2,92.4c0,34.9,13.7,67.6,38.4,92.3   l187.8,187.8c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-3.9l188.2-187.5c24.7-24.7,38.3-57.5,38.3-92.4   C471.801,124.501,458.301,91.701,433.601,67.001z M414.401,232.701l-178.7,178l-178.3-178.3c-19.6-19.6-30.4-45.6-30.4-73.3   s10.7-53.7,30.3-73.2c19.5-19.5,45.5-30.3,73.1-30.3c27.7,0,53.8,10.8,73.4,30.4l22.6,22.6c5.3,5.3,13.8,5.3,19.1,0l22.4-22.4   c19.6-19.6,45.7-30.4,73.3-30.4c27.6,0,53.6,10.8,73.2,30.3c19.6,19.6,30.3,45.6,30.3,73.3   C444.801,187.101,434.001,213.101,414.401,232.701z" />
                        </g>
                    </svg>
                </a>
                <a href="#" data>
                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16">
                        <path fill="currentColor"
                            d="M13.901 2.599A8 8 0 0 0 0 8h1.5a6.5 6.5 0 0 1 11.339-4.339L10.5 6H16V.5l-2.099 2.099zM14.5 8a6.5 6.5 0 0 1-11.339 4.339L5.5 10H0v5.5l2.099-2.099A8 8 0 0 0 16 8h-1.5z" />
                    </svg>
                </a>

            </ul> -->
        </div>

    </div>
</template>

<script>
import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";

// import orderDetails from "../mixins.js"
// import totalCount  from "../mixins.js"
// import persianTotalCount  from "../mixins.js"
// import totalPrice  from "../mixins.js"
// import persianTotalPrice  from "../mixins.js"


import mixin from "../mixins.js"


// import { useComposition } from '@/compositions/composition'

const { notify } = useNotification()
export default {
    name: 'productListBox',
    props: {
        product: Object,
    },

   mixins: [ mixin ],
    // data() {
    //     return {
    //         orderDetails :[]
    //     }
    // },
    mounted() {
    },

    methods: {
        
        toProductDitails() {           
            // const toPath = this.$route.query.to || '/'
            this.$router.push(this.product.get_absolute_url)
        },
        newTabProductDitails() {           
            // const toPath = this.$route.query.to || '/'
            window.open( this.product.get_absolute_url, "_blank");
        },
        async addToOrder(){

            this.$store.commit('setIsLoading', true)
            const formData = {
                code: this.product.code,
                count : '1',
            }
            await axios
                .post('/order/product_order/',formData)
                .then(response => {

                    // console.log(this.orderDetails)
                    this.orderDetails = response.data
                    this.$emit("orderDetails",this.orderDetails)
                    // @orderDetails="setOrderDetails($event)"

                    // this.totalCount = 0
                    // this.totalPrice = 0

                    // for(let orderDetail in this.orderDetails){
                    //     this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                    //     this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
                    // }
                    // this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
                    // this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())

                    notify({
                            title: "یک عدد محصول به سبد خرید اضافه شد",
                            type: "success",
                            });
                    this.$store.commit('setIsLoading', false)
                })
                .catch(error => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                        });  
                })
        }
    },
}
</script>