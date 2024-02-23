<template>
    <div class="limiter">

        <div class="container-login100">
            <div class="wrap p-t-50 p-b-90">
                <form @submit.prevent="submitForm" class="login-form">
                    <span class="login100-form-title p-b-51"> ایجاد حساب کاربری </span>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Username is required">
                        <input class="input100" type="text" name="username" placeholder="نام کاربری" v-model="username">
                        <span class="focus-input100"></span>
                    </div>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                        <input class="input100" type="password" name="pass" placeholder="رمز" v-model="password">
                        <span class="focus-input100"></span>
                    </div>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                        <input class="input100" type="password" name="pass" placeholder="تکرار رمز" v-model="password2">
                        <span class="focus-input100"></span>
                    </div>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                        <input class="input100" type="email" name="pass" placeholder="ایمیل" v-model="email">
                        <span class="focus-input100"></span>
                    </div>

                    <!-- <div class="flex-sb-m w-full p-t-3 p-b-24">
                <div class="contact100-form-checkbox">
                    <a @click="login" class="txt2">
                        ورود با گوگل
                    </a>

                </div>

            </div> -->
                    <div class="flex-sb-m w-full p-t-3 p-b-24">
                        <VueClientRecaptcha :value="inputValue" @getCode="getCaptchaCode" @isValid="checkValidCaptcha" />
                        <input v-model="inputValue" placeholder="متن را وارد کنید" class="input100" type="text" />
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="container-login100-form-btn m-t-17">
                        <button class="login100-form-btn">
                            ثبت نام
                        </button>
                    </div>
                    <div class="createAccount">
                        <router-link to="/log-in" class="txt1">
                            ورود 
                        </router-link>
                    </div>

                    <div class="createAccount">
                        <!-- <a @click="googleReg" class="txt1">
                            حساب کاربری با گوگل
                        </a> -->
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';
import VueClientRecaptcha from "vue-client-recaptcha";
// import { ref } from "vue";
import { ref, reactive } from "@vue/reactivity";
import { Email } from "@/assets/smtp/smtp.js"

import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()

export default {
    name: "Register",
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            // authUrl:'',
            email: '',
            inputValue: '',
            isChapchaTrue: false,
            errors: [],
        }
    },
    components: {
        VueClientRecaptcha,
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
        // const data = reactive({
        //     captchaCode: null,
        //     isValid: false,
        // });
        // const getCaptchaCode = (value) => {
        //     /* you can access captcha code */
        //     data.captchaCode = value;
        // };

        // const checkValidCaptcha = (value) => {
        //     /* expected return boolean if your value and captcha code are same return True otherwise return False */
        //     data.isValid = value;
        //     if (value) {
        //         alert("Your Captcha is valid now you can submit");
        //     }
        // };

        // return {
        //     inputValue,
        //     data,
        //     getCaptchaCode,
        //     checkValidCaptcha,
        // };
    },
    mounted() {
        document.title = 'ثبت نام' + ' | موبایل'
        window.scroll(0, 0);
    },
    methods: {
        // sendEmail(){
        //     Email.send({
        //         SecureToken: "upbmpccfjbpmgstp",
        //         To: "hojjat.shahpar@gmail.com",
        //         From: "www.ekbatanmobile.ir@gmail.com",
        //         name: "hojjat",
        //         Subject: "kir khar",
        //         Body: "kos nanate vue"
        //     }).then((message) => alert(message));
        // },
        // googleReg() {
        //     window.location.href = "https://accounts.google.com/o/oauth2/auth?client_id=751970675392-t4kssidau1tu5jnhh9msjk9cj1hejtcv.apps.googleusercontent.com&redirect_uri=http://localhost:8080&state=mgPdQffepPVZ10KRuwx0NhWZPlhOv76F&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid+openid+email+profile"

        //     // await axios.get('api/v1/o/google-oauth2/?redirect_uri=http://localhost:8080', {})
        //     //     .then(function (response) {
        //     //         console.log(response.data['authorization_url']);
        //     //         // const authUrl = response.data['authorization_url']
        //     //         // console.log(authUrl)
        //     //         // this.$router.push(authUrl)
        //     //         // window.location.href = authUrl
        //     //         // window.location.href = "https://accounts.google.com/o/oauth2/auth?client_id=751970675392-t4kssidau1tu5jnhh9msjk9cj1hejtcv.apps.googleusercontent.com&redirect_uri=http://localhost:8080&state=mgPdQffepPVZ10KRuwx0NhWZPlhOv76F&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid+openid+email+profile"
        //     //     }).catch(error=>{
        //     //         this.errors.push("مشکل در حساب کاربری با گوگل")
        //     //     })
        // },
        async submitForm() {
            this.errors = []
            // this.sendEmail()
            if (this.username === '') {
                this.errors.push('نام کاربری خالی است')
            }

            if (this.password === '') {
                this.errors.push('رمز اشتباه است')
            }

            if (this.password2 === '') {
                this.errors.push('رمز اشتباه است')
            }
            /*! test shavad */
            if (!(this.password2 === this.password)) {
                this.errors.push('یکی نیست')
            }

            if (this.email === '') {
                this.errors.push('ایمیل اشتباه است')
            }

            if (!this.dataChapcha.isValid) {
                this.errors.push('متن تصویر اشتباه است')
            }

            if ((!this.errors.length) && (this.dataChapcha.isValid)) {
                // console.log("this.checkValidCaptcha", this.dataChapcha.isValid)
                this.$store.commit('setIsLoading', true)
                const formData = {
                    username: this.username,
                    password: this.password,
                    re_password: this.password2,
                    email: this.email,
                    // is_active: false
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        
                        // toast({
                        //     message: 'Accept created, please log in!',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        notify({
                            title: " .ایمیل فعال سازی برای شما ارسال شد ",
                            type: "success",
                            });
                        this.$store.commit('setIsLoading', false)         
                        this.$router.push('/')
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

        }
    },
}
</script>