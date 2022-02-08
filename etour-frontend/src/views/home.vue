<template>
  <div class="home">
      <intro/>
      <about/>
      <faq/>
    </div>
</template>

<script>
import intro from '../components/intro.vue'
import about from '../components/about.vue'

import faq from '../components/faq.vue'
export default {
  name: 'home',
  props: {
   
  },
  components: {
    intro,
    about,
    faq
  }

}

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

}

</style>
