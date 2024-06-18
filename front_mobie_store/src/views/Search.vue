<template>
    <div class="page-serch">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-5 has-text-grey">{{ query }}</h2>
            </div>
<!-- 
            <ProductBox
                v-for="product in products" 
                v-bind:key="product.id"
                v-bind:product="product"
                /> -->
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
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/productBox.vue'
import productListBox from '@/components/productListBox.vue'

export default {
    name: 'Search',
    components: {
        ProductBox,
        productListBox,

    },
    data() {
        return {
            products:[],
            query: ''
        }
    },
    mounted() {
        document.title = 'جستجو'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        setOrderDetails(orderDetails){
            this.$emit("orderDetails",orderDetails)
        },
        async performSearch(){
            this.$store.commit('setIsLoading',true)

            await axios
                .post('api/v1/products/search/', {'query':this.query})
                .then(response =>{
                    this.products = response.data

                    console.log(this.products)
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading',false)

        }
    },
}
</script>


<style>
@import "@/assets/css/search.css"
</style>