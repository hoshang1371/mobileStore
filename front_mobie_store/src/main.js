import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/style.css'

import Notifications from '@kyvg/vue3-notification'


import VueImageZoomer from 'vue-image-zoomer'
import 'vue-image-zoomer/dist/style.css';
// import './assets/js/products.js'
// import './assets/js/slider.js'
import axios from 'axios'
// import VueClientRecaptcha from 'vue-client-recaptcha/dist/vue-client-recaptcha.es'
axios.defaults.baseURL = 'http://127.0.0.1:8000/'


import OpenLayersMap from "vue3-openlayers";
import "vue3-openlayers/styles.css"; 

// import VueMyToasts from 'vue-my-toasts'
// import 'vue-my-toasts/dist/vue-my-toasts.css'
// import YourToastComponent from '~/components/toasts/YourToastComponent'
// createApp(App).use(store).use(router,OpenLayersMap).mount('#app')
const app= createApp(App).use(store).use(router,OpenLayersMap).use(Notifications).use(VueImageZoomer);

app.mount('#app')
// app.use(OpenLayersMap /* options */);

// app.mount("#app");
// import './assets/js/index.js'

// import Vue from "vue";

// Vue.config.productionTip = false;

// new Vue({
//   render: h => h(App)
// }).$mount("#app");

