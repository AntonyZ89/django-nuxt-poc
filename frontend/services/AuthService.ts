import { useApi } from './api'
import type { User } from '~/types'

interface LoginParams {
  email: string;
  password: string;
  role: User['role']
}

function login (params: LoginParams) {
  return useApi('login/', { method: 'POST', body: params })
}

export default {
  login
}
