<template>
    <li class="glide__slide">
        <div class="hero__center">
            <div class="hero__left">
                <span>{{ sliderUpp.title }}</span>
                <h1>{{ sliderUpp.description1 }}</h1>
                <p>{{ sliderUpp.description2 }}</p>
                <a href="#"><button class="hero__btn">خرید</button></a>
            </div>

            <div class="hero__right">
                <div class="hero__img-container">
                    <img :src="sliderUpp.get_image_sliderUp" alt="" class="banner_01" />
                </div>
            </div>
        </div>
    </li>
</template>

<script>
export default {
    name: 'sliderUpBox',
    props: {
        sliderUpp: Object,
    }
}
</script>