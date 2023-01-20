<template>
  <div>
    <h1>Result</h1>
    <div v-for="(celeb,i) in top3" :key="i">
      <p>{{ i+1 }}위</p>
      <img :src="celeb.image_url" height="250" width="250">
      <p>{{ celeb.name }} / {{ celeb.mbti }}</p>
      <br>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'ResultView',
  computed: {
    ...mapGetters(['top3'])
  }

}
</script>
