<template>
  <UiDialog :open="dialog" @update:open="dialog = $event">
    <UiDialogTrigger as-child>
      <UiButton variant="destructive" class="px-3 h-auto">
        <Trash class="w-4 h-4" />
      </UiButton>
    </UiDialogTrigger>
    <UiDialogContent class="sm:max-w-[425px]">
      <UiDialogHeader>
        <UiDialogTitle>
          Excluir disciplina "{{ item.name }}"?
        </UiDialogTitle>
        <UiDialogDescription>
          Esta ação não pode ser desfeita
        </UiDialogDescription>
      </UiDialogHeader>
      <UiDialogFooter>
        <UiButton variant="destructive" @click="handleRemove">
          Excluir
        </UiButton>
      </UiDialogFooter>
    </UiDialogContent>
  </UiDialog>
</template>

<script setup lang="ts">
import { Trash } from 'lucide-vue-next'
import type { FetchError } from 'ofetch'
import type { Discipline, Response } from '~/types'
import { DisciplineService } from '~/services'

interface Props {
  item: Discipline
}

const { toast } = useToast()
const props = defineProps<Props>()
const disciplineStore = useDisciplineStore()

const dialog = ref(false)

/**
 * Function
 */

async function handleRemove () {
  try {
    await DisciplineService.remove(props.item.id)

    toast({ type: 'success', message: 'Disciplina excluída com sucesso' })

    dialog.value = false

    if (disciplineStore.meta.page > 1 && disciplineStore.items.length === 1) {
      disciplineStore.handlePage(disciplineStore.meta.page - 1)
    } else {
      disciplineStore.load()
    }
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  }
}
</script>
