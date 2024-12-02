<template>
    <div class="Methode">
        <div class="container">
            <div class="sendMethode">
                <div><a>روش ارسال</a></div>
                <div>
                    <input type="radio" id="one" value="پست پیشتاز" v-model="formData.send" />
                    <label for="one">پست پیشتاز</label>
                </div>
    
                <div>
                    <input type="radio" id="two" value="تیپاکس" v-model="formData.send" />
                    <label for="two">تیپاکس</label>
                </div>
    
                <div>
                    <input type="radio" id="tree" value="باربری" v-model="formData.send" />
                    <label for="tree">باربری</label>
                </div>
    
            </div>
            <div class="peymentMethode">
                <div><a>روش پرداخت</a></div>
                <div>
                    <input type="radio" id="one" value="ثبت سفارش (پیش فاکتور)" v-model="formData.peyment" />
                    <label for="one">ثبت سفارش (پیش فاکتور)</label>
                </div>
    
                <div>
                    <input type="radio" id="two" value="پرداخت از طریق درگاه پرداخت اینترنتی" v-model="formData.peyment" />
                    <label for="two">پرداخت از طریق درگاه پرداخت اینترنتی</label>
                </div>
                
            </div>
        </div>
        <div class="rull">
            <input type="checkbox" id="checkbox" v-model="formData.rull" />
            <label for="checkbox">من با <a @click="showRull()">شرایط خدمات</a> موافقم و بی قید و شرط به آن‌ها پایبندم </label>
        </div>
        <div>
            <button @click="send()">ادامه</button>
        </div>

        <div class="rullAndTerm hide_rullAndTerm">
            <div class="rullAndTerm_content">
                <div class="rullAndTerm_close">
                    <svg class="svg-icon"
                    style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;"
                    viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M810.65984 170.65984q18.3296 0 30.49472 12.16512t12.16512 30.49472q0 18.00192-12.32896 30.33088l-268.67712 268.32896 268.67712 268.32896q12.32896 12.32896 12.32896 30.33088 0 18.3296-12.16512 30.49472t-30.49472 12.16512q-18.00192 0-30.33088-12.32896l-268.32896-268.67712-268.32896 268.67712q-12.32896 12.32896-30.33088 12.32896-18.3296 0-30.49472-12.16512t-12.16512-30.49472q0-18.00192 12.32896-30.33088l268.67712-268.32896-268.67712-268.32896q-12.32896-12.32896-12.32896-30.33088 0-18.3296 12.16512-30.49472t30.49472-12.16512q18.00192 0 30.33088 12.32896l268.32896 268.67712 268.32896-268.67712q12.32896-12.32896 30.33088-12.32896z" />
                </svg>
                </div>

                <div class="rullAndTerm_right">
                    <div class="right_content">
                        <h2>&nbsp; قوانین و مقررات &nbsp;</h2>
                        <p>
                            رضایت و لذت از خرید، سرلوحه تعامل با مشتریان در فروشگاه تخصصی برق و الکترونیک بوده و این مجموعه همواره می‌کوشد تا سفارش‌ها به بهترین نحو ممکن به دست خریداران محترم برسد. مطالعه دقیق موارد زیر جهت استفاده درست و بهینه از خدمات و کالاهای فروشگاه تخصصی برق و الکترونیک مارا دررسیدن به این هدف یاری می‌کند.
                            ورود کاربران به وب‌سایت فروشگاه هنگام استفاده از پروفایل شخصی، به معنای آگاه بودن و پذیرفتن شرایط و قوانین فروشگاه تخصصی برق و الکترونیک است. توجه داشته باشید که ثبت هرگونه سفارش و یا تراکنش مالی در هر زمان به معنی پذیرفتن کامل کلیه شرایط و قوانین این فروشگاه از سوی کاربر است.
                             
                            <h1>
                                قوانین عمومی
                            </h1>
                            توجه داشته باشید کلیه اصول و رویه‏‌های فروشگاه تخصصی برق و الکترونیک منطبق با قوانین جمهوری اسلامی ایران، قانون تجارت الکترونیک و قانون حمایت از حقوق مصرف‌کننده است و متعاقباً کاربر نیز موظف به رعایت قوانین مرتبط با کاربر است. درصورتی‌که هر زمان در قوانین مندرج، رویه‏‌ها و شرایط فروش این فروشگاه تغییراتی ایجاد شود، در همین صفحه منتشر و به‌روزرسانی می‌شود و شما توافق می‏‌کنید که استفاده مستمر شما از سایت به معنی پذیرش هرگونه تغییر است.
                             <h1>
                                 تعریف مشتری یا کاربر
                             </h1>
                            مشتری یا کاربر به شخصی گفته می‌شود که با اطلاعات کاربری خود که در فرم ثبت‌نام درج کرده است، به ثبت سفارش یا هرگونه استفاده از خدمات فروشگاه اقدام نماید.
                            <h1>
                                ثبت اطلاعات مشتریان
                            </h1>
                            مشتری موظف است در هنگام ثبت‌نام و یا ثبت سفارش، مشخصات شخصی شامل نام و نام خانوادگی، شماره تلفن تماس (تلفن همراه و تلفن ثابت با پیش شماره شهرستان) و آدرس و کد پستی کامل خود را با کیبورد فارسی به‌دقت وارد کند. همچنین ایمیل و شماره تماس ثبت‌شده می‌بایست معتبر باشد تا بتوان در مواقع لزوم با مشتری تماس گرفت. بدیهی است درصورتی‌که اطلاعات مندرج در حساب کاربری مشتری صحیح نباشد، ‌مسئولیت هرگونه ناهماهنگی درروند ارسال سفارش، شامل (و نه محدود به) تأخیر، گم‌شدن و یا برگشت سفارش بر عهده مشتری بوده و هرگونه ضرر و زیان احتمالی، متوجه کاربر خواهد بود. برای جلوگیری از هرگونه موارد کلاهبرداری، شماره تلفن مشتری به هنگام ثبت نام با ارسال کد شناسایی احراز می گردد.
                            خاطرنشان می‌گردد این فروشگاه به اطلاعات خصوصی اشخاصى که از خدمات سایت استفاده می‏‌کنند، احترام گذاشته و از آن محافظت می‏‌کند.
                            <h1>
                                پست پیشتاز:
                            </h1>
                            زمان حمل اعلامی شرکت پست در این روش ۱ تا ۳ روز است که برای مراکز استان ۱ تا ۲ روز، ‌شهرستان‌های بزرگ ۲ تا ۳ روز و شهرهای کوچک و روستاها ۳ روز می‌باشد. هرگونه تأخیر در این زمان‌بندی بر عهده شرکت پست بوده و خارج از مسئولیت فروشگاه می‌باشد. مرسولات ارسالی به این روش تا سقف 15میلیون ریال بیمه می شوند. مرسولات ارسالی با پست از «سامانه رهگیری مرسولات پستی» قابل رهگیری می باشند.
                            پست پیشتاز با بیمه:
                            این روش همانند پست پیشتاز می باشد، با این تفاوت که می توانید سفارشات خود را بر اساس مبلغ سفارش تا سقف مشخص بیمه نمایید و در صورت بروز مشکل برای مرسوله، غرامت خود را از شرکت پست مطالبه نمایید. این روش برای سفارشات با ارزش بیش از ۱۵ میلیون ریال فعال بوده و هزینه بیمه مرسوله به صورت خودکار بر اساس ارزش سفارش محاسبه شده و در قسمت هزینه ارسال نمایش داده شده و به همراه مبلغ سفارش اخذ می‌گردد. این روش ارسال مشمول ارسال رایگان نمی‌گردد. دقت فرمایید برای دریافت غرامت در صورت وجود هرگونه مشکل در بسته، می بایست در لحظه تحویل و نزد مامور پست بسته را بررسی و مشکلات احتمالی را صورتجلسه کنید.
                          تمامی شرایط و قوانین مندرج، در شرایط عادی قابل‌اجرا است و در صورت بروز هرگونه از موارد قوه قهریه (مانند و نه محدود به: سیل، زلزله، آشوب و ...) فروشگاه هیچ‌گونه مسئولیتی ندارد.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { closestSquaredDistanceXY } from 'ol/extent';
import axios from 'axios'
import { useNotification } from "@kyvg/vue3-notification";

const { notify } = useNotification()
export default{
    name:"peymentAndSendMethode",
    props: {
        orderDetails: Object,
    },
    data() {
        return {
            formData:{
                Order_id:"",
                send:"",
                peyment:"",
                rull: false,
            }
        }
    },
    mounted() {
        const rullAndTerm = document.querySelector(".rullAndTerm")
        const rullAndTerm_close = document.querySelector(".rullAndTerm_close")

        if (rullAndTerm) {
            rullAndTerm_close.addEventListener("click", () => {
                rullAndTerm.classList.add("hide_rullAndTerm");
            })
        }
    },
    methods: {
        async send(){
            // console.log("ok")
            // console.log(this.orderDetails[0].order.id)
            this.formData.Order_id = this.orderDetails[0].order.id
            console.log(this.formData.rull)

            if(this.formData.rull == false)
                notify({
                            title: "قوانین و مقررات موافقت نشده است",
                            type: "warn",
                        });   
            else if(this.formData.rull == true)
                this.$store.commit('setIsLoading', true)
                await axios
                    .post('/post_information/peymentAndSendMethode', this.formData)
                    .then(response => {
                        // console.log(response.status)
                        console.log(response.data.code)
                        if( response.data.code == 1){
                            console.log("tamas")
                            this.$router.push("/finishNoCartPeyment")
                        }
                        //! toDO: edame be product list
                        this.$store.commit('setIsLoading', false)
                    })
                    .catch((err) => {
                        notify({
                            title: "مشکلی بوجود امده است",
                            type: "warn",
                        });    
                    })
            // console.log(this.formData.send) 
            // console.log(this.formData.peyment)
            // console.log(this.formData.rull)
        },  
        showRull(){
            console.log("showRull")
            const rullAndTerm = document.querySelector(".rullAndTerm")
            rullAndTerm.classList.remove("hide_rullAndTerm");
            
        }

    },
}
</script>
<style>
@import "@/assets/css/peymentAndSendMethode.css"
</style>