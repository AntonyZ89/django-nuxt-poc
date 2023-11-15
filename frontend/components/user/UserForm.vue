<template>
  <form @submit.prevent="handleSubmit">
    <UiCard v-if="values">
      <UiCardContent v-auto-animate class="p-3 space-y-3">
        <div>
          <UiLabel for="name">
            {{ $t('user.field.name') }}
          </UiLabel>
          <UiInput name="name" :disabled="loading" />
          <UiInputError name="name" />
        </div>
        <div>
          <UiLabel for="email">
            {{ $t('user.field.email') }}
          </UiLabel>
          <UiInput name="email" type="email" :disabled="loading" />
          <UiInputError name="email" />
        </div>
        <div>
          <UiLabel for="birthday">
            {{ $t('user.field.birthday') }}
          </UiLabel>
          <UiDate name="birthday" :disabled="loading" />
          <UiInputError name="birthday" />
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
            :disabled="loading || !!id"
            :placeholder="$t('select')"
          />
          <UiInputError name="role" />
        </div>
        <div>
          <UiLabel for="password">
            {{ id ? $t('user.field.new_password'): $t('user.field.password') }}
          </UiLabel>
          <UiInput name="password" :disabled="loading" type="password" />
          <UiInputError name="password" />
        </div>
        <div v-if="values.password">
          <UiLabel for="password_confirmation">
            {{ $t('user.field.password_confirmation') }}
          </UiLabel>
          <UiInput name="password_confirmation" :disabled="loading" type="password" />
          <UiInputError name="password_confirmation" />
        </div>

        <div class="text-right">
          <UiButton :loading="loading">
            {{ id ? $t('update'): $t('create') }}
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
import { UserRole, UserRoleList } from '~/types'

interface Props {
  id?: number
}

const props = withDefaults(defineProps<Props>(), {
  id: undefined
})

const { toast } = useToast()
const router = useRouter()
const { t } = useI18n()

const validationSchema = z.object({
  name: z.string().min(3, t('user.validation.name')),
  email: z.string().email(t('user.validation.email')),
  role: z.object({
    value: z.nativeEnum(UserRole),
    label: z.string()
  }, { required_error: t('user.validation.role') }),
  birthday: z.date({ required_error: t('user.validation.birthday') }),
  password: z.string().min(6, t('user.validation.password_min')).optional(),
  password_confirmation: z.string().optional()
}).superRefine((data, context) => {
  if (!props.id) {
    if (!data.password) {
      context.addIssue({
        path: ['password'],
        code: z.ZodIssueCode.custom,
        message: t('user.validation.password')
      })
    } else if (data.password.length < 6) {
      context.addIssue({
        path: ['password'],
        code: z.ZodIssueCode.custom,
        message: t('user.validation.password.min')
      })
    }
  }

  if (data.password !== data.password_confirmation) {
    context.addIssue({
      path: ['password_confirmation'],
      code: z.ZodIssueCode.custom,
      message: t('user.validation.password_confirmation')
    })
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
      role: UserRoleList.find(role => role.value === data.role)!,
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

    const message = error.data?.message as string || 'Ocorreu um erro, tente novamente'

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
