enum UserRole {
  STUDENT = 'STUDENT',
  TEACHER = 'TEACHER',
  COORDINATOR = 'COORDINATOR',
}

const UserRoleLabel = {
  [UserRole.STUDENT]: 'Estudante',
  [UserRole.TEACHER]: 'Professor',
  [UserRole.COORDINATOR]: 'Coordenador'
}

const UserRoleList = [
  { value: UserRole.STUDENT, label: UserRoleLabel[UserRole.STUDENT] },
  { value: UserRole.TEACHER, label: UserRoleLabel[UserRole.TEACHER] },
  { value: UserRole.COORDINATOR, label: UserRoleLabel[UserRole.COORDINATOR] }
]

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

type UserCreate = Pick<User, 'name' | 'email' | 'birthday' | 'role'>
type UserUpdate = UserCreate

export {
  UserRole,
  UserRoleList,
  UserRoleLabel
}

export type {
  User,
  UserCreate,
  UserUpdate
}
