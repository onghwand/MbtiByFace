<template>
  <div class="about">
    <h1>Mbti By Face</h1>
    <p>성격은 <strong>얼굴</strong>에 나타난다</p>
    <br>
    <h2>내 사진 넣기</h2>
    <form @submit.prevent="">
      <input type="file" @change="upload" id="imgUpload">
      <div>
        <button type="submit">가즈아</button>
      </div>
    </form>
  </div>
</template>

<script>
import api from '@/api/api'
import axios from 'axios'

export default {
  name: 'AboutView',
  data () {
    return {
      photoUrl: ''
    }
  },
  methods: {
    upload (e) {
      const file = e.target.files
      const url = URL.createObjectURL(file[0])
      this.photoUrl = url
    },
    uploadPhoto () {
      const frm = new FormData()
      const photoFile = document.getElementById('imgUpload')
      frm.append('imgUpload', photoFile.files[0])
      axios({
        url: api.celebrities.top3,
        method: 'post',
        data: frm,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
