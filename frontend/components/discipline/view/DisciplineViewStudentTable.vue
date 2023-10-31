<template>
  <UiTable>
    <UiTableHeader>
      <UiTableHead>
        Aluno
      </UiTableHead>
      <UiTableHead>
        Nota 1
      </UiTableHead>
      <UiTableHead>
        Nota 2
      </UiTableHead>
      <UiTableHead>
        Média
      </UiTableHead>
      <PermissionRole role="TEACHER">
        <UiTableHead class="text-center">
          Ações
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
          Nenhuma disciplina encontrada
        </h1>
      </UiTableEmpty>
    </UiTableBody>
  </UiTable>
</template>

<script setup lang="ts">
import { UserRole } from '~/types'

const globalStore = useGlobalStore()
const disciplineViewStore = useDisciplineViewStore()

const item = computed(() => disciplineViewStore.item!)
</script>
