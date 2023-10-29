import { useApi } from './api'
import type { User } from '@/types'

function me() {
  return useApi<User>('me/')
}

export default {
  me
}
