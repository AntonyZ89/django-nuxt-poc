<template>
  <UiCard>
    <UiCardContent class="flex justify-between p-3">
      <ul class="flex gap-x-3">
        <NavbarItem to="/" name="Início" />
        <NavbarItem to="/discipline" name="Disciplinas" />

        <PermissionRole role="COORDINATOR">
          <NavbarItem to="/user" name="Usuários" />
        </PermissionRole>
      </ul>

      <ul class="flex items-center gap-x-3">
        <template v-if="globalStorage.user">
          <li class="text-sm font-bold">
            {{ UserRoleLabel[globalStorage.user.role] }}
          </li>
          <li class="flex items-center text-sm bg-gray-100 py-2.5 px-3 rounded-lg">
            <User class="mr-2 w-4 h-4" />

            {{ globalStorage.user.name }}
          </li>
        </template>
        <NavbarItem name="Sair" @click="logout" />
      </ul>
    </UiCardContent>
  </UiCard>
</template>

<script setup>
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
