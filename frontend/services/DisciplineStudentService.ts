import { useApi } from './api'
import type { DisciplineStudent } from '~/types'

type UpdateParams = Pick<DisciplineStudent, 'id' | 'note_1' | 'note_2'>

function update (params: UpdateParams) {
  const { id, ...rest } = params

  return useApi(`/discipline-student/${id}/`, { method: 'PATCH', body: rest })
}

export default {
  update
}
