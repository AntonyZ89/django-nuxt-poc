import { UserService } from '~/services'
import type { User } from '~/types'

const useGlobalStore = defineStore('global', () => {
  /**
   * `null` = not logged in
   * `undefined` = user not loaded yet
   * `object` = logged in
   */
  const user = ref<User | undefined | null>()

  async function loadUserData () {
    try {
      user.value = await UserService.me()
    } catch {
      user.value = null
    }
  }

  return {
    user,
    loadUserData
  }
})

export { useGlobalStore }
