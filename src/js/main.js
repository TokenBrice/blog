import Vue from 'vue';
import Filters from './App.vue';
import Multiselect from "vue-multiselect";

Vue.component('multiselect', Multiselect)


/* eslint-disable no-new */
const app = new Vue({
    el: '#app',
    components: { Filters },
    data() {
        return {}
    }
});