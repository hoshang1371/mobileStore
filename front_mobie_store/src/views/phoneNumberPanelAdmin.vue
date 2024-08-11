<template>
    <div>
        <div class="content">
            <panelAdminRight/>
            <div class="container_left">
                <form @submit.prevent="submitForm">

                    <div>
                        <label>شماره موبایل<span>*</span></label>
                        <input @keyup="KeyUpFunctionMobilePhone($event)" v-model="formData.mobile" type="text" placeholder="شماره موبایل">
                    </div>
                    <div class="capcha">
                        <label>متن را وارد کنید<span>*</span></label>
                        <input v-model="inputValue" placeholder="متن را وارد کنید" class="" type="text" />
                        <VueClientRecaptcha style="flex-direction: row-reverse;" :value="inputValue" @getCode="getCaptchaCode" @isValid="checkValidCaptcha" />
                    </div>
    
                    <div class="acceptCode">
                        <label>تایید پیامکی<span>*</span></label>
                        <input v-model="formData.code" type="text" placeholder="تایید پیامکی">
                        <button type="button" @click="sendcode()">ارسال کد</button>
                    </div>
                    <div class="counterDown" :class="{ timeFinish: timeFinish }">
                        <p>{{ persianCountDown }}</p>
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
                mobile: "",
                code: "",
                inputValue: '',
            },
            errors: [],
            countDown: 120,
            persianCountDown:"",
            timeFinish: false,
            interval: 0,

        }
    },
    mounted() {
        document.title = 'شماره موبایل' + ' | موبایل'
        window.scroll(0, 0);
        
        // this.startTimer();
       
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
        KeyUpFunctionMobilePhone(k) {
            if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
            let en_number = this.formData.mobile;
            let number = this.toEnglishDigit(en_number);
            // let number_buffer = parseInt(number, 10);
            // console.log("number_buffer",number_buffer)
            // number = number_buffer.toString();
            // console.log(number)
            if (isNaN(number))
                number = "0";
            this.formData.mobile = (this.toPersinaDigit(number));
            }
            else {
            this.formData.mobile = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.formData.mobile)).toString()));
            }
        },
        startTimer(){
            this.timeFinish =false;
            this.interval= setInterval(() => { 
                if(--this.countDown <= 0){
                    clearInterval(this.interval)
                    this.persianCountDown="";
                } 
                // console.log(typeof(interval))
                // this.countDown--;
                if(this.countDown == 10){
                    this.timeFinish = !this.timeFinish
                }
                console.log(this.countDown)
                this.persianCountDown=(this.toPersinaDigit(this.countDown.toString()))
            }, 1000)
        },
        async sendcode(){
            console.log("kiiiiiiiiiiiiiiiiiiiir")
            // console.log(this.toEnglishDigit(this.formData.mobile).toString())
            this.errors = []
            if((this.formData.mobile =='')|(this.formData.mobile == NaN)){
                this.errors.push(' شماره موبایل را صحیح وارد کنید ')
            }
            if (!this.dataChapcha.isValid) {
                this.errors.push('متن تصویر اشتباه است')
            }
            if ((!this.errors.length) && (this.dataChapcha.isValid)) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    mobileNumber: this.toEnglishDigit(this.formData.mobile).toString(),
                }
                axios
                    .post("/api/v1/sendCodeMobileNumber/", formData)
                    .then(response => {
                        // console.log(response)
                        notify({
                            title: " کد برای شما ارسال شد ",
                            type: "success",
                            });
                            this.startTimer();
                        this.$store.commit('setIsLoading', false)   

                    })
                    .catch(error => {
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
        },
        async submitForm() {
            this.errors = []
            if((this.formData.mobile =='')|(this.formData.mobile == NaN)){
                this.errors.push(' شماره موبایل را صحیح وارد کنید ')
            }
            if (!this.dataChapcha.isValid) {
                this.errors.push('متن تصویر اشتباه است')
            }
            if (!this.formData.code) {
                this.errors.push(' کد ارسالی را وارد کنید ')
            }
            if ((!this.errors.length) && (this.dataChapcha.isValid)) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    mobileNumber: this.toEnglishDigit(this.formData.mobile).toString(),
                    code:this.formData.code
                }
                axios
                    .post("/api/v1/setMobileNumber/", formData)
                    .then(response => {
                        clearInterval(this.interval);
                        this.persianCountDown="";
                        console.log(response.data)
                        console.log(response.data.massege)
                        if(response.data.massege == "ok"){
                            notify({
                            title: " کد برای شما ارسال شد ",
                            type: "success",
                            });
                        }
                        else if(response.data.massege == "timeFin"){
                            notify({
                            title: " زمان ارسال کد تمام شد ",
                            type: "warn",
                            });
                            this.errors.push(' زمان تمام شد ')
                        }
 
                        this.$store.commit('setIsLoading', false)   

                    })
                    .catch(error => {
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
        },


    },
}
</script>

<style>
@import "@/assets/css/panelAdmin.css";
</style>
