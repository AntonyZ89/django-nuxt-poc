import type { User } from '~/types'

interface Discipline {
  id: number
  teacher: number
  name: string
  workload: number
  created_at: string
  updated_at: string

  teacher_obj: Pick<User, 'id' | 'name'>
  total_students: number

  students?: User[]
}

type DisciplineCreate = Pick<Discipline, 'name' | 'workload' | 'teacher'> & { students: Array<User['id']> }
type DisciplineUpdate = DisciplineCreate

export type {
  Discipline,
  DisciplineCreate,
  DisciplineUpdate
}
