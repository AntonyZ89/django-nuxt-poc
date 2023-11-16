<template>
  <UiTable>
    <UiTableHeader>
      <UiTableHead>
        {{ t('student') }}
      </UiTableHead>
      <UiTableHead>
        {{ t('note') }} 1
      </UiTableHead>
      <UiTableHead>
        {{ t('note') }} 2
      </UiTableHead>
      <UiTableHead>
        {{ t('average') }}
      </UiTableHead>
      <PermissionRole role="TEACHER">
        <UiTableHead class="text-center">
          {{ t('actions') }}
        </UiTableHead>
      </PermissionRole>
    </UiTableHeader>

    <UiTableBody>
      <template v-if="item.students.length">
        <UiTableRow v-for="disciplineStudent in item.students" :key="disciplineStudent.id">
          <UiTableCell>
            {{ disciplineStudent.user_obj.name }}
          </UiTableCell>
          <DisciplineViewStudentTableEditable
            v-if="globalStore.user!.role === UserRole.TEACHER"
            :discipline-id="item.id"
            :item="disciplineStudent"
          />
          <DisciplineViewStudentTableRaw
            v-else
            :item="disciplineStudent"
          />
        </UiTableRow>
      </template>

      <UiTableEmpty v-else :colspan="6">
        <h1 class="text-xl font-bold">
          {{ t('no_data') }}
        </h1>
      </UiTableEmpty>
    </UiTableBody>
  </UiTable>
</template>

<script setup lang="ts">
import { UserRole } from '~/types'

const globalStore = useGlobalStore()
const disciplineViewStore = useDisciplineViewStore()
const { t } = useI18n()

const item = computed(() => disciplineViewStore.item!)
</script>

<i18n lang="json">
  {
    "en": {
      "student": "Student",
      "note": "Note",
      "no_data": "No data found",
      "average": "Average"
    },
    "pt": {
      "student": "Aluno",
      "note": "Nota",
      "no_data": "Nenhuma informação encontrada",
      "average": "Média"
    },
    "es": {
      "student": "Alumno",
      "note": "Nota",
      "no_data": "No información encontrada",
      "average": "Promedio"
    }
  }
</i18n>
