/*
==========================
Glide Js Carsousel
==========================
*/
const slider1 = document.getElementById('glide_1');
const slider2 = document.getElementById('glide_2');



/*
==========================
Hero
==========================
*/

if (slider1) {
    new Glide(slider1, {
        type: 'carsoual',
        startAt: 0,
        // autoplay: 3000,
        hoverpause: true,
        perView: 1,
        animationDuration: 800,
        animationTimingFunc: 'linear',
    }).mount();
}

/*
==========================
Latest Products
==========================
*/
if (slider2) {
    // console.log("kir khar")
    new Glide(slider2, {
        type: 'carsoual',
        startAt: 0,
        hoverpause: true,
        perView: 4,
        animationDuration: 800,
        animationTimingFunc: "ease-in-out",
        breakpoints: {
            1200: {
                perView: 3,
            },
            768: {
                perView: 2, 
            },
        },
    }).mount();
}
/*
==========================
Testimonial
==========================
*/
/*
==========================
News
==========================
*/