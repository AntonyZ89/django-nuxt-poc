enum UserRole {
  STUDENT = 'STUDENT',
  TEACHER = 'TEACHER',
  COORDINATOR = 'COORDINATOR',
}

interface User {
  id: number
  last_login: string | null
  name: string
  email: string
  birthday: string
  role: UserRole
  created_at: string
  updated_at: string
}

export type {
  User
}
