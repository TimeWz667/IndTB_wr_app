<template>
<div>
    <div class="d-grid">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#loc">Location</button>
        <div id="loc" class="collapse show">
            <div class="container">
                <form>
                Location (current: {{i}}})
              <select class="form-select">
                  <option>1</option>
                  <option>2</option>
                </select>
              <div class="form-check mb-3">
                <label class="form-check-label">
                  <input class="form-check-input" type="checkbox" name="remember"> Show 2015-
                </label>
              </div>
              <button type="submit" class="btn btn-primary" v-on:click="">Update</button>
            </form>
            </div>

        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#intv">Interventions</button>
        <div id="intv" class="collapse show">
            Form
        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#mem">Memento</button>
        <div id="mem" class="collapse show">
            Form
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "controller"
}
</script>

<style scoped>
.btn {
    text-align: left;
}
</style>