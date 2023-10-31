<template>
  <UiCard class="w-96">
    <UiCardContent class="space-y-3 p-3">
      <h1 class="text-2xl font-bold text-center">
        Bem-vindo
      </h1>

      <form class="space-y-3" @submit.prevent="handleSubmit">
        <UiSelect
          name="role"
          :items="UserRoleList"
          object-key="value"
          object-value="label"
          :disabled="loading"
          placeholder="Tipo de usuário"
        />
        <UiInputError name="role" />

        <div>
          <UiInput name="email" placeholder="E-mail" type="email" />
          <UiInputError name="email" />
        </div>

        <div>
          <UiInput name="password" placeholder="Senha" type="password" />
          <UiInputError name="password" />
        </div>

        <div class="text-center">
          <UiButton type="submit">
            Entrar
          </UiButton>
        </div>
      </form>
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { z } from 'zod'
import type { FetchError } from 'ofetch'
import { AuthService } from '@/services'
import { UserRoleList, type Response, UserRole } from '@/types'

definePageMeta({
  layout: 'login'
})

const router = useRouter()
const { toast } = useToast()

const validationSchema = toTypedSchema(z.object({
  role: z.object({
    value: z.nativeEnum(UserRole),
    label: z.string()

  }, { required_error: 'Tipo de usuário é obrigatorio.' }),
  email: z.string().email('Informe um e-mail válido.').min(1, 'E-mail é obrigatório.'),
  password: z.string().min(1, 'Senha é obrigatória.')
}))

const initialValues = {
  role: undefined,
  email: '',
  password: ''
}

const loading = ref(false)
const { handleSubmit: submit, setFieldError, resetForm } = useForm({ initialValues, validationSchema })

const handleSubmit = submit(async (values) => {
  try {
    loading.value = true

    const response = await AuthService.login({
      ...values,
      role: values.role.value
    })
    toast({ type: 'success', message: response.message })

    localStorage.setItem('token', response.token)

    resetForm()
    router.push({ name: 'index' })
  } catch (e) {
    const error = e as FetchError<Response>
    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
    setFieldError('email', message)
  } finally {
    loading.value = false
  }
})
</script>
