<template>
    <UiCard class="w-96">
        <UiCardContent class="space-y-3 p-3">
            <h1 class="text-2xl font-bold text-center">Bem-vindo</h1>

            <form class="space-y-3" @submit.prevent="handleSubmit">
                <div>
                    <UiInput name="email" placeholder="E-mail" type="email" />
                    <UiInputError name="email" />
                </div>

                <div>
                    <UiInput name="password" placeholder="Senha" type="password"/>
                    <UiInputError name="password" />
                </div>

                <div class="text-center">
                    <UiButton type="submit">Entrar</UiButton>
                </div>
            </form>
        </UiCardContent>

    </UiCard>
</template>

<script setup lang="ts">
import { z } from 'zod'
import type { FetchError } from 'ofetch'
import { AuthService } from '@/services'
import type { Response } from '@/types'

definePageMeta({
    layout: 'login'
})

const router = useRouter()
const { toast } = useToast()

const validationSchema = toTypedSchema(z.object({
    email: z.string().email('Informe um e-mail válido.').min(1, 'E-mail é obrigatório.'),
    password: z.string().min(1, 'Senha é obrigatória.')
}))

const initialValues = {
    email: '',
    password: ''
}

const { handleSubmit: submit, setFieldError, resetForm } = useForm({ initialValues, validationSchema })

const handleSubmit = submit(async (values) => {
  try {
    const response = await AuthService.login(values)
    toast({ type: 'success', message: response.message })

    localStorage.setItem('token', response.token)

    resetForm()
    router.push({ name: 'index' })

  } catch (e) {
    const error = e as FetchError<Response>
    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
    setFieldError('email', message)
  }
})
</script>
