<template>
    <div class="orderDetails_container">
        <div class="orderDetail_img">
            <!-- <img src="../assets/images/products/giorgio-trovato-K62u25Jk6vo-unsplash.jpg" alt=""> -->
            <img :src="orderDetail.product.get_thumbnail" alt="">
        </div>
        <div class="orderDetail_title">
            <a href=""> {{ orderDetail.product.title }} </a>
            <div>
                <div class="price">
                    <!-- <p class="priceOff">{{ orderDetail.product.price }} ريال<</p> -->
                    <p >{{ price }} ريال</p>
                    <!-- <p v-if="orderDetail.product.priceOff != null"> {{ orderDetail.product.priceOff }} ريال</p> -->
                </div>
                <div class="orderDetail_count">{{ count }}x</div>
            </div>
        </div>
        <div class="orderDetail_remove">
            <svg 
            @click="removeThisItem(orderDetail.id)"
            xmlns="http://www.w3.org/2000/svg" id="delete" x="0" y="0" version="1.1" viewBox="0 0 29 29" xml:space="preserve">
                <path d="M19.795 27H9.205a2.99 2.99 0 0 1-2.985-2.702L4.505 7.099A.998.998 0 0 1 5.5 6h18a1 1 0 0 1 .995 1.099L22.78 24.297A2.991 2.991 0 0 1 19.795 27zM6.604 8 8.21 24.099a.998.998 0 0 0 .995.901h10.59a.998.998 0 0 0 .995-.901L22.396 8H6.604z"></path><path d="M26 8H3a1 1 0 1 1 0-2h23a1 1 0 1 1 0 2zM14.5 23a1 1 0 0 1-1-1V11a1 1 0 1 1 2 0v11a1 1 0 0 1-1 1zM10.999 23a1 1 0 0 1-.995-.91l-1-11a1 1 0 0 1 .905-1.086 1.003 1.003 0 0 1 1.087.906l1 11a1 1 0 0 1-.997 1.09zM18.001 23a1 1 0 0 1-.997-1.09l1-11c.051-.55.531-.946 1.087-.906a1 1 0 0 1 .905 1.086l-1 11a1 1 0 0 1-.995.91z"></path><path d="M19 8h-9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1zm-8-2h7V4h-7v2z"></path>
            </svg>
        </div>
    </div>
</template>


<script>
    import axios from 'axios';

    import { useNotification } from "@kyvg/vue3-notification";
    const { notify } = useNotification()

export default {

    name: 'orderDetails_component',
    props: {
        orderDetail: Object,
    },
    data() {
        return {
            price:'',
            count:'',
        }
    },
    mounted() {
        // console.log(this.orderDetail.product.title)
        // this.price = toPersinaDigit(this.orderDetail.price)
        // console.log(this.price)
        this.setDetail()
    },
    methods: {
        toPersinaDigit(digit) {
            var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
            return digit.replace(/[0-9]/g, function (w) { return id[+w] });
        },
        setDetail(){
            this.price = this.toPersinaDigit(parseInt(this.orderDetail.price).toString())
            this.count = this.toPersinaDigit(parseInt(this.orderDetail.count).toString())
        },

        async removeThisItem(id) {
            this.$store.commit('setIsLoading', true)

            await axios
                .delete(`/order/Delete_product_orderDetail/${id}/`)
                .then(response => {

                    if (response.status == 204) {
                        this.$emit("remove")
                    }

                    notify({
                            title: " .محصول از سبد خرید شما حذف شد ",
                            type: "success",
                            });

                    this.$store.commit('setIsLoading', false)

                })
                .catch((err) => {
                    notify({
                        title: "مشکلی بوجود امده است",
                        type: "warn",
                    });    
                })
        },

        // removeItem(index){
        //     this.comment.replies.splice(index,1);
        //     console.log(this.orderDetail.id)
        // }
    },
}
</script>