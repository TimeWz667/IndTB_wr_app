<template>
<div>
  <h3></h3>
  <div class="row">
    <div class="col-8">
      <div class="row">
        <h4>Selectors</h4>
        <div id="ctrl">
          <div id="my-accordion" class="accordion" role="tablist">
            <b-card no-body class="mb-1">
              <b-card-header header-tag="header" class="p-1  d-grid gap-2" role="tab">
                <b-button v-b-toggle.accordion-2 visible variant="dark">Interventions</b-button>
              </b-card-header>
              <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel" visible>
                <b-card-body>
                  <form id="intv">
                    <div class="action" v-for="(intv, i) in IntvForm">
                      <div class="form-switch">
                        <input class="form-check-input" role="switch" type="checkbox" :id="i" v-model="intv.Clicked">
                        <label class="form-check-label" v-b-toggle="'intv'+i"><p><b>{{ `&nbsp;${intv.Desc} &#9432;` }}</b></p></label>
                      </div>

                      <b-collapse :id="'intv'+i">
                        <div class="from-group  bg-light" v-for="par in intv.Pars">
                          <label :for="i + par.name" size="sm">{{par.label + " " + Math.round(par.value * 100) + "%"}}</label>
                          <input class="form-control" :id="i + par.name" :name="par.name" type="range" :min="par.min" :max="par.max" step="0.01"
                                 v-model="par.value">
                        </div>
                      </b-collapse>
                    </div>

                    <b-button-group style="padding-top: 20pt" class="d-flex">
                      <button type="submit" class="btn btn-info" v-on:click="updateInterventions">Submit</button>
                      <button type="submit" class="btn btn-warning" v-on:click="resetInterventions">Reset</button>
                    </b-button-group>
                  </form>
                </b-card-body>
              </b-collapse>
            </b-card>
          </div>
        </div>
        <div id="mem">
          <b-card no-body class="mb-1">
            <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel" visible>
              <b-card-body>
                <form id="keeper">
                  <div class="form-group">
                    <label for="lab">Label:</label>
                    <input type="text" class="form-control" id="lab" v-model="CurrName">
                  </div>
                  <b-button-group style="padding-top: 20pt" class="d-flex">
                    <button type="submit" class="btn btn-primary" v-on:click="keepInterventions">Keep</button>
                    <button type="submit" class="btn btn-danger" v-on:click="clearInterventions">Clear</button>
                  </b-button-group>
                </form>
              </b-card-body>
            </b-collapse>
            <ul class="list-group" v-for="(intv, i) in Keeps">
              <li class="list-group-item">
                <div class="row">
                  <div class="col-7">{{intv.Label}}</div>
                  <div class="container col-5">
                    <b-button v-on:click="gotoKeep(i)">Apply</b-button>
                    <b-button v-on:click="removeKeep(i)">x</b-button>
                  </div>
                </div>
              </li>
            </ul>
          </b-card>
        </div>
      </div>

    </div>
    <div class="col-4">
      <h4>Value</h4>
      <h5>Intervention: </h5>
      <p>{{CurrText}}</p>
      <h3>Simulation: </h3>
      <p>{{CurrSource}}</p>
    </div>
  </div>
</div>
</template>

<script>


const intvs = [
  {
    Name: "PPM",
    Desc: "Private-public mixing",
    Clicked: false,
    Pars: [
      {
        name: "Scale", label: "Prop. remaining private providers to be engaged", value:0, min: 0, max: 1
      }
    ]
  },
  {
    Name: "CS",
    Desc: "Reducing symptomatic period",
    Clicked: false,
    Pars: [
      {
        name: "Scale", label: "Reduction in time to next care-seeking, %", value:0, min: 0, max: 0.99
      }
    ]
  }
]

export default {
  name: "scenario",
  data() {

    const i0 = JSON.stringify(intvs)

    return {
      IntvForm: intvs,
      Intv0: i0,
      IntvCurr: i0,
      CurrText: "Baseline",
      CurrSource: "",
      Keeps: [],
      CurrName: "untitle"
    }
  },
  mounted() {
    this.updateInterventions();
  },
  methods: {
    updateInterventions(evt) {
      evt.preventDefault();
      this.CurrName = "";
      this.CurrText = this.IntvForm.filter(d => d.Clicked).map(d => d.Name + ": " + d.Pars[0].value).join("; ");
      this.CurrSource = "New simulation";
      this.IntvCurr = JSON.stringify(this.IntvForm);
    },
    resetInterventions(evt) {
      evt.preventDefault();
      this.CurrName = "";
      this.CurrText = "Baseline";
      this.CurrSource = "";
      this.IntvForm = JSON.parse(this.Intv0);
      this.IntvCurr = this.Intv0
    },
    keepInterventions(evt) {
      evt.preventDefault();
      this.Keeps.push({
        'Label': this.CurrName,
        'Intv': this.IntvCurr
      })
    },
    clearInterventions(evt) {
      evt.preventDefault();
      this.Keeps = [];
    },
    gotoKeep(i) {
      const sel = this.Keeps[i];

      this.CurrName = sel.Label;
      this.IntvForm = JSON.parse(sel.Intv);
      this.IntvCurr = sel.Intv
      this.CurrText = this.IntvForm.filter(d => d.Clicked).map(d => d.Name + ": " + d.Pars[0].value).join("; ");
      this.CurrSource = "Loaded from " + sel.Label;

    },
    removeKeep(i) {
      this.Keeps = this.Keeps.filter((d, key) => key !== i);
    },
  }
}
</script>

<style scoped>

</style>