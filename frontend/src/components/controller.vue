<template>
<div>
    <div class="d-grid">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#loc">Location</button>
        <div id="loc" class="collapse">
            Form
        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#intv">Interventions</button>
        <div id="intv" class="collapse">
            Form
        </div>
    </div>
    <div class="d-grid pt-2">
        <button class="btn btn-info btn-block" data-bs-toggle="collapse" data-bs-target="#mem">Memento</button>
        <div id="mem" class="collapse">
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