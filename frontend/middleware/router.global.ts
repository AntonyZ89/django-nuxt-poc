const GUEST_ROUTES: Array<string> = [
  'login'
]

export default defineNuxtRouteMiddleware(async (to) => {
  if (process.server || typeof to.name !== 'string') { return }

  const globalStore = useGlobalStore()

  !globalStore.user && await globalStore.loadUserData()

  const isAuthenticated = !!globalStore.user

  if (!isAuthenticated && !GUEST_ROUTES.includes(to.name)) {
    return { name: 'login' }
  }

  if (isAuthenticated && GUEST_ROUTES.includes(to.name)) {
    return { name: 'index' }
  }
})
