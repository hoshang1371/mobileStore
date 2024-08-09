<template>
    <div class="cantaner_center">
        <div class="cantainer_left">
            <div class="category">
                <div  v-for="cat in productDetais.categories">
                    <a :href="'/category'+'?query='+cat.title">{{ cat.title }}</a>
                    <p>/</p>
                </div>
            </div>
            <!-- <img src="../assets/images/products/eniko-kis-KsLPTsYaqIQ-unsplash.jpg" alt=""> -->
            <!-- <img :src="productDetais.get_image" alt="">  this.productDetais.categories-->
            <vue-image-zoomer :regular="this.originalImg" :zoom="this.originalImg" img-class="img-fluid" alt="Product"
                hover-message="ذره بین" touch-message="ذره بین" close-pos="top-right" message-pos="top" />
            <!-- <vue-image-zoomer :regular="productDetais.get_image" :zoom="productDetais.get_image" img-class="img-fluid"
                alt="Product" hover-message="ذره بین" touch-message="ذره بین" close-pos="top-right" message-pos="top" /> -->
            <div class="image_list">
                <img v-for="ProductGallery in ProductGallerys" :src="ProductGallery.image" :alt="ProductGallery.title"
                    @click="setImage(ProductGallery.image)" />
            </div>
        </div>
        <div class="cantainer_right">
            <h1>{{ productDetais.title }}</h1>

            <div class="rating">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                    id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                    enable-background="new 0 0 122.88 116.864" xml:space="preserve" v-for="star in  5 " :key="star" :class="{
                        'active': star <= stars,
                        'deactive': star > stars
                    }" @click="$store.state.isAuthenticated ? postStar(star) : ''" :style="[
    $store.state.isAuthenticated ? { 'cursor': 'pointer' } : '',
]">
                    <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                            points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0"
                            :style="[
                                (star == stars + 1) && (starsF) ? { 'opacity': starsF, 'background-color': 'red', 'fill': 'var(--yellow)' } : '',
                            ]" />
                    </g>
                </svg>


            </div>

            <span>{{ productDetais.description }}</span>

            <!-- <div class="product__price">
                <h4 class="product__price_kh">{{productDetais.price}} تومان</h4>
                <h3>تخفیف</h3>
                <h4>{{productDetais.priceOff}} تومان</h4>
            </div> -->

            <div class="product__price">
                <h4 :class="{
                    'product__price_kh': productDetais.priceOff != null,
                }">
                    {{ productDetais.price }} تومان</h4>
                <h3 v-if="productDetais.priceOff != null">تخفیف</h3>
                <h4 v-if="productDetais.priceOff != null">{{ productDetais.priceOff }} تومان</h4>
            </div>

            <div class="likes" v-bind:class="$store.state.isAuthenticated ? 'likesHover' : '',
                boolLike ? 'liked' : ''
                ">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                    height="800px" width="800px" version="1.1" id="Capa_1" viewBox="0 0 471.701 471.701"
                    xml:space="preserve" @click="$store.state.isAuthenticated ? postLike() : ''" :style="[
                        $store.state.isAuthenticated ? { 'cursor': 'pointer' } : '',
                    ]">
                    <g>
                        <path
                            d="M433.601,67.001c-24.7-24.7-57.4-38.2-92.3-38.2s-67.7,13.6-92.4,38.3l-12.9,12.9l-13.1-13.1   c-24.7-24.7-57.6-38.4-92.5-38.4c-34.8,0-67.6,13.6-92.2,38.2c-24.7,24.7-38.3,57.5-38.2,92.4c0,34.9,13.7,67.6,38.4,92.3   l187.8,187.8c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-3.9l188.2-187.5c24.7-24.7,38.3-57.5,38.3-92.4   C471.801,124.501,458.301,91.701,433.601,67.001z M414.401,232.701l-178.7,178l-178.3-178.3c-19.6-19.6-30.4-45.6-30.4-73.3   s10.7-53.7,30.3-73.2c19.5-19.5,45.5-30.3,73.1-30.3c27.7,0,53.8,10.8,73.4,30.4l22.6,22.6c5.3,5.3,13.8,5.3,19.1,0l22.4-22.4   c19.6-19.6,45.7-30.4,73.3-30.4c27.6,0,53.6,10.8,73.2,30.3c19.6,19.6,30.3,45.6,30.3,73.3   C444.801,187.101,434.001,213.101,414.401,232.701z" />
                    </g>
                </svg>
                <span>{{ likes }}</span>
            </div>

            <div class="numberOfProduct">
                <div class="number">
                    <input type="text" id="numberProduct" name="first_name" class="toPe" @keyup="KeyUpFunction($event)"
                        v-model="number">
                    <a class="up">
                        <div class='BCup' @click="BCupClick()">+</div>
                        <div class='BCdown' @click="BCdownClick()">-</div>
                    </a>
                </div>

                <button class="AddToCart" @click="AddToCart()">اضافه به سبد خرید</button>
            </div>

        </div>
    </div>

    <div class="cantainer_comment">


        <div class="cantainer_comment_down">

            <commentSection @remove="removeItem(index)" v-for="(comment, index) in comments" v-bind:key="comment.id" v-bind:comment="comment" />



        </div>


        <div class="cantainer_comment_up">
            <div class="add-comment-section">
                <input  v-model="message" type="text" class="form-control mr-3" placeholder="افزودن نظر">
                <button @click="$store.state.isAuthenticated ? postComment() : loginCustomerComment()"  class="btn btn-primary" type="button">ارسال</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import { VueImageZoomer } from 'vue-image-zoomer'
import 'vue-image-zoomer/dist/style.css';


import commentSection from '@/components/commentSection.vue'

import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()
import mixin  from "../mixins.js"

export default {
    name: "ProductDetails",
    components: {
        VueImageZoomer,
        commentSection,
    },
    mixins: [ mixin ],
    props: {
        orderDetails: Object,
    },
    data() {
        return {
            number: "1",
            productDetais: [],
            ProductGallerys: [],
            stars: "0",
            starsF: 0.0,
            likes: "",
            boolLike: false,
            originalImg: "",
            comments: [],
            message: "",
            // orderDetails: Object,
        }
    },
    mounted() {
        window.scroll(0, 0);
        let BCup = document.querySelector('.BCup');
        let BCdown = document.querySelector('.BCdown');
        // let numberProduct = document.querySelector('#numberProduct');

        console.log("this.orderDetails=",this.orderDetails)
        this.number = this.toPersinaDigit(this.number)


        this.getProductDetails()
        this.getLike()
        this.getProductGallery()
        this.getComments()
        // this.getLikesCustomerComment()
        // console.log(axios.defaults.headers.common['Authorization'])
        // window.scroll(0, 0);
        // const product_id = this.$route.params.product_id
        // const product_title = this.$route.params.product_title

        // document.title = 'ثبت نام' + ' | موبایل'
        // window.scroll(0, 0);

        // console.log("product_id=",product_id)
        // console.log("product_title=",product_title)
    },
    methods: {
        BCupClick() {
            this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) + 1).toString())
        },
        BCdownClick() {
            if (parseInt(this.toEnglishDigit(this.number)) > 1)
                this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) - 1).toString())
        },
        toEnglishDigit(replaceString) {
            var find = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
            var replace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

            var regex;
            for (var i = 0; i < find.length; i++) {
                regex = new RegExp(find[i], "g");
                replaceString = replaceString.replace(regex, replace[i]);
            }
            return replaceString;
        },

        // KeyUpFunction(k) {

        //     if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
        //         let en_number = this.number;

        //         let number = this.toEnglishDigit(en_number);
        //         let number_buffer = parseInt(number, 10);
        //         number = number_buffer.toString();
        //         // console.log(number)
        //         if (isNaN(number))
        //             number = "0";
        //         this.number = (this.toPersinaDigit(number));
        //     }
        //     else {
        //         this.number = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.number)).toString()));
        //     }
        // },
        // product_id
        // product_title

        async getProductDetails() {
            const product_id = this.$route.params.product_id
            const product_title = this.$route.params.product_title
            await axios
                // .get(`api/v1/products/${product_id}/${product_title}`) productDetais.get_image
                .get(`api/v1/products/${product_id}`)
                .then(response => {
                    this.productDetais = response.data
                    this.originalImg = this.productDetais.get_image
                    // console.log(this.productDetais.categories)
                    this.stars = this.productDetais.int_average_rating
                    this.starsF = this.productDetais.float_average_rating
                })
        },


        async getComments() {
            const product_id = this.$route.params.product_id
            const product_title = this.$route.params.product_title


            await axios
                // .get(`api/v1/products/${product_id}/${product_title}`) productDetais.get_image
                .get(`/api/v1/GetCustomerComment/${product_id}`)
                .then(response => {
                    this.comments = response.data
                    // console.log("this.comments=",this.comments)
                })
        },

        async postLike() {
            const product_id = this.$route.params.product_id
            const formData = {
                product: this.productDetais.id,
            }
            await axios
                .post(`api/v1/GetLikeClass/${product_id}`, formData)
                .then(response => {
                    // console.log(response.data)  
                    this.boolLike = response.data["like"]
                    this.likes = this.toPersinaDigit(response.data["numberLike"].toString())
                })
            // console.log("kir")
        },
        async getLike() {
            const product_id = this.$route.params.product_id
            await axios
                .get(`api/v1/GetLikeClass/${product_id}`)
                .then(response => {
                    this.boolLike = response.data["like"]
                    this.likes = this.toPersinaDigit(response.data["numberLike"].toString())
                })
        },

        // async getLikesCustomerComment() {
        //     const product_id = this.$route.params.product_id
        //     await axios
        //         .get(`/api/v1/GetLikesCustomerComment/${product_id}`)
        //         .then(response => {
        //             console.log(response.data)
        //         })
        // },

        async getProductGallery() {
            const product_id = this.$route.params.product_id
            await axios
                .get(`api/v1/GetProductDetailProductGallery/${product_id}`)
                .then(response => {
                    this.ProductGallerys = response.data
                })
        },

        setImage(img) {
            console.log(img)
            this.originalImg = img
        },

        async postStar(starId) {
            this.$store.commit('setIsLoading', true)
            const formData = {
                stars: starId,
                product: this.productDetais.id,
            }
            await axios
                .post("api/v1/SetStarClass/", formData)
                .then(response => {
                    this.stars = response.data["ratI"]
                    this.starsF = response.data["ratF"]
                    this.$store.commit('setIsLoading', false)
                })
            // console.log("starId", (starId))
        },

        removeItem(index){
            this.comments.splice(index,1);
        },

        async postComment(){

            this.$store.commit('setIsLoading', true)
            const formData = {
                product: this.productDetais.id,
                text : this.message,
                parent : null
            }
            await axios
                .post("/api/v1/PostCustomerComment/", formData)
                .then(response => {
                    notify({
                            title: "نظر شما با موفقیت ثبت شد پش از بررسی اعمال خواهد شد",
                            type: "success",
                            });
                    this.$store.commit('setIsLoading', false)
                    this.message = "";
                })
                this.$store.commit('setIsLoading', false)
        },

        loginCustomerComment()
        {
            notify({
                        title: "لطفا وارد حساب کاربری خود شوید",
                        type: "warn",
                    });        
        },

 

        async AddToCart(){

            this.$store.commit('setIsLoading', true)
            const toPath = this.$route.query.to || '/'
            const formData = {
                code: this.productDetais.code,
                count : this.toEnglishDigit(this.number),
            }
            await axios
                .post('/order/product_order/',formData)
                .then(response => {

                    if( response.status == 200 ){

                        for(var a in response.data){

                            if(this.orderDetails[a]==undefined){
                                this.orderDetails.push(response.data[a])
                            }
                            this.orderDetails[a].count = response.data[a].count
                        }
                        this.$emit("orderDetails",this.orderDetails)
                        notify({
                                title: "محصول به سبد خرید اضافه شد",
                                type: "success",
                                });
                                // this.setOrderDetails(this.orderDetails);
                                // this.$emit("orderDetails",response.data)
                                // this.$router.push(toPath)
                    }
                    else if(response.status == 201){
                        notify({
                        title: " این تعداد در انبار موجود نیست ",
                        type: "warn",
                        });  
                    }
                    this.$store.commit('setIsLoading', false)
                })
                /*.catch(error => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                        });  
                })*/
        }

    },
    // updated() {
    //     console.log("updated=",this.orderDetails)
    // },
}

</script>

<style>
@import "@/assets/css/ProductDetails.css"
</style>