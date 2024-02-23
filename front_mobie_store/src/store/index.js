import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      item:[]
    },
    isAuthenticated:false,
    token: '',
    isLoading: false,
  },
  getters: {
  },
  mutations: {
    initailizeStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
        state.token =localStorage.getItem('token')
        state.isAuthenticated =true
      } else {
        state.token =''
        state.isAuthenticated = false
      }

    },
    setIsLoading(state, status){
      // console.log('kir khar')
      state.isLoading = status
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})


