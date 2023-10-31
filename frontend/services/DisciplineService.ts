import { useApi } from './api'
import type { Discipline, DisciplineCreate, DisciplineUpdate, ResponseList } from '~/types'

type ListParams = Partial<{
  page: number;
  per_page: number;
  expand?: ['students']
}>

interface DetailParams {
  id: number
  expand?: ['students']
}

type CreateParams = DisciplineCreate
type UpdateParams = Pick<Discipline, 'id'> & DisciplineUpdate

function list (params?: ListParams) {
  const expand = ApiHelper.parseExpand(params)

  return useApi<ResponseList<Discipline>>('discipline/', { params: { ...params, expand } })
}

function detail (params: DetailParams) {
  const { id, ...rest } = params

  return useApi<RequiredSelect<Discipline, 'students'>>(`discipline/${id}/`, { params: rest })
}

function create (params: CreateParams) {
  return useApi<Discipline>('discipline/', { method: 'POST', body: params })
}

function update (params: UpdateParams) {
  const { id, ...rest } = params

  return useApi<Discipline>(`discipline/${id}/`, { method: 'PUT', body: rest })
}

function remove (id: number) {
  return useApi<Discipline>(`discipline/${id}/`, { method: 'DELETE' })
}

export default {
  list,
  detail,
  create,
  update,
  remove
}
