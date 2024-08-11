<template>
    <div>
        <div class="content">
            <panelAdminRight/>
            <div class="container_left">
                <form @submit.prevent="submitForm">
                    <div>
                        <label>رمز عبور<span>*</span></label>
                        <input v-model="formData.password" type="password" placeholder="رمز عبور">
                    </div>
                    <div class="mt_1">
                        <label>رمز عبور جدید<span>*</span></label>
                        <input v-model="formData.new_password" type="password" placeholder="رمز عبور جدید">
                    </div>
                    <div class="mt_1">
                        <label>تکرار رمز عبور جدید<span>*</span></label>
                        <input v-model="reapet_new_password" type="password" placeholder="تکرار رمز عبور جدید">
                    </div>

                    <div class="capcha">
                        <label>متن را وارد کنید<span>*</span></label>
                        <input v-model="inputValue" placeholder="متن را وارد کنید" class="" type="text" />
                        <VueClientRecaptcha style="flex-direction: row-reverse;" :value="inputValue" @getCode="getCaptchaCode" @isValid="checkValidCaptcha" />
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
    
                    <div>
                        <button type="submit">ذخیره</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import panelAdminRight from '@/components/panelAdminRight.vue'
import mixin  from "../mixins.js"
import { ref, reactive } from "@vue/reactivity";
import VueClientRecaptcha from "vue-client-recaptcha";

import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()

export default{
    name: "phoneNumberPanelAdmin",
    mixins: [ mixin ],

    components:{
        panelAdminRight,
        VueClientRecaptcha,

    },
    data() {
        return {
            formData:{
                password: "",
                new_password: "",
            },
            errors: [],
            reapet_new_password: "",
        }
    },
    mounted() {
        document.title = 'تغییر رمز' + ' | موبایل'
        window.scroll(0, 0);       
    },
    setup() {
        const inputValue = ref(null);

        const dataChapcha = reactive({
            captchaCode: null,
            isValid: false,
        });

        const getCaptchaCode = (value) => {
            /* you can access captcha code */
            // console.log(value);
            dataChapcha.captchaCode = value;

        };

        const checkValidCaptcha = (value) => {
            /* expected return boolean if your value and captcha code are same return True otherwise return False */
            // console.log(value);
            dataChapcha.isValid = value;
            // this.isChapchaTrue =value
            // console.log("this.isChapchaTrue",this.isChapchaTrue);
        };
        return {
            dataChapcha,
            inputValue,
            getCaptchaCode,
            checkValidCaptcha,
        };

    },
    methods: {
        async submitForm() {
            this.errors = []

            if (!this.dataChapcha.isValid) {
                this.errors.push('متن تصویر اشتباه است')
            }
            if(this.formData.password == ''){
                this.errors.push('رمز اشتباه است')
            }
            if(this.new_password == ''){
                this.errors.push('رمز عبور اشتباه است')
            }
            if((this.formData.new_password !== this.reapet_new_password)|(this.formData.new_password == '')){
                this.errors.push('تکرار رمز عبور اشتباه است')
            }
            if ((!this.errors.length) && (this.dataChapcha.isValid)) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    password: this.formData.password,
                    new_password: this.formData.new_password
                }
                axios
                    .put("/api/v1/change_password/", formData)
                    .then(response => {

                        if(response.status == 200){
                            notify({
                            title: " رمز عبور تغییر کرد ",
                            type: "success",
                            });
                        }
                        // else if(response.status == 400){
                        //     notify({
                        //     title: " رمز عبور اشتباه است ",
                        //     type: "warn",
                        //     });
                        // }
                        this.$store.commit('setIsLoading', false)   

                    })
                    .catch(error => {
                        console.log(error)
                        clearInterval(this.interval)
                        this.$store.commit('setIsLoading', false)
                        if (error.response) {
                            // console.log(error.response)
                            // this.errors.push(error.response)
                            for (const property in error.response.data) {
                                // this.errors.push(`${property}:${error.response.data[property]}`)
                                this.errors.push(`${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            // console.log(error.message)
                            this.errors.push('Something went. please try again')

                            // console.log(JSON.stringify(error))
                        }
                    })
                    this.$store.commit('setIsLoading', false)

            }
        }
    },
}
</script>

<style>
@import "@/assets/css/panelAdmin.css";
</style>