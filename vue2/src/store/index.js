import Vue from 'vue'
import Vuex from 'vuex'
import celebrity from './modules/celebrity'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { celebrity }
})
