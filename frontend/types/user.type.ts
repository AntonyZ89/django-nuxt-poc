let _t: any

const t = (key: string) => {
  if (!_t) {
    _t = useI18n().t
  }

  return _t(key)
}

enum UserRole {
  STUDENT = 'STUDENT',
  TEACHER = 'TEACHER',
  COORDINATOR = 'COORDINATOR',
}

const UserRoleLabel = {
  [UserRole.STUDENT]: 'role.student',
  [UserRole.TEACHER]: 'role.teacher',
  [UserRole.COORDINATOR]: 'role.coordinator'
} as const

const UserRoleList = [
  {
    value: UserRole.STUDENT,
    get label () {
      return t(UserRoleLabel[UserRole.STUDENT])
    }
  },
  {
    value: UserRole.TEACHER,
    get label () {
      return t(UserRoleLabel[UserRole.TEACHER])
    }
  },
  {
    value: UserRole.COORDINATOR,
    get label () {
      return t(UserRoleLabel[UserRole.COORDINATOR])
    }
  }
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
