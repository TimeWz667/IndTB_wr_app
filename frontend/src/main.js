import { createApp } from 'vue'
import './style.css'
import axios from 'axios';
import PrimeVue from "primevue/config";
import App from './App.vue'


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend


const app = createApp(App);

app.use(PrimeVue)
    .mount('#app')
