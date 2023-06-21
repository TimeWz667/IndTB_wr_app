<template>
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
    <div class="row">
        <div class="col-md-4">
            <q-inputs
                    :IntvForm="intvs"
                    :locations="locations"></q-inputs>
        </div>
        <div class="col-md-8">
            <q-trends
                    :baseline="baseline"
                    :intervention="intervention"></q-trends>
        </div>
    </div>




</template>

<script>
import QInputs from './components/QInputs.vue'
import QTrends from './components/QTrends.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
      QInputs,
      QTrends
  },
  data() {
    return {
        baseline: [],
        intervention: [],
        locations: [],
        intvs: []
    }
  },
  methods: {
      get_locations() {
          return axios.get("/locs/").then((res) => {
              this.locations = res.data;
          })
              .catch((error) => {
                  console.error(error);
              });
      },
      get_intvform() {
          return axios.get("/intv/").then((res) => {
              this.intvs = res.data;
          })
            .catch((error) => {
                console.error(error);
            });


      },
      get_baseline() {
          return axios.get("/run/India/").then((res) => {
              this.baseline = res.data;
          })
              .catch((error) => {
                  console.error(error);
              });
      },
      get_intervention(intv) {
          return axios.put("/run/India/", intv).then((res) => {
              this.intervention = res.data;
          })
              .catch((error) => {
                  console.error(error);
              });
      }
  },
    mounted() {
      this.get_locations();
      this.get_intvform();
      this.get_baseline();
      this.get_intervention({BetaRed: 0})
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
