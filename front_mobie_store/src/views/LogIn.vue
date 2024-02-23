<template>
    <div class="limiter">

        <div class="container-login100">
            <div class="wrap p-t-50 p-b-90">
                <form @submit.prevent="submitForm" class="login-form">
                    <span class="login100-form-title p-b-51"> ورود </span>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Username is required">
                        <input class="input100" type="text" name="email" placeholder="ایمیل" v-model="email">
                        <span class="focus-input100"></span>
                    </div>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Password is required">
                        <input class="input100" type="password" name="pass" placeholder="رمز" v-model="password">
                        <span class="focus-input100"></span>
                    </div>

                    <div class="flex-sb-m w-full p-t-3 p-b-24">
                        <div class="contact100-form-checkbox">
                            <!-- <a @click="login" class="txt2">
                                ورود با گوگل
                            </a> -->

                        </div>
                        <div>
                            <!-- <a href="#" class="txt1">
                                فراموشی؟
                            </a> -->
                            <router-link to="/sendForgetPass" class="txt1">
                                فراموشی؟
                            </router-link>
                        </div>

                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="container-login100-form-btn m-t-17">
                        <button class="login100-form-btn">
                            ورود
                        </button>
                    </div>
                    <div class="createAccount">
                        <router-link to="/register" class="txt1">
                            ساخت حساب کاربری
                        </router-link>
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
import { googleSdkLoaded } from "vue3-google-login";

import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()


export default {
    name: "LogIn",
    data() {
        return {
            // username: '',
            email: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'ورود' + ' | موبایل'
        window.scroll(0, 0);
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ""
            this.$store.commit('setIsLoading', true)
            localStorage.removeItem("token")

            const formData = {
                // username: this.username,
                password: this.password,
                email: this.email,
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    //console.log("response.data=",response.data)
                    //console.log("token=",token)

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = "Token" + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/'
                    notify({
                            title: "خوش آمدید",
                            type: "success",
                            });
                    this.$store.commit('setIsLoading', false)
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${error.response.data[property]}`)
                            console.log(this.errors)
                            console.log(JSON.stringify(error))
                        }
                    } else {
                        this.errors.push('Something went wrong. please try again')

                        console.log(JSON.stringify(error))
                    }
                })
                this.$store.commit('setIsLoading', false)
        },

        login() {
            googleSdkLoaded(google => {
                google.accounts.oauth2
                    .initCodeClient({
                        client_id:
                            "419616523969-cp852cneehq9fvj7ppbegpq128222mk6.apps.googleusercontent.com",
                        scope: "email profile openid",
                        redirect_uri: "http://localhost:4000/auth/callback",
                        callback: response => {
                            if (response.code) {
                                //this.sendCodeToBackend(response.code);
                                console.log("===============")
                                console.log(response.code);
                            }
                        }
                    })
                    .requestCode();
            });
        },

    },
}
</script>


<style>
@import "@/assets/css/login.css"
</style>