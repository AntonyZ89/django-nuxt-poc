import type { User } from '~/types'

interface Discipline {
  id: number
  name: string
  workload: number
  created_at: string
  updated_at: string

  teacher: Pick<User, 'name'>
  total_students: number
}

type DisciplineCreate = Pick<Discipline, 'name' | 'workload' | 'teacher'>
type DisciplineUpdate = Partial<DisciplineCreate>

export type {
  Discipline,
  DisciplineCreate,
  DisciplineUpdate
}
