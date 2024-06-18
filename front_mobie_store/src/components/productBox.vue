<template>
                <li class="glide__slide"
                >
                <productListBox 
                  @orderDetails="setOrderDetails($event)"
                  v-bind:key="product.id" 
                  v-bind:product="product" 
                  />

                </li>
</template>

<script>

import productListBox from '@/components/productListBox.vue'

export default {
    name: 'ProductBox',
    props: {
        product: Object,
    },
    components: {
      productListBox,
    },
    methods: {
      setOrderDetails(orderDetails){
            this.$emit("orderDetails",orderDetails)
      },
    },
}
</script>