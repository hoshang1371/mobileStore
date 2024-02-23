<template>
    <div class="activeEmail">
        <p>{{ res.massege }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "ActiveEmail",
    data() {
       return{
        res:"",
       }
    },
    mounted() {
        document.title = 'فعال سازی اکانت' + ' | موبایل'
        this.activateEmail();
        window.scroll(0, 0);
    },
    methods: {
        async activateEmail() {
            const uid = this.$route.params.uid
            const token = this.$route.params.token
            console.log("uid=",uid)
            console.log("token=",token)

            const formData = {
                    uid: uid,
                    token: token,
                }

            await axios
                .get(`/activate/${uid}/${token}`)
                .then(response =>{
                    this.res = response.data
                    console.log(this.res)
                })

        }
    }
}

</script>

<style>
@import "@/assets/css/activeEmail.css"
</style>