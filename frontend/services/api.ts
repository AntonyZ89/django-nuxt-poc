import { ofetch } from 'ofetch'

function getCookie (name: string) {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)

  if (parts.length === 2) {
    return parts.pop()?.split(';').shift()
  }
}

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
    const cookie = getCookie('i18n_redirected')
    const headers = options.headers as Record<string, string> ?? {}

    if (cookie) {
      headers['Accept-Language'] = cookie
    }

    if (token) {
      headers.Authorization = `Token ${token}`
    }

    options.headers = headers
  }
})

export { useApi }
