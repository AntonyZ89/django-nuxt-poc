import { useApi } from './api'
import type { Discipline, ResponseList } from '~/types'

type ListParams = Partial<{
  page: number;
  per_page: number;
}>

function list(params?: ListParams) {
  return useApi<ResponseList<Discipline>>('discipline/', { params })
}

export default {
  list
}


