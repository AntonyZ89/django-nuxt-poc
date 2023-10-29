import { ofetch } from 'ofetch'

const useApi = ofetch.create({
  baseURL: import.meta.env.VITE_BASE_URL,
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

