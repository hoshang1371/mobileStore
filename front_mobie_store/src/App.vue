<template>
    <header class="header" id="header">
        <div class="navigation">
            <div class="container">
                <nav class="nav">

                    <div class="nav__hamburger">
                        <img src="./assets/images/icons8-menu.svg" alt="">
                    </div>
                    <div class="nav__logo">
                        <a href="/" class="scroll-link">موبایل</a>
                    </div>

                    <div class="nav__menu">
                        <div class="menu__top">
                            <span class="nav__category"> موبایل </span>
                            <a href="#" class="close__toggle">
                                <img src="./assets/images/icons8-close.svg" alt="blabla_is_working">
                            </a>
                        </div>

                        <ul class="nav__list">
                            <li class="nav__item">
                                <a href="#header" class="nav__link scroll-link">خانه</a>
                                <!-- <router-link to="/" class="nav__link scroll-link">خانه</router-link> -->

                            </li>

                            <li class="nav__item">
                                <a href="#category" class="nav__link scroll-link">دسته بندی</a>
                            </li>

                            <li class="nav__item">
                                <a href="#news" class="nav__link scroll-link">بلاگ</a>
                            </li>

                            <li class="nav__item">
                                <a href="#contact" class="nav__link scroll-link">تماس با ما</a>
                            </li>
                        </ul>

                    </div>


                    <div class="nav__icons">

                        <router-link to="/log-in" class="icon__item" v-if="!$store.state.isAuthenticated">
                            <img src="./assets/icons/login.png" alt="">
                        </router-link>

                        <router-link to="/register" class="icon__item" v-if="!$store.state.isAuthenticated">
                            <img src="./assets/icons/register.png" alt="">
                        </router-link>

                        <a href="#" @click="setShowSearch()" class="icon__item">
                            <img src="./assets/images/icons8-search.svg" alt="search">
                        </a>

                        <a href="#" class="icon__item" @click="logout()" v-if="$store.state.isAuthenticated">
                            <img src="./assets/icons/logout.png" alt="log_out" >
                        </a>

                        
                        <a class="icon__item" @click="isCloseOrder = !isCloseOrder;" v-if="$store.state.isAuthenticated">
                            <img src="./assets/images/icon-shopping-basket.svg" alt="">
                            <span v-if="orderDetails.length != 0" id="cart__total">{{ persianTotalCount }}</span>
                        </a>
                    </div>

                </nav>



            </div>
        </div>



    </header>

    <div class="is-loading-bar has-text-centered " v-bind:class="{ 'is-loading': $store.state.isLoading }">
        <div class="lds-dual-ring"></div>
    </div>

    <!-- <notifications />  orderDetails-->
    <!-- <notifications position="bottom right" classes="vue-notification" /> -->
    <notifications position="bottom right" classes="notify_class" />
    <router-view 
    @orderDetails="setOrderDetails($event)"
    :orderDetails="orderDetails"
    />
    


    <footer id="footer" class="footer">
        <div class="container">
            <div class="footer__top">
                <div class="footer-top__box">
                    <!-- <h3>EXTERA</h3>
                    <div id="app">
                    </div> -->
                    <OpenLMap />
                </div>
                <!-- <div class="footer-top__box">
                    <h3>اطلاعات</h3>
                    <a href="#">درباره ی ما</a>
                    <a href="#">حریم خصوصی</a>
                    <a href="#">شرایط</a>
                    <a href="#">درباره ی ما</a>
                    <a href="#">نقشه سایت</a>
                </div>
                <div class="footer-top__box">
                    <h3>حساب کاربری</h3>
                    <a href="#">تاریخچه سفارش ها</a>
                    <a href="#">Wish List</a>
                    <a href="#">خبرنامه</a>
                    <a href="#">Returns</a>
                </div> -->
                <div class="footer-top__box">
                    <h3>دربار ی ما</h3>

                    <div class="">
                        <span>
                            <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 297 297" xml:space="preserve">
                                <g>
                                    <path d="M148.5,0C87.43,0,37.747,49.703,37.747,110.797c0,91.026,99.729,179.905,103.976,183.645
		c1.936,1.705,4.356,2.559,6.777,2.559c2.421,0,4.841-0.853,6.778-2.559c4.245-3.739,103.975-92.618,103.975-183.645
		C259.253,49.703,209.57,0,148.5,0z M148.5,272.689c-22.049-21.366-90.243-93.029-90.243-161.892
		c0-49.784,40.483-90.287,90.243-90.287s90.243,40.503,90.243,90.287C238.743,179.659,170.549,251.322,148.5,272.689z" />
                                    <path d="M148.5,59.183c-28.273,0-51.274,23.154-51.274,51.614c0,28.461,23.001,51.614,51.274,51.614
		c28.273,0,51.274-23.153,51.274-51.614C199.774,82.337,176.773,59.183,148.5,59.183z M148.5,141.901
		c-16.964,0-30.765-13.953-30.765-31.104c0-17.15,13.801-31.104,30.765-31.104c16.964,0,30.765,13.953,30.765,31.104
		C179.265,127.948,165.464,141.901,148.5,141.901z" />
                                </g>
                            </svg>
                        </span>
                        {{ siteSettings.address }}
                    </div>

                    <div class="">
                        <span>
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <g stroke="#ccc" stroke-linejoin="round" stroke-width="2">
                                    <path fill=none
                                        d="m2 6c0-1.10457.89543-2 2-2h16c1.1046 0 2 .89543 2 2v12c0 1.1046-.8954 2-2 2h-16c-1.10457 0-2-.8954-2-2z"
                                        stroke-linecap="round" />
                                    <path fill=none
                                        d="m3 5 6.34255 5.6378c1.51555 1.3472 3.79935 1.3472 5.31495 0l6.3425-5.6378" />
                                </g>
                            </svg>
                        </span>
                        {{ siteSettings.email }}
                    </div>

                    <div class="">
                        <span>
                            <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 202.592 202.592"
                                xml:space="preserve">
                                <g>
                                    <g>
                                        <path d="M198.048,160.105l-31.286-31.29c-6.231-6.206-16.552-6.016-23.001,0.433l-15.761,15.761
			c-0.995-0.551-2.026-1.124-3.11-1.732c-9.953-5.515-23.577-13.074-37.914-27.421C72.599,101.48,65.03,87.834,59.5,77.874
			c-0.587-1.056-1.145-2.072-1.696-3.038l10.579-10.565l5.2-5.207c6.46-6.46,6.639-16.778,0.419-23.001L42.715,4.769
			c-6.216-6.216-16.541-6.027-23.001,0.433l-8.818,8.868l0.243,0.24c-2.956,3.772-5.429,8.124-7.265,12.816
			c-1.696,4.466-2.752,8.729-3.235,12.998c-4.13,34.25,11.52,65.55,53.994,108.028c58.711,58.707,106.027,54.273,108.067,54.055
			c4.449-0.53,8.707-1.593,13.038-3.275c4.652-1.818,9.001-4.284,12.769-7.233l0.193,0.168l8.933-8.747
			C204.079,176.661,204.265,166.343,198.048,160.105z M190.683,176.164l-3.937,3.93l-1.568,1.507
			c-2.469,2.387-6.743,5.74-12.984,8.181c-3.543,1.364-7.036,2.24-10.59,2.663c-0.447,0.043-44.95,3.84-100.029-51.235
			C14.743,94.38,7.238,67.395,10.384,41.259c0.394-3.464,1.263-6.95,2.652-10.593c2.462-6.277,5.812-10.547,8.181-13.02l5.443-5.497
			c2.623-2.63,6.714-2.831,9.112-0.433l31.286,31.286c2.394,2.401,2.205,6.492-0.422,9.13L45.507,73.24l1.95,3.282
			c1.084,1.829,2.23,3.879,3.454,6.106c5.812,10.482,13.764,24.83,29.121,40.173c15.317,15.325,29.644,23.27,40.094,29.067
			c2.258,1.249,4.32,2.398,6.17,3.5l3.289,1.95l21.115-21.122c2.634-2.623,6.739-2.817,9.137-0.426l31.272,31.279
			C193.5,169.446,193.31,173.537,190.683,176.164z" />
                                    </g>
                                </g>
                            </svg>
                        </span>
                        {{ siteSettings.phone }}
                    </div>

                    <div class="">
                        <span>
                            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve">
                                <g>
                                    <g>
                                        <path d="M508.645,18.449c-2.929-2.704-7.133-3.51-10.826-2.085L6.715,204.446c-3.541,1.356-6.066,4.515-6.607,8.264
			c-0.541,3.75,0.985,7.496,3.995,9.796l152.127,116.747c-0.004,0.116-0.575,0.224-0.575,0.342v83.592
			c0,3.851,2.663,7.393,6.061,9.213c1.541,0.827,3.51,1.236,5.199,1.236c2.026,0,4.181-0.593,5.931-1.756l56.12-37.367
			l130.369,99.669c1.848,1.413,4.099,2.149,6.365,2.149c1.087,0,2.186-0.169,3.248-0.516c3.27-1.066,5.811-3.672,6.786-6.974
			L511.571,29.082C512.698,25.271,511.563,21.148,508.645,18.449z M170.506,321.508c-0.385,0.36-0.7,0.763-1.019,1.163
			L31.659,217.272L456.525,54.557L170.506,321.508z M176.552,403.661v-48.454l33.852,25.887L176.552,403.661z M359.996,468.354
			l-121.63-93.012c-1.263-1.77-2.975-3.029-4.883-3.733l-47.29-36.163L480.392,60.86L359.996,468.354z" />
                                    </g>
                                </g>
                            </svg>
                        </span>
                        {{ siteSettings.fax }}
                    </div>

                </div>
            </div>
        </div>
    </footer>

    <!-- order Details  orderDetails_show -->
    <div class="orderDetails" v-bind:class="{ orderDetails_show: isCloseOrder}">
        <div class="orderDetails_left" >

            <div class="cart_nav">
                <div class="orderDetails_close_container">
                    <div @click="isCloseOrder = !isCloseOrder;" class="orderDetails_close"><svg class="svg-icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" style="width: 1em; height: 1em; vertical-align: middle; fill: currentcolor; overflow: hidden;"><path d="M810.65984 170.65984q18.3296 0 30.49472 12.16512t12.16512 30.49472q0 18.00192-12.32896 30.33088l-268.67712 268.32896 268.67712 268.32896q12.32896 12.32896 12.32896 30.33088 0 18.3296-12.16512 30.49472t-30.49472 12.16512q-18.00192 0-30.33088-12.32896l-268.32896-268.67712-268.32896 268.67712q-12.32896 12.32896-30.33088 12.32896-18.3296 0-30.49472-12.16512t-12.16512-30.49472q0-18.00192 12.32896-30.33088l268.67712-268.32896-268.67712-268.32896q-12.32896-12.32896-12.32896-30.33088 0-18.3296 12.16512-30.49472t30.49472-12.16512q18.00192 0 30.33088 12.32896l268.32896 268.67712 268.32896-268.67712q12.32896-12.32896 30.33088-12.32896z"></path></svg></div>
                </div>
                <p>سبد خرید</p>
            </div>

            <orderDetails_component 
                @remove="removeItem(index)"
                v-for="(orderDetail, index) in orderDetails"
                v-bind:key="orderDetail.id" v-bind:orderDetail="orderDetail"
               />

               

            <div v-if="orderDetails.length == 0" class="cart_empty">
                <p>سبد خرید شما خالی است</p>
            </div>

            <div class="goto_checkOut">
                <div class="product_price_sum">
                    <a>جمع محصولات</a>
                    <p>تومان {{ persianTotalPrice }}</p>
                </div>
                <div class="look_and_payment">
                    <router-link to="/cart" class="" v-if="$store.state.isAuthenticated">
                        <button @click="isCloseOrder = !isCloseOrder;">مشاهده و پرداخت</button>
                    </router-link>
                </div>
            </div>
        </div>
        <div  class="orderDetails_Right" @click="isCloseOrder = !isCloseOrder;"></div>

    </div>


    <!-- PopUp  hide__popup-->
    <div class="popup hide__popup">
        <div class="popup__content">
            <div class="popup__close">
                <svg class="svg-icon"
                    style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;"
                    viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M810.65984 170.65984q18.3296 0 30.49472 12.16512t12.16512 30.49472q0 18.00192-12.32896 30.33088l-268.67712 268.32896 268.67712 268.32896q12.32896 12.32896 12.32896 30.33088 0 18.3296-12.16512 30.49472t-30.49472 12.16512q-18.00192 0-30.33088-12.32896l-268.32896-268.67712-268.32896 268.67712q-12.32896 12.32896-30.33088 12.32896-18.3296 0-30.49472-12.16512t-12.16512-30.49472q0-18.00192 12.32896-30.33088l268.67712-268.32896-268.67712-268.32896q-12.32896-12.32896-12.32896-30.33088 0-18.3296 12.16512-30.49472t30.49472-12.16512q18.00192 0 30.33088 12.32896l268.32896 268.67712 268.32896-268.67712q12.32896-12.32896 30.33088-12.32896z" />
                </svg>
            </div>

            <div class="popup__left">
                <div class="popup-img__container">
                    <img src="./assets/images/popup.jpg" alt="" class="popup__image">
                </div>
            </div>

            <div class="popup__right">
                <div class="right__content">
                    <h1><span>۳۰٪</span>&nbsp;تخفیف بگیرید&nbsp;</h1>
                    <p>در خبرنامه ما بخوانید و۳۰٪ برای خرید بعدی خود صرفه جویی کنید. قول می دهیم هرزنامه نیست</p>
                    <form action="#">
                        <input type="email" class="popup__form" placeholder="ایمیل خود را وارد کنید...">
                        <a href="#">اشتراک</a>
                    </form>
                </div>
            </div>
        </div>
    </div>


    <!-- search -->
    <div class="search hide__search">
        <div class="search__content">
            <div class="search__close">
                <svg class="svg-icon"
                    style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;"
                    viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M810.65984 170.65984q18.3296 0 30.49472 12.16512t12.16512 30.49472q0 18.00192-12.32896 30.33088l-268.67712 268.32896 268.67712 268.32896q12.32896 12.32896 12.32896 30.33088 0 18.3296-12.16512 30.49472t-30.49472 12.16512q-18.00192 0-30.33088-12.32896l-268.32896-268.67712-268.32896 268.67712q-12.32896 12.32896-30.33088 12.32896-18.3296 0-30.49472-12.16512t-12.16512-30.49472q0-18.00192 12.32896-30.33088l268.67712-268.32896-268.67712-268.32896q-12.32896-12.32896-12.32896-30.33088 0-18.3296 12.16512-30.49472t30.49472-12.16512q18.00192 0 30.33088 12.32896l268.32896 268.67712 268.32896-268.67712q12.32896-12.32896 30.33088-12.32896z" />
                </svg>
            </div>

            <div class="search__right">
                <div class="right__content">
                    <form method="get" action="/search">
                        <input v-model="searchData" class="popup__form" placeholder="جستجو"  name="query">
                        <button href="#">جستجو</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- Go to top goto-top -->

    <a href="#" class="goto-top scroll-link">
        <svg xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision"
            image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd" viewBox="0 0 512 299.283">
            <path
                d="M75.334 286.691c-64.764 36.929-96.186-15.595-60.203-51.975L215.997 25.104c33.472-33.472 46.534-33.472 80.006 0l200.866 209.612c35.983 36.38 4.561 88.904-60.203 51.975L256 189.339 75.334 286.691z" />
        </svg>
    </a>
</template>




<script>
import axios from 'axios'
// import { mapir } from "mapir-vue";
// import { mapir, mapMarker } from "mapir-vue";
import Map from './components/Map.vue'
import OpenLMap from './components/OpenLMap.vue'
import orderDetails_component from '@/components/orderDetails_component.vue'

// import toPersinaDigit from '@/views/ProductDetails.vue'
// import sliderUpBox from '@/components/sliderUpBox.vue'
// <orderDetails v-for="sliderUpp in sliderUp" v-bind:key="sliderUpp.id" v-bind:sliderUpp="sliderUpp" />
import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()

// import orderDetails  from "./mixins.js"
// import totalCount  from "./mixins.js"
// import persianTotalCount  from "./mixins.js"
// import totalPrice  from "./mixins.js"
// import persianTotalPrice  from "./mixins.js"
import mixin  from "./mixins.js"

// import toPersinaDigit  from "./mixins.js"

export default {
    name: "App",
    inheritAttrs: false,
    components: {
        // mapir,
        // mapMarker,
        Map,
        OpenLMap,
        orderDetails_component,
    },
    mixins: [ mixin ],
    data() {
        return {
            siteSettings: [],
            orderDetails: [],
            // totalCount: 0,
            // persianTotalCount: '',
            // totalPrice: 0,
            // persianTotalPrice: 0,
            // your Api Key.
            isCloseOrder: true,
            searchData: ""
        }
    },

    beforeCreate() {
        this.$store.commit('initailizeStore')

        const token = this.$store.state.token

        if (token) {
            axios.defaults.headers.common['Authorization'] = "Token " + token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
    },
    created() {
        // this.map = null;
    },

    mounted() {
        this.getSiteSettings()

        if(this.$store.state.isAuthenticated)
            this.getOrderDetails()

        const navOpen = document.querySelector('.nav__hamburger');
        const navClose = document.querySelector('.close__toggle');
        const menu = document.querySelector('.nav__menu');
        const navContainer = document.querySelector('.nav__menu');


        navOpen.addEventListener('click', () => {
            menu.classList.add('open');
            document.body.classList.add('active');
            navContainer.style.right = '0';
            navContainer.style.width = '30rem';
        });

        navClose.addEventListener('click', () => {
            menu.classList.remove('open');
            document.body.classList.remove('active');
            navContainer.style.right = '-30rem';
            navContainer.style.width = '0';
        });

        const search = document.querySelector(".search")
        const closeSearch = document.querySelector(".search__close")

        if (search) {
            closeSearch.addEventListener("click", () => {
                search.classList.add("hide__search");
            })
        }

        // const popup = document.querySelector(".popup")
        // const closePopup = document.querySelector(".popup__close")

        // if (popup) {
        //     closePopup.addEventListener("click", () => {
        //         popup.classList.add("hide__popup");
        //     })
        // }

        // window.addEventListener('load', () => {
        //     setTimeout(() => {
        //         popup.classList.remove('hide__popup');
        //     }, 500);
        // });

        /*
        ============================
        Fixed Navigator
        ============================
        */
        const navBar = document.querySelector('.navigation')
        const gotoTop = document.querySelector('.goto-top')
        const scrollLink = document.querySelectorAll(".scroll-link")
        // Smooth Scroll 
        // Array.from(scrollLink).map(link=>{
        //     link.addEventListener('click', e=>{
        //         // prevent default
        //         e.preventDefault();
        //         console.log(e)
        //         const id = e.currentTarget.getAttribute("href").slice(1);
        //         console.log(id)
        //         const element = document.getElementById(id)
        //         const navHeight = navBar.getBoundingClientRect().height;
        //         const fixedNav = navBar.classList.contains('fixed__nav');
        //         console.log(element)
        //         let position = element.offsetTop - navHeight

        //         if(!fixedNav){
        //             position = position - navHeight
        //         }

        //         window.scrollTo({
        //             left: 0,
        //             top: position,
        //         });
        //         navContainer.style.left = "-30rem";
        //         document.body.classList.remove("active");
        //     });
        // });

        // Fix NavBar

        window.addEventListener('scroll', e => {
            const scrollHeight = window.pageYOffset;
            const navHeight = navBar.getBoundingClientRect().height;

            if (scrollHeight > navHeight) {
                navBar.classList.add('fix__nav');
            } else {
                navBar.classList.remove("fix__nav");
            }

            if (scrollHeight > 300) {
                gotoTop.classList.add('show-top')
            } else {
                gotoTop.classList.remove("show-top");
            }
        });


        // this.$notify("Hello user!");
    },
    methods: {
        // toPersinaDigit(digit) {
        //     var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
        //     return digit.replace(/[0-9]/g, function (w) { return id[+w] });
        // },
        
        // onMapLoaded(event) {
        //     // in component
        //     this.map = event.map;
        //     // or just to store if you want have access from other components
        //     this.$store.map = event.map;
        // },
        // onClick(e) {
        //     console.log(e, "HIiiiiiiii");
        // },
        setOrderDetails(orderDetails){
            this.orderDetails = orderDetails
            this.totalCount = 0
            this.totalPrice = 0
            for(let orderDetail in this.orderDetails){
                this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
            }
            this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
            this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())

         },
        async getSiteSettings() {
            await axios
                .get('/site__Setting/')
                .then(response => {
                    this.siteSettings = response.data
                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        },

        async getOrderDetails() {
            await axios
                .get('/order/product_order/')
                .then(response => {

                    this.orderDetails = response.data

                    for(let orderDetail in this.orderDetails){
                        this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                        this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
                    }
                    // console.log(this.totalPrice)
                    this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
                    this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())
                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        },

        // orderDetails_close(){
        //     console.log(this.isCloseOrder);
        // }

        removeItem(index){
            this.orderDetails.splice(index,1);
            
            this.totalCount = 0
            this.totalPrice = 0
            for(let orderDetail in this.orderDetails){
                        this.totalCount = this.totalCount + this.orderDetails[orderDetail].count
                        this.totalPrice = this.totalPrice + this.orderDetails[orderDetail].price
                    }
                    this.persianTotalCount = this.toPersinaDigit(this.totalCount.toString())
                    this.persianTotalPrice = this.toPersinaDigit(this.totalPrice.toString())

        },

        logout(){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')

        },
        setShowSearch(){
            const search = document.querySelector(".search")

            search.classList.remove("hide__search");
        },

        async postSearch(){
            // console.log(this.searchData)

            this.$store.commit('setIsLoading', true)
            const formData = {
                query: this.searchData,
            }
            await axios
                .post('api/v1/products/search/', formData)
                .then(response => {
                    console.log(response.status)
                    console.log(response.data)
                    //! toDO: edame be product list
                    this.$store.commit('setIsLoading', false)
                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        },
    },
}
</script>

<style>
/* .notify_class{
    background-color: red;
} */
.notify_class {
    margin: 0 5px 5px;
    padding: 10px;
    font-size: 12px;
    color: #ffffff;
    direction: rtl;

    background: #44a4fc;
    border-right: 5px solid #187fe7;

    &.success {
        background: #68cd86;
        border-right-color: #42a85f;
    }

    &.warn {
        background: #ffb648;
        border-left-color: #f48a06;
    }

    &.error {
        background: #e54d42;
        border-left-color: #b82e24;
    }
}

.notify_class div {
    direction: rtl;
    text-align: center;
    font-family: KalamehWeb_Bold;
    /* font-size: 20px; */
    font-size: 2rem;
}
</style>

<style lang="scss">
.lds-dual-ring {
    display: inline-block;
    width: 90px;
    height: 90px;
}

.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.is-loading-bar {
    height: 0;
    overflow: hidden;

    -webkit-transition: all 0.3s;
    transition: all 0.3s;

    &.is-loading {
        // height: 90px;
        height: 100%;
        position: fixed;
        display: flex;
        width: 100%;
        justify-content: center;
        align-items: center;
    }
}
</style>
