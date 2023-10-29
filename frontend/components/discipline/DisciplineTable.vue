<template>
  <UiTable>
    <UiTableHeader>
      <UiTableHead>
        Nome
      </UiTableHead>
      <UiTableHead>
        Professor
      </UiTableHead>
      <UiTableHead>
        Total de Alunos
      </UiTableHead>
      <UiTableHead>
        Cadastrado em
      </UiTableHead>
      <UiTableHead>
        Atualizado em
      </UiTableHead>
      <UiTableHead class="text-center">
        Ações
      </UiTableHead>
    </UiTableHeader>

    <UiTableBody>
      <UiTableRow v-for="item in items" :key="item.id">
        <UiTableCell>
          {{ item.name }}
          </UiTableCell>
        <UiTableCell>
          {{ item.teacher.name }}
          </UiTableCell>
        <UiTableCell>
          {{ item.total_students }}
          </UiTableCell>
        <UiTableCell>
          {{ DateHelper.format(item.created_at) }}
          </UiTableCell>
        <UiTableCell>
          {{ DateHelper.format(item.updated_at) }}
          </UiTableCell>
        <UiTableCell class="text-center space-x-3">
          <UiButton>Editar</UiButton>
          <UiButton>Visualizar</UiButton>
          </UiTableCell>
      </UiTableRow>
    </UiTableBody>
  </UiTable>
</template>

<script setup lang="ts">
import type { FetchError } from 'ofetch'
import { DisciplineService } from '~/services'
import type { Discipline, Response } from '~/types'

const { toast } = useToast()
const items = ref<Discipline[]>([])

/**
 * Function
 */

async function getItems() {
  try {
    const { results } = await DisciplineService.list()

    items.value = results
  } catch (e) {
    const error = e as FetchError<Response>
    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  }
}

onMounted(getItems)
</script>
