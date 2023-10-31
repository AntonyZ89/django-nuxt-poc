<template>
  <UiTableCell colspan="4">
    <form class="grid grid-cols-4" @submit.prevent="handleSubmit">
      <div>
        <UiInput
          class="w-24"
          name="note_1"
          :placeholder="item.note_1 === null ? 'Vazio' : ''"
          type="number"
          min="0"
          max="10"
          step="0.01"
        />
        <UiInputError name="note_1" />
      </div>

      <div>
        <UiInput
          class="w-24"
          name="note_2"
          :placeholder="item.note_2 === null ? 'Vazio' : ''"
          type="number"
          min="0"
          max="10"
          step="0.01"
        />
        <UiInputError name="note_2" />
      </div>

      <span class="flex items-center">{{ item.media ?? '-' }}</span>
      <div class="text-center">
        <UiButton type="submit" :loading="loading">
          Salvar
        </UiButton>
      </div>
    </form>
  </UiTableCell>
</template>

<script setup lang="ts">
import { z } from 'zod'
import { FetchError } from 'ofetch'
import type { Discipline, Response } from '~/types'
import { DisciplineStudentService } from '~/services'

interface Props {
  disciplineId: number,
  item: NonNullable<Discipline['students']>[number]
}
const { toast } = useToast()
const disciplineViewStore = useDisciplineViewStore()

const props = defineProps<Props>()

const validationSchema = toTypedSchema(z.object({
  note_1: z.number({ invalid_type_error: 'Inválido' })
    .min(0, 'Mínimo 0')
    .max(10, 'Máximo 10')
    .or(
      z.literal('')
        .transform(value => value === '' ? null : value)
    )
    .nullable(),
  note_2: z.number({ invalid_type_error: 'Inválido' })
    .min(0, 'Mínimo 0')
    .max(10, 'Máximo 10')
    .or(
      z.literal('')
        .transform(value => value === '' ? null : value)
    )
    .nullable()
}))

const initialValues = {
  note_1: props.item.note_1,
  note_2: props.item.note_2
}

const loading = ref(false)
const { handleSubmit: submit, setErrors } = useForm({ initialValues, validationSchema })

/**
 * Function
 */

const handleSubmit = submit(async (values) => {
  try {
    loading.value = true

    await DisciplineStudentService.update({
      id: props.item.id,
      ...values
    })

    toast({ type: 'success', message: 'Nota salva com sucesso' })

    await disciplineViewStore.load(props.disciplineId)
  } catch (e) {
    const error = e as FetchError<Response | Record<string, string>>
    const message = error.data?.message || 'Erro ao carregar a disciplina'

    toast({ type: 'error', message })

    if (error.statusCode === 400) {
      const data = error.data as Record<string, string>
      setErrors(data)
    }
  } finally {
    loading.value = false
  }
})
</script>
