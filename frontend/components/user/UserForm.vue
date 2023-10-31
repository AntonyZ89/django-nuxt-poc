<template>
  <form @submit.prevent="handleSubmit">
    <UiCard v-if="values">
      <UiCardContent v-auto-animate class="p-3 space-y-3">
        <div>
          <UiLabel for="name">
            Nome
          </UiLabel>
          <UiInput name="name" :disabled="loading" />
          <UiInputError name="name" />
        </div>
        <div>
          <UiLabel for="email">
            E-mail
          </UiLabel>
          <UiInput name="email" type="email" :disabled="loading" />
          <UiInputError name="email" />
        </div>
        <div>
          <UiLabel for="birthday">
            Aniversário
          </UiLabel>
          <UiDate name="birthday" :disabled="loading" />
          <UiInputError name="birthday" />
        </div>
        <div>
          <UiLabel for="role">
            Tipo
          </UiLabel>
          <UiSelect
            name="role"
            :items="UserRoleList"
            object-key="value"
            object-value="label"
            :disabled="loading || !!id"
            placeholder="Selecione"
          />
          <UiInputError name="role" />
        </div>
        <div>
          <UiLabel for="password">
            {{ id ? "Nova senha" : "Senha" }}
          </UiLabel>
          <UiInput name="password" :disabled="loading" type="password" />
          <UiInputError name="password" />
        </div>
        <div v-if="values.password">
          <UiLabel for="password_confirmation">
            Confirmar senha
          </UiLabel>
          <UiInput name="password_confirmation" :disabled="loading" type="password" />
          <UiInputError name="password_confirmation" />
        </div>

        <div class="text-right">
          <UiButton :loading="loading">
            {{ id ? "Atualizar" : "Criar" }}
          </UiButton>
        </div>
      </UiCardContent>
    </UiCard>
  </form>
</template>

<script setup lang="ts">
import { format } from 'date-fns'
import type { FetchError } from 'ofetch'
import { z } from 'zod'
import { UserService } from '~/services'
import type { Response } from '~/types'
import { UserRole, UserRoleList, UserRoleLabel } from '~/types'

interface Props {
  id?: number
}

const props = withDefaults(defineProps<Props>(), {
  id: undefined
})

const { toast } = useToast()
const router = useRouter()

const validationSchema = z.object({
  name: z.string().min(3, 'O nome deve ter pelo menos 3 caracteres'),
  email: z.string().email('E-mail inválido'),
  role: z.object({
    value: z.nativeEnum(UserRole),
    label: z.string()
  }, { required_error: 'O tipo de usuário é obrigatório' }),
  birthday: z.date({ required_error: 'A data de aniversário é obrigatória' }),
  password: z.string().optional(),
  password_confirmation: z.string().min(6, 'A senha deve ter pelo menos 6 caracteres').optional()
}).superRefine((data, context) => {
  if (!props.id) {
    if (!data.password) {
      context.addIssue({
        path: ['password'],
        code: z.ZodIssueCode.custom,
        message: 'A senha é obrigatória'
      })
    } else if (data.password.length < 6) {
      context.addIssue({
        path: ['password'],
        code: z.ZodIssueCode.custom,
        message: 'A senha deve ter pelo menos 6 caracteres'
      })
    } else if (data.password !== data.password_confirmation) {
      console.log('teste', data.password, data.password_confirmation)
      context.addIssue({
        path: ['password_confirmation'],
        code: z.ZodIssueCode.custom,
        message: 'As senhas não conferem'
      })
    }
  }
})

const initialValues = {
  name: '',
  email: '',
  role: undefined,
  birthday: undefined,
  password: undefined,
  password_confirmation: undefined
}

const { values, setValues, setErrors, handleSubmit: submit } = useForm({
  initialValues,
  validationSchema: toTypedSchema(validationSchema)
})
const loading = ref(false)

/**
 * Function
 */

async function getItem () {
  try {
    loading.value = true

    const data = await UserService.detail(props.id!)

    setValues({
      ...data,
      role: { value: data.role, label: UserRoleLabel[data.role] },
      birthday: new Date(data.birthday + 'T00:00:00')
    })
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  } finally {
    loading.value = false
  }
}

const handleSubmit = submit(async (values) => {
  try {
    loading.value = true
    let message

    const data = {
      ...values,
      role: values.role.value,
      birthday: format(values.birthday, 'yyyy-MM-dd')
    }

    if (props.id) {
      await UserService.update({ id: props.id, ...data })
      message = 'Usuário atualizada com sucesso'
    } else {
      await UserService.create(data)
      message = 'Usuário criada com sucesso'
    }

    toast({ type: 'success', message })

    router.push({ name: 'user' })
  } catch (e) {
    const error = e as FetchError<Response | Record<string, string[]>>

    if (error.status === 400) {
      const data = error.data as Record<string, string[]>

      if ('non_field_errors' in data) {
        data.email = data.non_field_errors
      }

      setErrors(data)
    }

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  } finally {
    loading.value = false
  }
})

/**
 * Lifecycle
 */

onMounted(() => (props.id && getItem()))
</script>
