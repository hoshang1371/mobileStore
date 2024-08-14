<template>
    <div>
        <div class="content">
            <panelAdminRight/>
            <div class="container_left">
                <p v-if="comments.length==0">شما هیچ نظری ثبت نکرده اید.</p>
                <table>
                    <tr>
                        <th>نام کالا</th>
                        <th>متن نظر</th>
                    </tr>
                    <tr  v-for="(comment, index) in comments">
                        <td>
                            <div>
                                <a @click="toProductDitails(comment.CommentProduct.get_absolute_url)">{{comment.CommentProduct.title}}</a>
                            </div>
                        </td>
                        <td>
                            <div>
                                <h3>{{comment.text}}</h3>
                            </div>
                        </td>
                    </tr>
    
            </table>
            </div>

        </div>
    </div>
</template>

<script>
import panelAdminRight from '@/components/panelAdminRight.vue'

import mixin  from "../mixins.js"

import axios from 'axios';
import { useNotification } from "@kyvg/vue3-notification";
const { notify } = useNotification()
export default{
    name: "CommentsPanelAdmin",
    mixins: [ mixin ],
    components:{
        panelAdminRight,
    },
    data() {
        return {
            comments: [],
        }
    },
    mounted() {
        document.title = 'نظرات' + ' | موبایل'
        window.scroll(0, 0);
        this.getComments();
    },
    methods: {
        toProductDitails(link) {           
            this.$router.push(link)
        },
        async getComments() {
            axios
                .get("/api/v1/GetAllProductCustomerComment/")
                .then(response => {
                    this.$store.commit('setIsLoading', true)
                    this.comments = response.data
                    // console.log(this.comments)
                    for(let a in this.comments){
                        console.log(this.comments[a].CommentProduct.title)
                    }
                    // if(response.status == 200){
                    //     notify({
                    //     title: " رمز عبور تغییر کرد ",
                    //     type: "success",
                    //     });
                    // }
                    this.$store.commit('setIsLoading', false)   
                })
        },
    },
}
</script>

<style>
@import "@/assets/css/panelAdmin.css";
@import "@/assets/css/CommentsPanelAdmin.css";
</style>