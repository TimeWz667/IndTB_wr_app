<template>
    <div>
        <p>{{locations}}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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
