<template>
<div>
    <div>
        <input type="range" min="0" max="5" step="0.01" id="tc" v-model="rate_tc">
        <label for="tc">Treatment completion {{rate_tc}} per year</label>
    </div>
    <div>
        <input type="range" min="0" max="5" step="0.01" id="td" v-model="rate_td">
        <label for="td">Death duration treatment {{rate_td}} per year</label>
    </div>
    <div>
        <input type="range" min="0" max="5" step="0.01" id="tl" v-model="rate_tl">
        <label for="tl">LTFU {{rate_tl}} per year</label>
    </div>

    <h4>Treatment period {{duration.toFixed(2)}} year</h4>
    <h4>Pr(TC) = {{pr_tc}}, Pr(TD) = {{pr_td}}, Pr(TL) = {{pr_tl}}</h4>
</div>
</template>

<script>
export default {
    name: "tutorial_txout",
    data() {
        return {
            rate_tc: 1,
            rate_td: 0,
            rate_tl: 1
        }
    },
    computed: {
        duration() {
            return 1 / (parseFloat(this.rate_tl) + parseFloat(this.rate_tc) + parseFloat(this.rate_td));
        },
        pr_tc() {
            return (this.rate_tc * this.duration * 100).toFixed() + '%';
        },
        pr_td() {
            return (this.rate_td * this.duration * 100).toFixed() + '%';
        },
        pr_tl() {
            return (this.rate_tl * this.duration * 100).toFixed() + '%';
        }
    }
}
</script>

<style scoped>

</style>