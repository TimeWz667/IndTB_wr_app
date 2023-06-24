<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-4">
                <controller />
            </div>
            <div class="col-md-8">
                <trajectory />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Controller from "./controller.vue";
import Trajectory from "./trajectory.vue";


export default {
    components: {
        Controller,
        Trajectory
    },
    data() {
        return {
            locations: 'locations'
        }
    },
    methods: {
        async loadMeta() {
            this.locations = await axios.get('/locs').then(d => d.data);
        }
    },
    mounted() {
        this.loadMeta();
    }
}

</script>

<style scoped>
.read-the-docs {
    color: #888;
}
</style>
