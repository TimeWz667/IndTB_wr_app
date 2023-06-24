<template>
    <div class="container">
        <div class="card">
            <div class="card-header">
                <h3>Location</h3>
            </div>
            <div class="card-body">
                <div class="row">
                    <select class="form-control" name="template" v-model="selected">
                        <option v-for="(item, index)  in locations" :key="index" :value="item">
                            {{ item }}
                        </option>
                    </select>
                </div>
                <p>{{selected}}</p>
            </div>
        </div>
        <div id="ctrl" class="card">
            <div class="card-header">
                <h3>Intervention</h3>
            </div>
            <div class="card-body">
                <form id="intv">
                    <div class="action" v-for="(intv, i) in IntvForm" :key="i">
                        <div class="form-switch">
                            <input class="form-check-input" role="switch" type="checkbox" :id="i" v-model="intv.Clicked">
                            <label class="form-check-label" v-b-toggle="'intv'+i"><p><b>{{ `&nbsp;${intv.Desc} &#9432;` }}</b></p></label>

                            <div class="from-group  bg-light" v-for="(par, j) in intv.Pars" :key="j">
                                <label :for="i + par.name" size="sm">{{par.label + " " + Math.round(par.value * 100) + "%"}}</label>
                                <input class="form-control" :id="i + par.name" :name="par.name" type="range" :min="par.min" :max="par.max" step="0.01"
                                       v-model="par.value">
                            </div>
                        </div>
                    </div>

<!--                    <b-button-group style="padding-top: 20pt" class="d-flex">-->
<!--                        <button type="submit" class="btn btn-info" v-on:click="updateInterventions">Submit</button>-->
<!--                        <button type="submit" class="btn btn-warning" v-on:click="resetInterventions">Reset</button>-->
<!--                    </b-button-group>-->
                </form>
            </div>
        </div>
        <div id="mem" class="card">
            <div class="card-header">
                <h3>Memento</h3>
            </div>
            <div class="card-body">
                <form id="keeper">
                    <div class="form-group">
                        <label for="lab">Label:</label>
                        <input type="text" class="form-control" id="lab" v-model="CurrName">
                    </div>
                    <b-button-group style="padding-top: 20pt" class="d-flex">
                        <button type="submit" class="btn btn-primary">Keep</button>
                        <button type="submit" class="btn btn-danger">Clear</button>
                    </b-button-group>
                </form>
<!--                <ul class="list-group" v-for="(intv, i) in Keeps">-->
<!--                    <li class="list-group-item">-->
<!--                        <div class="row">-->
<!--                            <div class="col-7">{{intv.Label}}</div>-->
<!--                            <div class="container col-5">-->
<!--                                <b-button>Apply</b-button>-->
<!--                                <b-button>x</b-button>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </li>-->
<!--                </ul>-->
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: "QInputs",
    props: {
        locations: {
            type: Array,
            default() {
                return ["India", "Delhi"]
            }
        },
        IntvForm: {
            type: Array,
            default() {
                return [];
            }
        }
    },
    data() {
        return {
            selected: "India"
        }
    }
}
</script>

<style scoped>

</style>