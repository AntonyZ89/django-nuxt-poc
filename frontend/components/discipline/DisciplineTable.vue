<template>
  <UiTable>
    <UiTableHeader>
      <UiTableHead>
        {{ $t('discipline.field.name') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('discipline.field.teacher') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('discipline.field.workload') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('discipline.field.total_students') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('discipline.field.created_at') }}
      </UiTableHead>
      <UiTableHead>
        {{ $t('discipline.field.updated_at') }}
      </UiTableHead>
      <UiTableHead class="text-center">
        {{ $t('actions') }}
      </UiTableHead>
    </UiTableHeader>

    <UiTableBody>
      <template v-if="disciplineStore.items.length">
        <UiTableRow v-for="item in disciplineStore.items" :key="item.id">
          <UiTableCell>
            {{ item.name }}
          </UiTableCell>
          <UiTableCell>
            {{ item.teacher_obj.name }}
          </UiTableCell>
          <UiTableCell>
            {{ item.workload }}h
          </UiTableCell>
          <UiTableCell>
            {{ item.total_students }}
          </UiTableCell>
          <UiTableCell>
            {{ DateHelper.formatDatetime(item.created_at) }}
          </UiTableCell>
          <UiTableCell>
            {{ DateHelper.formatDatetime(item.updated_at) }}
          </UiTableCell>
          <UiTableCell class="text-center space-y-1 lg:space-y-0 md:space-x-2">
            <PermissionRole role="COORDINATOR">
              <UiButton
                class="px-3 h-auto"
                :as="NuxtLink"
                :to="{ name: 'discipline-update-id', params: { id: item.id } }"
              >
                <Pencil class="w-4 h-4" />
              </UiButton>
            </PermissionRole>

            <UiButton
              :as="NuxtLink"
              :to="{ name: 'discipline-view-id', params: { id: item.id } }"
              variant="outline"
              class="px-3 h-auto"
            >
              <Eye class="w-4 h-4" />
            </UiButton>

            <PermissionRole role="COORDINATOR">
              <DisciplineTableRemove :item="item" />
            </PermissionRole>
          </UiTableCell>
        </UiTableRow>
      </template>

      <UiTableEmpty v-else :colspan="6">
        <h1 class="text-xl font-bold">
          Nenhuma disciplina encontrada
        </h1>
      </UiTableEmpty>
    </UiTableBody>
  </UiTable>
</template>

<script setup lang="ts">
import { Pencil, Eye } from 'lucide-vue-next'
import { NuxtLink } from '#components'

const disciplineStore = useDisciplineStore()
</script>
