<template>
<div>
    {{text}}
</div>
</template>

<script>
// const axios = require('axios');


export default {
    name: "atb",
    data() {
        return {
            "text": "test"
        }
    },
    methods: {
        getText() {
            fetch('http://example.com/users/1', {
              method: 'PUT',
              body: JSON.stringify({
                name: 'John Doe',
                age: 27,
              }),
              headers: {
                'Content-type': 'application/json',
              },
            })
              .then((response) => response.json())
              .then((json) => console.log(json));

            // axios.get("http://localhost:5000/locs/").then((res) => {
            //     this.text = res.data;
            // })
            //   .catch((error) => {
            //       console.error(error);
            //   });

          this.text = "HI"
        }
    },
    mounted() {
      this.getText();
    }
}
</script>

<style scoped>

</style>