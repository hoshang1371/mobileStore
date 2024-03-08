<template>
    <div class="comment_section">
        <div class="commented-user">
            <h5 class="">{{ comment.user }}</h5>
            <span class="dot"></span>
            <!-- <span class="">5 ساعت قبل</span> -->
            <div>
                <span v-if="comment.time_calc.years != '۰'" class="">{{ comment.time_calc.years }} سال قبل</span>
                <span v-if="comment.time_calc.days != '۰'" class="">{{ comment.time_calc.days }} روز قبل</span>
                <span v-if="comment.time_calc.hours != '۰'" class="">{{ comment.time_calc.hours }} ساعت قبل</span>
                <span v-if="comment.time_calc.minutes != '۰'" class="">{{ comment.time_calc.minutes }} دقیقه قبل</span>
                <span v-if="comment.time_calc.seconds != '۰'" class="">{{ comment.time_calc.seconds }} ثانیه قبل</span>
            </div>
        </div>
        <div class="comment-text-sm">
            <span>{{ comment.text }}</span>
        </div>
        <div class="reply-section">
            <div class="voting-icons">

                <svg v-if="comment.is_liked == true" @click="$store.state.isAuthenticated ? setLike(comment.id) : ''"
                    fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M1863.059 1016.47c0-124.574-101.308-225.882-225.883-225.882H1203.37c-19.651 0-37.044-9.374-47.66-25.863-10.391-16.15-11.86-35.577-3.84-53.196 54.776-121.073 94.87-247.115 119.378-374.513 15.925-83.576-5.873-169.072-60.085-234.578C1157.29 37.384 1078.005 0 993.751 0H846.588v56.47c0 254.457-155.068 473.224-285.063 612.029-72.734 77.477-176.98 122.09-285.967 122.09H56v734.117C56 1742.682 233.318 1920 451.294 1920h960c124.574 0 225.882-101.308 225.882-225.882 0-46.42-14.117-89.676-38.174-125.59 87.869-30.947 151.116-114.862 151.116-213.234 0-46.419-14.118-89.675-38.174-125.59 87.868-30.946 151.115-114.862 151.115-213.233"
                        fill-rule="evenodd" />
                </svg>
                <svg v-if="comment.is_liked == false" @click="$store.state.isAuthenticated ? setLike(comment.id) : ''"
                    fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M1637.176 1129.412h-112.94v112.94c62.23 0 112.94 50.599 112.94 112.942 0 62.344-50.71 112.941-112.94 112.941h-112.942v112.941c62.23 0 112.941 50.598 112.941 112.942 0 62.343-50.71 112.94-112.94 112.94h-960c-155.634 0-282.354-126.606-282.354-282.352V903.529h106.617c140.16 0 274.334-57.6 368.3-157.778C778.486 602.089 937.28 379.256 957.385 112.94h36.367c50.484 0 98.033 22.363 130.334 61.44 32.64 39.53 45.854 91.144 36.14 141.515-22.7 118.589-60.197 236.048-111.246 349.102-23.83 52.517-19.313 112.602 11.746 160.94 31.397 48.566 84.706 77.591 142.644 77.591h433.807c62.231 0 112.942 50.598 112.942 112.942 0 62.343-50.71 112.94-112.942 112.94m225.883-112.94c0-124.575-101.308-225.883-225.883-225.883H1203.37c-19.651 0-37.044-9.374-47.66-25.863-10.391-16.15-11.86-35.577-3.84-53.196 54.663-121.073 94.87-247.115 119.378-374.513 15.925-83.576-5.873-169.072-60.085-234.578C1157.29 37.384 1078.005 0 993.751 0H846.588v56.47c0 254.457-155.068 473.224-285.063 612.029-72.734 77.477-176.98 122.09-285.967 122.09H56v734.117C56 1742.682 233.318 1920 451.294 1920h960c124.574 0 225.882-101.308 225.882-225.882 0-46.42-14.117-89.676-38.174-125.59 87.869-30.947 151.116-114.862 151.116-213.234 0-46.419-14.118-89.675-38.174-125.59 87.868-30.946 151.115-114.862 151.115-213.233"
                        fill-rule="evenodd" />
                </svg>
                <span class="mr-1">{{ comment.like_comment_calc }}</span>
                <span class="dot mr-1"></span>
                <h6 class="" @click="$store.state.isAuthenticated ? toggleCustomerComment() : loginCustomerComment()">پاسخ</h6>

                <!-- TODO: add remove for user -->
                <h6 class="removeComment" v-if="comment.is_user" @click="removeComment(comment.id)">حذف</h6>
            </div>
        </div>

        <customerComentPost v-if="showCommentPost == true" v-bind:key="comment.id" v-bind:customerComment="comment" />

        <commentSection @remove="removeItem(index)" v-if="comment.replies.length != 0" v-for="(comment, index) in comment.replies" v-bind:key="comment.id"
            v-bind:comment="comment" />

    </div>
</template>



<script>

import axios from 'axios';

import customerComentPost from '@/components/customerComentPost.vue'
import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()
export default {
    name: 'commentSection',
    components: {
        customerComentPost,
    },
    props: {
        comment: Object,
    },
    data() {
        return {
            showCommentPost : false,
        }
    },
    mounted() {
        // console.log(this.comment.id,this.comment.text,this.comment.is_liked)
        // this.setComment()
    },
    setup(props, { root }) {
        const close = () => {
            root.$destroy();
            root.$el.parentNode.removeChild(root.$el);
        };
        return { close };
    },
    methods: {
        async setLike(id) {
            // console.log(id);
            // const product_id = this.$route.params.product_id
            // console.log(product_id);

            this.$store.commit('setIsLoading', true)
            //             {
            //     "like": false,
            //     "numberLike": 1
            // }
            await axios
                .post(`api/v1/GetLikesCustomerComment/${id}`)
                .then(response => {
                    // console.log(response.status)
                    this.comment.like_comment_calc = response.data["numberLike"]
                    this.comment.is_liked = response.data["like"]

                    this.$store.commit('setIsLoading', false)
                })
        },

        async removeComment(id) {
            // console.log(id)
            this.$store.commit('setIsLoading', true)

            await axios
                .delete(`api/v1/DeleteCustomerComment/${id}`)
                .then(response => {
                    console.log(response)
                    console.log(response.status)

                    if (response.status == 204) {
                        this.$emit("remove")
                    }
                    this.$store.commit('setIsLoading', false)
                })
        },
        removeItem(index){

            this.comment.replies.splice(index,1);
        },

        toggleCustomerComment()
        {
            this.showCommentPost = !this.showCommentPost;
        },

        loginCustomerComment()
        {
            notify({
                        title: "لطفا وارد حساب کاربری خود شوید",
                        type: "warn",
                    });        }
        // setComment() {
        //     // console.log(this.comment.replies.length)
        //     // console.log(typeof(this.comment.replies))
        //     console.log((this.comment.time_calc.days))
        //     // console.log(this.comment.parent)
        //     // console.log(this.comment.time_calc)
        //     // console.log(this.comment.time_calc.years != '۰' )
        // }
    }
}
</script>