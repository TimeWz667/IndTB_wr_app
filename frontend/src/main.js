import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend

app.mount("#app");