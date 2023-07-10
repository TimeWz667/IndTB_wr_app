<template>
<div>
  <h3></h3>
  <div class="row">
      <div class="col-md-12">
          <iframe id="portal" class="embed-responsive" src="http://127.0.0.1:5173"></iframe>
      </div>
  </div>
</div>
</template>

<script>

export default {
  name: "scenario"
}
</script>

<style scoped>

#portal {
    width: 100%;
    height: 700pt;
}


</style>

