<template>
  <UiTable>
    <UiTableHeader>
      <UiTableHead>
        {{ $t('user.field.name') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('user.field.email') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('user.field.role') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('user.field.created_at') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('user.field.updated_at') }}
      </UiTableHead>
      <UiTableHead class="text-center w-44">
        {{ $t('actions') }}
      </UiTableHead>
    </UiTableHeader>

    <UiTableBody>
      <template v-if="userStore.items.length">
        <UiTableRow v-for="item in userStore.items" :key="item.id">
          <UiTableCell>
            {{ item.name }}
          </UiTableCell>
          <UiTableCell>
            {{ item.email }}
          </UiTableCell>
          <UiTableCell>
            {{ $t(UserRoleLabel[item.role]) }}
          </UiTableCell>
          <UiTableCell>
            {{ DateHelper.formatDatetime(item.created_at) }}
          </UiTableCell>
          <UiTableCell>
            {{ DateHelper.formatDatetime(item.updated_at) }}
          </UiTableCell>
          <UiTableCell class="text-center space-y-1 lg:space-y-0 md:space-x-2">
            <UiButton
              class="px-3 h-auto"
              :as="NuxtLink"
              :to="{ name: 'user-id', params: { id: item.id } }"
            >
              <Pencil class="w-4 h-4" />
            </UiButton>
            <UserTableRemove v-if="item.id !== globalStore.user!.id" :item="item" />
          </UiTableCell>
        </UiTableRow>
      </template>

      <UiTableEmpty v-else :colspan="6">
        <h1 class="text-xl font-bold">
          Nenhum usuário encontrado
        </h1>
      </UiTableEmpty>
    </UiTableBody>
  </UiTable>
</template>

<script setup lang="ts">
import { Pencil } from 'lucide-vue-next'
import { NuxtLink } from '#components'
import { UserRoleLabel } from '~/types'

const globalStore = useGlobalStore()
const userStore = useUserStore()
</script>
