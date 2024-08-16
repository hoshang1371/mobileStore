<template>
    <div>
        <div class="content">
            <panelAdminRight/>
            <div class="container_left">

                <div class="productList">
                    <productListBox 
                    @orderDetails="setOrderDetails($event)"
                    v-for="product1 in products" 
                    v-bind:key="product1.id" 
                    v-bind:product="product1"
                    />
                </div>
                
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
    name:"LikedPanelAdmin",
    mixins: [ mixin ],
    components:{
        panelAdminRight,    
        productListBox,
        ProductBox,
    },
    mounted() {
        document.title = 'علاقه مندی ها' + ' | موبایل'
        window.scroll(0, 0);
        this.getLikePanelAdmin();
    },
    data() {
        return {
            liked: [],
            products: [],
        }
    },
    methods: {
        setOrderDetails(orderDetails){
            this.$emit("orderDetails",orderDetails)
        },
        async getLikePanelAdmin() {
            axios
                .get("/api/v1/LikeStarPanelAdminClass/")
                .then(response => {
                    this.$store.commit('setIsLoading', true)
                    this.liked = response.data
                    console.log(this.liked)
                    for( var like in this.liked){
                        console.log(this.liked[like].product.image)
                        this.products.push(this.liked[like].product)
                    }
                    console.log(this.products)
                    // if(response.status == 200){
                    //     notify({
                    //     title: " رمز عبور تغییر کرد ",
                    //     type: "success",
                    //     });
                    // }
                    this.$store.commit('setIsLoading', false)   
                })
        },
    },
}
</script>



<style>
@import "@/assets/css/LikedPanelAdmin.css"
</style>