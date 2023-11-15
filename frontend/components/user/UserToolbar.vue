<template>
  <UiCard>
    <UiCardContent class="p-3">
      <form class="grid md:grid-cols-[repeat(3,1fr)_150px] gap-3 items-end" @submit.prevent="handleSubmit">
        <div>
          <UiLabel for="name">
            {{ $t('user.field.name') }}
          </UiLabel>
          <UiInput name="name" />
          <UiInputError name="name" />
        </div>
        <div>
          <UiLabel for="email">
            {{ $t('user.field.email') }}
          </UiLabel>
          <UiInput name="email" />
          <UiInputError name="email" />
        </div>
        <div>
          <UiLabel for="role">
            {{ $t('user.field.role') }}
          </UiLabel>
          <UiSelect
            name="role"
            :items="UserRoleList"
            object-key="value"
            object-value="label"
            :placeholder="$t('all')"
          />
          <UiInputError name="role" />
        </div>

        <UiButton type="submit">
          {{ $t('search') }}
        </UiButton>
      </form>
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { z } from 'zod'
import { UserRole, UserRoleList } from '~/types'

const validationSchema = toTypedSchema(z.object({
  name: z.string().optional(),
  email: z.string().optional(),
  role: z.object({
    value: z.nativeEnum(UserRole),
    label: z.string()
  }).optional()
}))

const initialValues = {
  name: '',
  email: '',
  role: undefined
}

const userStore = useUserStore()

const { handleSubmit: submit, setValues } = useForm({ initialValues, validationSchema })

const handleSubmit = submit((values) => {
  userStore.filter = { ...values, role: values.role?.value }
})

/**
 * Lifecycle
 */

onMounted(() => {
  const filter = userStore.filter

  setValues({
    ...filter,
    role: filter?.role
      ? UserRoleList.find(r => r.value === filter.role)
      : undefined
  })
})
</script>
