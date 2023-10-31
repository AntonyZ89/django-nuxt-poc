import { useApi } from './api'
import type { DisciplineNote } from '~/types'

type Params = DisciplineNote

function create (params: Params) {
  return useApi<DisciplineNote>('discipline/', { method: 'POST', body: params })
}

function remove (params: Params) {
  return useApi<DisciplineNote>('discipline-note/', { method: 'DELETE', body: params })
}

export default {
  create,
  remove
}
