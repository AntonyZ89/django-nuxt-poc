import { UserRole } from '~/types'

const GUEST_ROUTES: Array<string> = [
  'login'
]

const ALL_ROUTES: Array<string> = [
  'index',
  'discipline',
  'discipline-view-id'
]

export default defineNuxtRouteMiddleware(async (to) => {
  if (process.server || typeof to.name !== 'string') { return }

  const globalStore = useGlobalStore()

  !globalStore.user && await globalStore.loadUserData()

  const isAuthenticated = !!globalStore.user
  const role = globalStore.user?.role

  if (!isAuthenticated && !GUEST_ROUTES.includes(to.name)) {
    return { name: 'login' }
  }

  if (
    isAuthenticated && (
      (role !== UserRole.COORDINATOR && !ALL_ROUTES.includes(to.name)) ||
          GUEST_ROUTES.includes(to.name)
    )
  ) {
    return { name: 'index' }
  }
})
