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
          {{ title }}
        </UiDialogTitle>
        <UiDialogDescription>
          {{ t('modal.delete.message') }}
        </UiDialogDescription>
      </UiDialogHeader>
      <UiDialogFooter>
        <UiButton variant="destructive" @click="handleRemove">
          {{ t('modal.delete.button') }}
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

const { t } = useI18n()
const { toast } = useToast()
const props = defineProps<Props>()
const disciplineStore = useDisciplineStore()

const dialog = ref(false)

const title = computed(() => {
  return t('modal.delete.title', [t('page.discipline', 1).toLowerCase(), props.item.name])
})

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
