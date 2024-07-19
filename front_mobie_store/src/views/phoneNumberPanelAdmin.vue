<template>
    <div>
        <div class="content">
            <panelAdminRight/>
            <div class="container_left">
                <div>
                    <label>شماره موبایل<span>*</span></label>
                    <input @keyup="KeyUpFunctionMobilePhone($event)" v-model="formData.mobile" type="text" placeholder="شماره موبایل">
                </div>
                <div class="capcha">
                    <label>متن را وارد کنید<span>*</span></label>
                    <input v-model="inputValue" placeholder="متن را وارد کنید" class="" type="text" />
                    <VueClientRecaptcha style="    flex-direction: row-reverse;" :value="inputValue" @getCode="getCaptchaCode" @isValid="checkValidCaptcha" />
                </div>

                <div class="acceptCode">
                    <label>تایید پیامکی<span>*</span></label>
                    <input @keyup="KeyUpFunctionMobilePhone($event)" v-model="formData.mobile" type="text" placeholder="تایید پیامکی">
                    <button >ارسال کد</button>
                </div>
                <!-- <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div> -->

                <div>
                    <button>ذخیره</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import panelAdminRight from '@/components/panelAdminRight.vue'
import mixin  from "../mixins.js"
import { ref, reactive } from "@vue/reactivity";
import VueClientRecaptcha from "vue-client-recaptcha";

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
                inputValue: '',
                errors: [],
            }
        }
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
            let number_buffer = parseInt(number, 10);
            number = number_buffer.toString();
            // console.log(number)
            if (isNaN(number))
                number = "0";
            this.formData.mobile = (this.toPersinaDigit(number));
            }
            else {
            this.formData.mobile = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.formData.mobile)).toString()));
            }
        },
    },
}
</script>

<style>
@import "@/assets/css/panelAdmin.css";
</style>
