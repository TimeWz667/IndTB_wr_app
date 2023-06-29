<template>
<div>
    <div class="d-grid">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#loc">
            {{ `&nbsp;${CurLoc}: ${YearStart} - ${YearEnd}` }}</button>
        <div id="loc" class="collapse show">
            <div class="container">
                <form>
                    <select class="form-select" v-model="CurLoc">
                        <option v-for="(loc, i) in Locations" :key="i" :value="loc">{{ loc }}</option>
                    </select>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" id="y0_2015" value="2015" name="y0" v-model="YearStart" checked>
                        <label class="form-check-label" for="y0_2015">2015~</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" id="y0_2022" value="2022" name="y0" v-model="YearStart">
                        <label class="form-check-label" for="y0_2022">2022~</label>
                    </div>

                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" id="y1_2030" value="2030" name="y1" v-model="YearEnd" checked>
                        <label class="form-check-label" for="y1_2030">~2030</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" id="y1_2035" value="2035" name="y1" v-model="YearEnd" disabled>
                        <label class="form-check-label" for="y1_2035">~2035</label>
                    </div>
                    <button type="submit" class="btn btn-primary" v-on:click="updateSettings">Update</button>
                </form>
            </div>
        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#intv">Interventions</button>
        <div id="intv" class="collapse show">
            <form>
                <div class="form_intv">
                    <div class="action" v-for="(intv, i) in IntvForm" :key="i">
                        <div class="form-switch">
                            <input class="form-check-input" role="switch" type="checkbox" :id="i" v-model="intv.Clicked">
                            <label class="form-check-label" :for="i"><h5>{{ `&nbsp;${intv.Desc} &#9432;` }}</h5></label>
                        </div>

                        <div class="from-group" v-for="par in intv.Pars" :key="par.name">
                            <div v-if="par.type === 'bool'">
                                <input class="form-check-input" :id="i + par.name" :name="par.name" type="checkbox"
                                       v-model="par.value">
                                <label :for="i + par.name" size="sm">{{par.label}}</label>
                            </div>
                            <div v-else-if="par.type === 'choice'">
                                <div class="form-check form-check-inline" v-for="(op, j) in par.values">
                                    <input class="form-check-input" type="radio" name="inlineRadioOptions" :id="'inlineRadio' + j"
                                           :value="op" v-model="par.value">
                                    <label class="form-check-label" :for="'inlineRadio' + j">{{ op }}</label>
                                </div>
                            </div>
                            <div v-else>
                                <label :for="i + par.name" size="sm">{{par.label + " " + par.fmt(par.value)}}</label>
                                <input class="form-control" :id="i + par.name" :name="par.name" type="range"
                                       :min="par.min" :max="par.max" :step="par.step"
                                       v-model="par.value">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="btn-group" role="group" aria-label="Basic example" style="padding-top: 20pt">
                    <!--                <button type="submit" class="btn btn-info" v-on:click="revertIntv">Last</button>-->
                    <button type="submit" class="btn btn-primary" v-on:click="updateIntv">Run</button>
                    <button type="submit" class="btn btn-warning" v-on:click="resetIntv">Reset</button>
                </div>
            </form>
        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#mem">Mementos</button>
        <div id="mem" class="collapse show">
            <div class="btn-group" role="group" aria-label="Basic example" style="padding-top: 20pt">
<!--                <button type="submit" class="btn btn-info" v-on:click="revertIntv">Last</button>-->
                <button type="submit" class="btn btn-primary" v-on:click="updateIntv">Update</button>
                <button type="submit" class="btn btn-warning" v-on:click="resetIntv">Reset</button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "controller",
    props: {
        Locations: {
            type: Array,
            required: true
        },
        IntvForm: {
            type: Array,
            required: true
        }
    },
    data: function() {
        return {
            CurLoc: this.Locations[0],
            YearStart: 2022,
            YearEnd: 2030
        }
    },
    methods: {
        updateSettings(evt) {
            evt.preventDefault();
            const res = { Location: this.CurLoc, YearStart: +this.YearStart, YearEnd: +this.YearEnd };
            this.$emit("settings_update", res);
        },
        updateIntv(evt) {
            evt.preventDefault();
            const res = this.IntvForm
                .filter(d => d.Clicked)
                .reduce((prev, d) => {
                    prev[d.Name] = d.Pars
                        .reduce((collector, x) => {collector[x.name] = x.value; return collector}, {});
                    return prev;
                }, {})

            this.$emit("intv_update", res);
        },
        resetIntv(evt) {
            evt.preventDefault();
            this.$emit("intv_reset");
        }
    }
}
</script>

<style scoped>
.btn {
    text-align: left;
}

.form_intv {
    overflow-y: scroll;
    height: 300pt;
}
</style>