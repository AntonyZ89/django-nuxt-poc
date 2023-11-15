<template>
  <ul class="flex flex-col md:flex-row items-stretch md:items-center gap-y-3 md:gap-x-3">
    <li>
      <LangSwitcher />
    </li>
    <template v-if="globalStorage.user">
      <li class="text-sm font-bold">
        {{ $t(UserRoleLabel[globalStorage.user.role]) }}
      </li>
      <li class="flex items-center text-sm bg-gray-100 py-2.5 px-3 rounded-lg">
        <User class="mr-2 w-4 h-4" />

        {{ globalStorage.user.name }}
      </li>
    </template>
    <NavbarItem :name="$t('logout')" @click="logout" />
  </ul>
</template>

<script setup lang="ts">
import { User } from 'lucide-vue-next'
import { UserRoleLabel } from '~/types'

const router = useRouter()
const globalStorage = useGlobalStore()

function logout () {
  localStorage.removeItem('token')

  location.replace(
    router.resolve({ name: 'login' }).href
  )
}
</script>
