import { createApp } from 'vue'
import './style.css'
import axios from 'axios';
import App from './App.vue'

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend


const app = createApp(App);

app.mount('#app')
