<template>
    <div class="container-fluid">
        <div class="row">
<!--            <div class="col-md-12">{{ IntvParsed }}</div>-->
            <div class="col-md-4">
                <controller
                  :Locations="Locations"
                  :IntvForm="IntvForm"
                  v-on:settings_update="updateSettings($event)"
                  v-on:intv_update="updateInterventions($event)"
                  v-on:intv_reset="resetInterventions($event)"
                ></controller>
            </div>
            <div class="col-md-8">
                <trajectory :Curr0="SimBaseline" :Curr1="SimIntv" :Year0="Settings.YearStart" :Year1="Settings.YearEnd"/>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import intvs from "../lists/interventions";
import Controller from "./controller.vue";
import Trajectory from "./trajectory.vue";


export default {
    components: {
        Controller,
        Trajectory
    },
    data() {
        const settings = { Location: "India", YearStart: 2022, YearEnd: 2030}
        const i0 = JSON.stringify(intvs);

        return {
            Settings: settings,
            Locations: ["India"],
            IntvForm: intvs,
            Intv0: i0,
            IntvCurr: i0,
            IntvParsed: {},
            SimBaseline: [],
            SimIntv: [],
            Keeps: {}
        }
    },
    methods: {
        async loadMeta() {
            this.Locations = await axios.get('/locs').then(d => d.data);
        },
        async runBaseline() {
            this.SimBaseline = await axios.get("/run/" + this.Settings.Location).then(d => d.data);
        },
        async runIntv(intv) {
            const i = this.parseInterventions(intv);
            this.IntvParsed = i;
            console.log(i);
            this.SimIntv = await axios.put("/run/" + this.Settings.Location, i).then(d => d.data);
        },
        updateSettings(evt) {
            const loc_changed = (evt.Location === this.Settings.Location);
            this.Settings = evt;

            if (loc_changed) {
                this.runBaseline();
                this.runIntv(this.IntvCurr);
            }
        },
        resetResults() {
            this.runBaseline();
            this.SimIntv = this.SimBaseline.map(d => d);
        },
        updateInterventions() {
            this.IntvCurr = JSON.stringify(this.IntvForm);
            this.runIntv(this.IntvCurr);
        },
        resetInterventions() {
            this.IntvForm = JSON.parse(this.Intv0);
        },
        parseInterventions(intv) {
            return JSON.parse(intv)
              .filter(d => d.Clicked)
              .reduce((prev, d) => {
                  prev[d.Name] = d.Pars
                    .reduce((collector, x) => {
                        switch(x.type) {
                            case "bool":
                                collector[x.name] = x.value;
                                break;
                            case "choice":
                                collector[x.name] = x.value;
                                break;
                            default:
                                collector[x.name] = +x.value;
                                break;

                        }
                        return collector;
                    }, {});
                  return prev;
              }, {});
        }
    },
    mounted() {
        this.loadMeta();
        this.resetResults();
    }
}
</script>

<style scoped>
.read-the-docs {
    color: #888;
}
</style>
