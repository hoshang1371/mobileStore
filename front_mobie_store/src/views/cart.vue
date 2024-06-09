<template>
    <div class="titleUp">
        <h2>سبد خرید</h2>
    </div>
    <div class="order">
        <table>
                <tr>
                    <th>تصویر</th>
                    <th>نام</th>
                    <th>تعداد</th>
                    <th>قیمت هر عدد</th>
                    <th>مجموع</th>
                </tr>
                <tr>
                    <td><img src="../assets/images/popup.jpg" alt=""></td>
                    <td>
                        <div>
                            <a href="">هدفون</a>
                            <span>هدفون می باشد </span>
                        </div>
                    </td>
                    
                    <td style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    ">
                        <div class="number">
                            <input type="text" id="numberProduct" name="first_name" class="toPe" @keyup="KeyUpFunction($event)" v-model="number">
                            <a class="up">
                                <div class='BCup' @click="BCupClick()">+</div>
                                <div class='BCdown' @click="BCdownClick()">-</div>
                            </a>
                        </div>

                        <div class="orderDetail_remove">
                            <svg 
                            xmlns="http://www.w3.org/2000/svg" id="delete" x="0" y="0" version="1.1" viewBox="0 0 29 29" xml:space="preserve">
                                <path d="M19.795 27H9.205a2.99 2.99 0 0 1-2.985-2.702L4.505 7.099A.998.998 0 0 1 5.5 6h18a1 1 0 0 1 .995 1.099L22.78 24.297A2.991 2.991 0 0 1 19.795 27zM6.604 8 8.21 24.099a.998.998 0 0 0 .995.901h10.59a.998.998 0 0 0 .995-.901L22.396 8H6.604z"></path><path d="M26 8H3a1 1 0 1 1 0-2h23a1 1 0 1 1 0 2zM14.5 23a1 1 0 0 1-1-1V11a1 1 0 1 1 2 0v11a1 1 0 0 1-1 1zM10.999 23a1 1 0 0 1-.995-.91l-1-11a1 1 0 0 1 .905-1.086 1.003 1.003 0 0 1 1.087.906l1 11a1 1 0 0 1-.997 1.09zM18.001 23a1 1 0 0 1-.997-1.09l1-11c.051-.55.531-.946 1.087-.906a1 1 0 0 1 .905 1.086l-1 11a1 1 0 0 1-.995.91z"></path><path d="M19 8h-9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1zm-8-2h7V4h-7v2z"></path>
                            </svg>
                        </div>
                    </td>

                    <td>
                        <!-- !takhfif lahaz shavad -->
                        <p>۱۰۰۰۰ ريال</p>
                    </td>

                    <td>
                        <p>۱۰۰۰۰ ريال</p>
                    </td>
                </tr>
            </table>
            
    </div>
</template>


<script>
import axios from 'axios'
export default{
    name: 'Cart',
    data() {
        return {
            number: "۱",

        }
    },
    mounted() {
        document.title = "سبد خرید"
    },
    methods: {
        BCupClick() {
            this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) + 1).toString())
        },
        BCdownClick() {
            if (parseInt(this.toEnglishDigit(this.number)) > 0)
                this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) - 1).toString())
        },
        
        toEnglishDigit(replaceString) {
            var find = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
            var replace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
            // console.log("digit")
            // var replaceString = this;
            // console.log(replaceString)
            var regex;
            for (var i = 0; i < find.length; i++) {
                regex = new RegExp(find[i], "g");
                replaceString = replaceString.replace(regex, replace[i]);
            }
            return replaceString;
        },
        toPersinaDigit(digit) {
            var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
            return digit.replace(/[0-9]/g, function (w) { return id[+w] });
        },
        KeyUpFunction(k) {
            // console.log(k)
            // console.log(k.key)
            // console.log(this.number)
            // # inja eshtebah ast
            if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
                let en_number = this.number;

                let number = this.toEnglishDigit(en_number);
                let number_buffer = parseInt(number, 10);
                number = number_buffer.toString();
                // console.log(number)
                if (isNaN(number))
                    number = "0";
                this.number = (this.toPersinaDigit(number));
            }
            else {
                this.number = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.number)).toString()));
            }
        },
    },
}
</script>

<style>
@import "@/assets/css/cart.css"
</style>
