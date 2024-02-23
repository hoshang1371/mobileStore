<template>
                <li class="glide__slide"
                >
                <productListBox 
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
    }
}
</script>