<template>
  <UiCard>
    <UiCardHeader class="flex-row items-center pb-0 justify-between">
      <UiCardTitle>Disciplinas</UiCardTitle>

      <PermissionRole role="COORDINATOR">
        <UiButton :as="NuxtLink" :to="{ name: 'discipline-create' }">
          Novo
        </UiButton>
      </PermissionRole>
    </UiCardHeader>
    <UiCardContent class="p-3 space-y-3">
      <DisciplineToolbar />

      <DisciplineTable />

      <UiPagination
        :meta="disciplineStore.meta"
        :model-value="disciplineStore.meta.page"
        @update:model-value="disciplineStore.handlePage"
      />
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { NuxtLink } from '#components'

const disciplineStore = useDisciplineStore()

onMounted(disciplineStore.load)
</script>
