<template>
    <div class="row">
        <div class="col-md-6 card">
            <div class="card-header">
                <h5 class="card-title">Incidence</h5>
            </div>
            <div class="card-body">
                <fig-plotly
                    :data="[Incidence.LU0, Incidence.LU1, Incidence.M0, Incidence.M1]"
                    :layout="layout_inc"
                    :options="options"
                ></fig-plotly>
            </div>
        </div>
        <div class="col-md-6 card">
            <div class="card-header">
                <h5 class="card-title">Mortality</h5>
            </div>
            <div class="card-body">
                <fig-plotly
                  :data="[Mortality.LU0, Mortality.LU1, Mortality.M0, Mortality.M1]"
                  :layout="layout_mor"
                  :options="options"
                ></fig-plotly>
            </div>
        </div>
    </div>
</template>
<script>
import FigPlotly from "./figs/FigPlotly.vue";


export default {
    name: "trajectory",
    components: {
        FigPlotly
    },
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
            this.update0();
        },
        Curr1() {
            this.update1();
        },
        Year0(yr0) {
            this.layout_inc.xaxis.range[0] = yr0
            this.layout_mor.xaxis.range[0] = yr0
        },
        Year1(yr1) {
            this.layout_inc.xaxis.range[1] = yr1
            this.layout_mor.xaxis.range[1] = yr1
        }
    },
    data() {
        return {
            Incidence: {
                Baseline: [],
                Intervention: [],
                M0: {
                    x: [],
                    y: [],
                    line: {color: "rgb(0,176,246)"},
                    mode: "lines",
                    name: "Baseline",
                    type: "scatter"
                },
                LU0: {
                    x: [],
                    y: [],
                    fill: "tozerox",
                    fillcolor: "rgba(0,176,246,0.2)",
                    line: {color: "transparent"},
                    name: "Baseline",
                    showlegend: false,
                    type: "scatter"
                },
                M1: {
                    x: [],
                    y: [],
                    line: {color: "rgb(231,107,243)"},
                    mode: "lines",
                    name: "Intervention",
                    type: "scatter"
                },
                LU1: {
                    x: [],
                    y: [],
                    fill: "tozerox",
                    fillcolor: "rgba(231,107,243, 0.2)",
                    line: {color: "transparent"},
                    name: "Intervention",
                    showlegend: false,
                    type: "scatter"
                }
            },
            Mortality: {
                Baseline: [],
                Intervention: [],
                M0: {
                    x: [],
                    y: [],
                    line: {color: "rgb(0,176,246)"},
                    mode: "lines",
                    name: "Baseline",
                    type: "scatter"
                },
                LU0: {
                    x: [],
                    y: [],
                    fill: "tozerox",
                    fillcolor: "rgba(0,176,246,0.2)",
                    line: {color: "transparent"},
                    name: "Baseline",
                    showlegend: false,
                    type: "scatter"
                },
                M1: {
                    x: [],
                    y: [],
                    line: {color: "rgb(231,107,243)"},
                    mode: "lines",
                    name: "Intervention",
                    type: "scatter"
                },
                LU1: {
                    x: [],
                    y: [],
                    fill: "tozerox",
                    fillcolor: "rgba(231,107,243, 0.2)",
                    line: {color: "transparent"},
                    name: "Intervention",
                    showlegend: false,
                    type: "scatter"
                }
            },
            layout_inc:{
                showlegend: false,
                xaxis: {
                    range: [2022, 2030],
                    showgrid: true,
                    showline: false,
                    showticklabels: true,
                    tickcolor: "rgb(127,127,127)",
                    ticks: "outside",
                    zeroline: false
                },
                yaxis: {
                    range: [0, 200],
                    gridcolor: "rgb(255,255,255)",
                    showgrid: true,
                    showline: false,
                    showticklabels: true,
                    tickcolor: "rgb(127,127,127)",
                    ticks: "outside",
                    zeroline: true
                }
            },
            layout_mor:{
                showlegend: false,
                xaxis: {
                    range: [2022, 2030],
                    showgrid: true,
                    showline: false,
                    showticklabels: true,
                    tickcolor: "rgb(127,127,127)",
                    ticks: "outside",
                    zeroline: true
                },
                yaxis: {
                    range: [0, 50],
                    gridcolor: "rgb(255,255,255)",
                    showgrid: true,
                    showline: false,
                    showticklabels: true,
                    tickcolor: "rgb(127,127,127)",
                    ticks: "outside",
                    zeroline: false
                }
            },
            options: {
                displayModeBar: false,
                staticPlot: true
            }
        }
    },
    methods: {
        calc_mlu(xs, mmx, lux) {
            const m = {x: [], y: []}, lu = {x: [], y: []};

            xs.reduce((ds, d) => {ds.push(d.Year); return ds;}, lu.x);
            xs.reduce((ds, d) => {ds.unshift(d.Year); return ds;}, lu.x);
            xs.reduce((ds, d) => {ds.push(d.U); return ds;}, lu.y);
            xs.reduce((ds, d) => {ds.unshift(d.L); return ds;}, lu.y);

            xs.reduce((ds, d) => {ds.push(d.Year); return ds}, m.x);
            xs.reduce((ds, d) => {ds.push(d.M); return ds}, m.y);

            mmx.x = m.x;
            mmx.y = m.y;
            lux.x = lu.x;
            lux.y = lu.y;
        },
        update0() {
            this.Incidence.Baseline = this.Curr0
                .filter(d => d.Year >= this.Year0)
                .filter(d => d.Year <= this.Year1)
                .map(d => {
                    return { 'Year': d.Year, 'M': d.IncR_M * 1e5, 'L': d.IncR_L * 1e5, 'U': d.IncR_U * 1e5 };
                })

            this.calc_mlu(this.Incidence.Baseline, this.Incidence.M0, this.Incidence.LU0);


            this.Mortality.Baseline = this.Curr0
              .filter(d => d.Year >= this.Year0)
              .filter(d => d.Year <= this.Year1)
              .map(d => {
                  return { 'Year': d.Year, 'M': d.MorR_M * 1e5, 'L': d.MorR_L * 1e5, 'U': d.MorR_U * 1e5 };
              })

            this.calc_mlu(this.Mortality.Baseline, this.Mortality.M0, this.Mortality.LU0);

            if (this.Incidence.Baseline.length > 0) {
                this.layout_inc.yaxis.range[1] = this.Incidence.Baseline[0].U;
                this.layout_mor.yaxis.range[1] = this.Mortality.Baseline[0].U;
            } else {
                this.layout_inc.yaxis.range[1] = 200;
                this.layout_mor.yaxis.range[1] = 40;
            }

        },
        update1 () {
            this.Incidence.Intervention = this.Curr1
              .filter(d => d.Year >= this.Year0)
              .filter(d => d.Year <= this.Year1)
              .map(d => {
                  return { 'Year': d.Year, 'M': d.IncR_M * 1e5, 'L': d.IncR_L * 1e5, 'U': d.IncR_U * 1e5 };
              })

            this.calc_mlu(this.Incidence.Intervention, this.Incidence.M1, this.Incidence.LU1);


            this.Mortality.Intervention = this.Curr1
              .filter(d => d.Year >= this.Year0)
              .filter(d => d.Year <= this.Year1)
              .map(d => {
                  return { 'Year': d.Year, 'M': d.MorR_M * 1e5, 'L': d.MorR_L * 1e5, 'U': d.MorR_U  * 1e5};
              })

            this.calc_mlu(this.Mortality.Intervention, this.Mortality.M1, this.Mortality.LU1);
        }
    },
    mounted() {
        this.update0();
        this.update1();
        // this.updateFigure();
    }
}
</script>

<style scoped>

</style>