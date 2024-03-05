<template>
    <div class="add-comment-section">
        <input  v-model="message" type="text" class="form-control mr-3" placeholder="افزودن نظر">
        <button @click="postResponseComment(customerComment.id)"  class="btn btn-primary" type="button">ارسال</button>
    </div>
</template>


<script>
import axios from 'axios';

import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()

export default {
    name: 'customerComentPost',
    props: {
        customerComment: Object,
    },
    data() {
        return {
            message:"",
        }
    },
    mounted() {

    },
    methods: {
        async postResponseComment(id){
            const product_id = this.$route.params.product_id
            console.log(id)
            console.log(product_id)
            console.log(this.message)
            
            this.$store.commit('setIsLoading', true)
            const formData = {
                product: product_id,
                text : this.message,
                parent : this.customerComment.id
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
        }  
    },
}
</script>