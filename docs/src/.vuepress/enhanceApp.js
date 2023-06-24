/**
 * Client app enhancement file.
 *
 * https://v1.vuepress.vuejs.org/guide/basic-config.html#app-level-enhancements
 */

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
// const axios = require('axios');
// // import axios from 'axios';
// import VueAxios from 'vue-axios'
//
//
// axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend


export default ({
  Vue, // the version of Vue being used in the VuePress app
  options, // the options for the root Vue instance
  router, // the router instance for the app
  siteData // site metadata
}) => {
  Vue.use(BootstrapVue);
  Vue.use(IconsPlugin);
  // Vue.use(VueAxios, axios);
}
