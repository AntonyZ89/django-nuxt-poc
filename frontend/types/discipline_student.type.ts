import type { User } from '~/types'

interface DisciplineStudent {
  id: number
  discipline: number
  user: number
  note_1: number | null
  note_2: number | null
  media: number | null
  user_obj: Pick<User, 'id' | 'name'>
}

export type {
  DisciplineStudent
}
