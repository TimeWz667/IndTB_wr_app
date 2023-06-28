<template>
    <div class="row">
        <div class="col-md-6 card">
            <div class="card-header">
                <h5 class="card-title">Incidence</h5>
            </div>
            <div class="card-body">
                {{ Incidence }}
            </div>
        </div>
        <div class="col-md-6 card">
            <div class="card-header">
                <h5 class="card-title">Mortality</h5>
            </div>
            <div class="card-body">
                {{ Mortality }}
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "trajectory",
    props: {
        Curr0: {
            type: Array
        },
        Curr1: {
            type: Array
        },
        Year0: {
            type: Number,
            default: 2022
        },
        Year1: {
            type: Number,
            default: 2030
        }
    },
    watch: {
        Curr0() {
            this.updateData();
            this.updateFigure();
        },
        Curr1() {
            this.updateData();
            this.updateFigure();
        }
    },
    data() {
        return {
            Incidence: {
                Baseline: [],
                Intervention: []
            },
            Mortality: {
                Baseline: [],
                Intervention: []
            }
        }
    },
    methods: {
        updateData() {
            this.Incidence.Baseline = this.Curr0
                .filter(d => d.Year >= this.Year0)
                .filter(d => d.Year <= this.Year1)
                .map(d => {
                    return { 'Year': d.Year, 'M': d.IncR_M, 'L': d.IncR_L, 'U': d.IncR_U };
                })
            this.Mortality.Baseline = this.Curr0
                .filter(d => d.Year >= this.Year0)
                .filter(d => d.Year <= this.Year1)
                .map(d => {
                    return { 'Year': d.Year, 'M': d.MorR_M, 'L': d.MorR_L, 'U': d.MorR_U };
                })
        },
        updateFigure() {
            this.Incidence.Intervention = this.Curr1
                .filter(d => d.Year >= this.Year0)
                .filter(d => d.Year <= this.Year1)
                .map(d => {
                    return { 'Year': d.Year, 'M': d.IncR_M, 'L': d.IncR_L, 'U': d.IncR_U };
                })
            this.Mortality.Intervention = this.Curr1
                .filter(d => d.Year >= this.Year0)
                .filter(d => d.Year <= this.Year1)
                .map(d => {
                    return { 'Year': d.Year, 'M': d.MorR_M, 'L': d.MorR_L, 'U': d.MorR_U };
                })
        }
    },
    mounted() {
        this.updateData();
        this.updateFigure();
    }
}
</script>

<style scoped>

</style>