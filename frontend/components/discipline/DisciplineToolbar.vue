<template>
  <UiCard>
    <UiCardContent class="p-3">
      <form class="grid md:grid-cols-[repeat(2,1fr)_150px] gap-3 items-end" @submit.prevent="handleSubmit">
        <div>
          <UiLabel for="name">
            Nome
          </UiLabel>
          <UiInput name="name" />
          <UiInputError name="name" />
        </div>
        <div>
          <UiLabel for="teacher">
            Professor
          </UiLabel>
          <UiInput name="teacher" />
          <UiInputError name="teacher" />
        </div>

        <UiButton type="submit">
          Pesquisar
        </UiButton>
      </form>
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { z } from 'zod'
const validationSchema = toTypedSchema(z.object({
  name: z.string().optional(),
  teacher: z.string().optional()
}))

const initialValues = {
  name: '',
  teacher: ''
}

const disciplineStore = useDisciplineStore()

const { handleSubmit: submit, setValues } = useForm({ initialValues, validationSchema })

const handleSubmit = submit(values => (disciplineStore.filter = values))

/**
 * Lifecycle
 */

onMounted(() => setValues(disciplineStore.filter))
</script>
