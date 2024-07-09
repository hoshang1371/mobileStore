<template>
    <div>
        <div class="sendForm">
            <div>
                <label>استان<span>*</span></label>
                <select  v-model="formData.ostan"  @change="onChangeOstan($event)">
                    <option v-for="(ostan , index) in ostanha" :key="index">{{ostan}}</option>
                </select>
            </div>
            <div>
                <label>شهر<span>*</span></label>
                <select v-model="formData.shahr">
                    <option v-for="(shahr , index) in shahrha" :key="index">{{shahr}}</option>
                </select>
            </div>
            <div>
                <label>کد پستی<span>*</span></label>
                <input @keyup="KeyUpFunctionPostCode($event)" v-model="formData.postCode" type="text" placeholder="کد پستی">
            </div>
            <div>
                <label>آدرس پستی<span>*</span></label>
                <textarea v-model="formData.address" name="" id="" cols="50" rows="10" placeholder="آدرس پستی"></textarea>
            </div>
            <!-- @click.prevent -->
             <div>
                 <button>ادامه</button>
             </div>
        </div>

    </div>
</template>

<script>
import mixin  from "../mixins.js"
import axios from 'axios'

export default{
    name: "postInfo",
    mixins: [ mixin ],
    data (){
        return{    
            // number: "", 
            ostanha: [
                // "آذربایجان شرقی",
                // "آذربایجان غربی",
                // "اردبیل",
                // "اصفهان",
                // "البرز",
                // "ایلام",
                // "بوشهر",
                // "تهران",
                // "چهارمحال و بختیاری",
                // "خراسان جنوبی",
                // "خراسان رضوی",
                // "خراسان شمالی",
                // "خوزستان",
                // "زنجان",
                // "سمنان",
                // "سیستان و بلوچستان",
                // "فارس",
                // "قزوین",
                // "قم",
                // "کردستان",
                // "کرمان",
                // "کرمانشاه",
                // "کهگیلویه وبویراحمد",
                // "گلستان",
                // "گیلان",
                // "لرستان",
                // "مازندران",
                // "مرکزی",
                // "هرمزگان",
                // "همدان",
                // "یزد"
                ],
            shahrha: [
                // "بیرجند",
                // "فردوس",
                // "طبس",
                // "قائنات",
                // "نهبندان",
                // "سربیشه",
                // "درمیان",
                // "سرایان",
                // "بشرویه",
                // "زیرکوه",
                // "خوسف",
            ],
            formData:{
                ostan:"خراسان جنوبی",
                shahr:"بیرجند",
                postCode: "",
                address: ""
            }

        }
    },
    mounted() {
        this.getAllOstan()
    },
    methods: {
        KeyUpFunctionPostCode(k) {
            if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
            let en_number = this.formData.postCode;

            let number = this.toEnglishDigit(en_number);
            let number_buffer = parseInt(number, 10);
            number = number_buffer.toString();
            // console.log(number)
            if (isNaN(number))
                number = "0";
            this.formData.postCode = (this.toPersinaDigit(number));
            }
            else {
            this.formData.postCode = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.formData.postCode)).toString()));
            }
        },

        async getAllOstan(event){
            console.log('https://iran-locations-api.ir/api/v1/fa/states')
            await axios
                .get("https://iran-locations-api.ir/api/v1/fa/states")
                .then(response => {
                    // console.log(response.data)
                    var ostans = response.data
                    for(var ostan in ostans){
                        // console.log(ostans[ostan].name)
                        this.ostanha.push(ostans[ostan].name);
                    }
                    // console.log(this.ostanha[0])
                    this.formData.ostan=this.ostanha[0]
                    this.getFirstShahr(this.formData.ostan);

                })
        },

        async getFirstShahr(event) {
            var link =`https://iran-locations-api.ir/api/v1/fa/cities?state=${event}`
            
            await axios
                .get(link)
                .then(response => {
                    // console.log(response.data[0].cities)
                    var cities =response.data[0].cities
                    this.shahrha =[]
                    for(var city in cities){
                        this.shahrha.push(cities[city].name)
                    }
                    this.formData.shahr = this.shahrha[0]

                })
        },
        async onChangeOstan(event) {
            var link =`https://iran-locations-api.ir/api/v1/fa/cities?state=${event.target.value}`
            
            await axios
                .get(link)
                .then(response => {
                    // console.log(response.data[0].cities)
                    var cities =response.data[0].cities
                    this.shahrha =[]
                    for(var city in cities){
                        this.shahrha.push(cities[city].name)
                    }
                    this.formData.shahr = this.shahrha[0]

                })
        },
    },


}
</script>


<style>
@import "@/assets/css/postInfo.css"
</style>