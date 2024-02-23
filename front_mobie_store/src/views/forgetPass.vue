<template>
    <div class="limiter">

<div class="container-login100">
    <div class="wrap p-t-50 p-b-90">
        <form @submit.prevent="submitForm" class="login-form">
            <span class="login100-form-title p-b-51"> رمز جدید </span>

            <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                <input class="input100" type="password" name="pass" placeholder="رمز" v-model="password">
                <span class="focus-input100"></span>
            </div>

            <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                <input class="input100" type="password" name="pass" placeholder="تکرار رمز" v-model="password2">
                <span class="focus-input100"></span>
            </div>

            <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="container-login100-form-btn m-t-17">
                <button class="login100-form-btn">
                    تایید رمز جدید
                </button>
            </div>
            <div class="createAccount">

                <!-- <a href="#" class="txt1">
                    ساخت حساب کاربری
                </a> -->
            </div>
        </form>
    </div>
</div>
</div>
</template>

<script>
import axios from 'axios';

import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()

export default {
    name: "forgetPass",
    data() {
        return {
            password: '',
            password2: '',
            errors: [],
        }
    },
    mounted() {
        document.title = ' فراموشی رمز ' + ' | موبایل'
        window.scroll(0, 0);
        // this.resetPass()
    },
    methods: {
        // resetPass(){
        //     const uid = this.$route.params.uid
        //     const token = this.$route.params.token
        //     console.log("uid=",uid)
        //     console.log("token=",token)
        // },

        submitForm(){
            this.errors = []

            const uid = this.$route.params.uid
            const token = this.$route.params.token

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

            if(!(this.errors.length)){
                this.$store.commit('setIsLoading', true)

                const formData = {
                    password: this.password,
                    re_password: this.password2,
                }

                axios
                    .post(`password/reset/confirm/${uid}/${token}/`,formData)
                    .then(response =>{
                        this.$store.commit('setIsLoading', false)
                        const message = response.data
                        console.log(message)
                        if(message == "yes"){
                            notify({
                            title: " .رمز عبور شما تغییر کرد . لطفاً وارد شوید",
                            type: "success",
                            });
                            // this.$router.push('/')
                            this.$router.push('/log-in')
                        }
                    })
                    .catch(error => {
                        if (error.response) {
                            // console.log(error.response)
                            // this.errors.push(error.response)
                            for (const property in error.response.data) {
                                // this.errors.push(`${property}:${error.response.data[property]}`)
                                this.errors.push(`${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            console.log(error.message)
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