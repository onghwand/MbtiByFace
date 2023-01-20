// import axios from 'axios'
// import api from '@/api/api'

export default ({
  state: {
    top3: []
  },
  getters: {
    top3: state => state.top3
  },
  mutations: {
    SET_TOP3: (state, top3) => (state.top3 = top3)
  },
  actions: {
    saveTop3 ({ commit }, top3) {
      commit('SET_TOP3', top3)
    }
  }
})
