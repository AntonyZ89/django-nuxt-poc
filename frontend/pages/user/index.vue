<template>
  <UiCard>
    <UiCardHeader class="flex-row items-center justify-between pb-0">
      <UiCardTitle>
        {{ $t('page.user', 0) }}
      </UiCardTitle>

      <UiButton :as="NuxtLink" :to="{ name: 'user-create' }">
        {{ $t('create_entity', [$t('page.user')]) }}
      </UiButton>
    </UiCardHeader>
    <UiCardContent class="p-3 space-y-3">
      <UserToolbar />

      <UserTable />

      <UiPagination
        :meta="userStore.meta"
        :model-value="userStore.meta.page"
        @update:model-value="userStore.handlePage"
      />
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { NuxtLink } from '#components'

const userStore = useUserStore()

onMounted(userStore.load)
</script>
