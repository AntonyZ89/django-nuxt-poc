import { useApi } from './api'
import type { User, Meta, ResponseList, UserCreate, UserUpdate } from '@/types'

type ListParams = Partial<Meta & Pick<User, 'role'> & {
  not_discipline: number | string
}>

type CreateParams = UserCreate
type UpdateParams = Pick<User, 'id'> & UserUpdate

function me () {
  return useApi<User>('user/me/')
}

function list (params?: ListParams) {
  return useApi<ResponseList<User>>('user/', { params })
}

function detail (id: number) {
  return useApi<User>(`user/${id}/`)
}

function create (params: CreateParams) {
  return useApi<User>('user/', { method: 'POST', body: params })
}

function update (params: UpdateParams) {
  const { id, ...rest } = params

  return useApi<User>(`user/${id}/`, { method: 'PATCH', body: rest })
}

function remove (id: number) {
  return useApi<User>(`user/${id}/`, { method: 'DELETE' })
}

export default {
  list,
  me,
  detail,
  create,
  update,
  remove
}
