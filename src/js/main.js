import Vue from 'vue';
import App from './App.vue';
import Multiselect from "vue-multiselect";

Vue.component('multiselect', Multiselect)


/* eslint-disable no-new */
new Vue({
    el: '#app',
    components: { App },
    template: '<App/>',
});