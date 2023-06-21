<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="card-header">
                    <h4 class="card-title">Incidence</h4>
                </div>
                <div class="card-body">
                    {{baseline}}
                </div>
            </div>
            <div class="col-md-6">
                <div class="card-header">
                    <h4 class="card-title">Mortality</h4>
                </div>
                <div class="card-body">
                    {{intervention}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "QTrends",
    props: {
        baseline: {
            type: Array,
            required: true
        },
        intervention: {
            type: Array,
            default() {
                return [];
            }
        }
    }
}
</script>

<style scoped>

</style>