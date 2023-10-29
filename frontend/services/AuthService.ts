import { useApi } from './api'

interface LoginParams {
  email: string;
  password: string;
}

function login(params: LoginParams) {
  return useApi('login/', { method: 'POST', body: params })
}

export default {
  login
}
