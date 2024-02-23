<template>
    <div class="limiter">

        <div class="container-login100">
            <div class="wrap p-t-50 p-b-90">
                <form @submit.prevent="submitForm" class="login-form">
                    <span class="login100-form-title p-b-51"> فراموشی رمز </span>

                    <div class="wrap-input100 validate-input m-b-16" data-validate="Username is required">
                        <input class="input100" type="text" name="email" placeholder="ایمیل" v-model="email">
                        <span class="focus-input100"></span>
                    </div>



                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="container-login100-form-btn m-t-17">
                        <button class="login100-form-btn">
                            ارسال لینک بازیابی رمز
                        </button>
                    </div>
                    <div class="createAccount">
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

// import { notify } from "@kyvg/vue3-notification";
import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()

export default {
    name: "sendForgetPass",
    data() {
        return {
            email: '',
            errors: []
        }
    },
    mounted() {
        document.title = ' فراموشی رمز ' + ' | موبایل'
        window.scroll(0, 0);
        // this.$notify("Hello user!");
        // this.$notify({
        //     title: "Important message",
        //     text: "Hello user!",
        // });
        // notify({
        //     title: "Authorization",
        //     text: "You have been logged in!",
        // });
        // notify({
        //     title: "لینک بازیابی ارسال شد",
        //     type: "success",
        //     // duration: 10000,
        // });
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const formData = {
                email: this.email,
            }

            await axios
                .post("/api/v1/users/reset_password/", formData)
                .then(response => {

                    // console.log("response.data=", response.data)
                    //console.log("token=",token)

                    const toPath = this.$route.query.to || '/'
                    notify({
                        title: "لینک بازیابی ارسال شد",
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
                    this.$store.commit('setIsLoading', false)
                })
        },
    }
}
</script>