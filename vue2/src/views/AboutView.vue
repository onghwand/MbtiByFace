<template>
  <div class="about">
    <h1>Mbti By Face</h1>
    <p>성격은 <strong>얼굴</strong>에 나타난다</p>
    <br>
    <h2>내 사진 넣기</h2>
    <form @submit.prevent="uploadPhoto()">
      <input type="file" id="imgUpload">
      <div>
        <button type="submit">가즈아</button>
      </div>
    </form>
  </div>
</template>

<script>
// import api from '@/api/api'
import axios from 'axios'
import router from '@/router'
import { mapActions } from 'vuex'

export default {
  name: 'AboutView',
  methods: {
    ...mapActions(['saveTop3']),
    uploadPhoto () {
      const frm = new FormData()
      const photoFile = document.getElementById('imgUpload')
      frm.append('file', photoFile.files[0])
      axios({
        url: 'http://127.0.0.1:8000/celebrities/top3/',
        method: 'post',
        data: frm,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(res => {
          console.log(res.data)
          this.saveTop3(res.data)
          router.push('result')
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
