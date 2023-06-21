<template>
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <h3>Baseline</h3>
  {{baseline}}

  <h3>Intervention</h3>
  {{intervention}}
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
    // HelloWorld
  },
    data() {
      return {
          baseline: [],
          intervention: []
      }
    },
  methods: {
      get_baseline() {
          return axios.get("/India/").then((res) => {
              this.baseline = res.data;
          })
              .catch((error) => {
                  console.error(error);
              });
      },
      get_intervention(intv) {
          return axios.put("/India/", intv).then((res) => {
              this.intervention = res.data;
          })
              .catch((error) => {
                  console.error(error);
              });
      }
  },
    mounted() {
      this.get_baseline();
      this.get_intervention({})
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
