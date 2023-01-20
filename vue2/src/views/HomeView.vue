<template>
  <div class="home">
    <h1>Home</h1>
    <button @click="go">닮은 연예인 알아보러 가기</button>
  </div>
</template>

<script>
import router from '@/router'
export default {
  name: 'HomeView',
  methods: {
    go () {
      router.push('about')
    }
  }
}
</script>
