import { ofetch } from 'ofetch'

const useApi = ofetch.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  onResponseError (error) {
    const token = localStorage.getItem('token')

    // Unauthorized
    if (error.response.status === 401 && token) {
      localStorage.removeItem('token')
      location.replace('/')
    }
  },
  onRequest ({ options }) {
    const token = localStorage.getItem('token')

    if (token) {
      options.headers = [
        ['Authorization', `Token ${token}`]
      ]
    }
  }
})

export { useApi }
