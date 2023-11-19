import {defineStore} from 'pinia'

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user: {
            isAuthenticated: false,
            email: null,
            token: null
        }
    }),
    actions: {
        initStore() {
            console.log('initStore')
            this.User.isAuthenticated = false
            if (localStorage.getItem('user.token')) {
                this.user.token = localStorage.getItem('user.token')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true
                console.log('init user', this.user)
            }
        },
        setToken(token, email) {
            console.log('setToken')
            this.user.token = token
            this.user.email = email
            this.user.isAuthenticated = true
            localStorage.setItem('user.token', token)
            localStorage.setItem('user.email', email)
            localStorage.setItem('user.email', true)
            console.log('seted token', token, email)
        },
        removeToken() {
            console.log('removeToken')
            this.user.token = null
            this.user.email = null
            this.user.isAuthenticated = false
            localStorage.setItem('user.token', token)
            localStorage.setItem('user.email', email)
            console.log('auth removed', email)
        }
    }

})
