<template>
  <form @submit.prevent="handleSubmit">
    <UiCard v-if="values">
      <UiCardHeader class="space-y-2">
        <div>
          <UiLabel for="name">
            Nome
          </UiLabel>
          <UiInput name="name" :disabled="loading" placeholder="Nome" />
          <UiInputError name="name" />
        </div>

        <div class="lg:w-[200px] space-y-2">
          <div>
            <UiLabel for="teacher">
              Professor
            </UiLabel>
            <UiSelect :items="teachers" :disabled="loading" name="teacher" object-value="name" placeholder="Professor" />
            <UiInputError name="teacher" />
          </div>

          <div>
            <UiLabel for="workload">
              Carga horária
            </UiLabel>
            <UiInput name="workload" :disabled="loading" placeholder="Carga horária" type="number" />
            <UiInputError name="workload" />
          </div>
        </div>
      </UiCardHeader>
      <UiCardContent class="space-y-3">
        <h1 class="text-xl font-bold">
          Estudantes
        </h1>

        <div v-auto-animate class="space-y-2">
          <div v-for="student in values.students" :key="student.user_obj.id" class="flex items-center gap-x-2">
            <UiButton
              type="button"
              variant="destructive"
              class="p-1 rounded-full h-auto hover:scale-110 transition-all"
              :disabled="loading"
              @click="handleRemove(student)"
            >
              <MinusCircle class="h-4 w-4" />
            </UiButton>

            <div class="flex items-center">
              {{ student.user_obj.name }}
            </div>
          </div>

          <div v-if="selecting" class="flex items-center gap-x-2 w-[300px]">
            <UiButton
              type="button"
              class="p-1 rounded-full h-auto hover:scale-110 transition-all bg-gray-300 hover:bg-gray-300/80 text-black"
              :disabled="loading"
              @click="select(false)"
            >
              <XCircle class="h-4 w-4" />
            </UiButton>

            <UiSelect name="student" :items="users" placeholder="Selecionar aluno" object-value="name" />

            <UiButton
              type="button"
              class="p-1 rounded-full bg-green-400 hover:bg-green-400 h-auto hover:scale-110 transition-all"
              :disabled="loading || !values.student"
              @click="handleAdd"
            >
              <CheckCircle2 class="h-4 w-4" />
            </UiButton>
          </div>

          <div v-else>
            <UiButton
              type="button"
              class="p-1 bg-green-400 font-bold rounded-full px-2 h-auto transition-all hover:scale-105 hover:bg-green-400"
              :disabled="loading || !users.length"
              @click="select(true)"
            >
              <PlusCircle class="h-4 w-4 mr-1" /> Adicionar
            </UiButton>
          </div>

          <UiInputError name="students" />

          <div v-if="!users.length">
            Todos os estudantes disponíveis já foram selecionados
          </div>
        </div>

        <div class="text-right">
          <UiButton :disabled="selecting" :loading="loading">
            {{ id ? 'Atualizar' : 'Criar' }}
          </UiButton>
        </div>
      </UiCardContent>
    </UiCard>
  </form>
</template>

<script setup lang="ts">
import type { FetchError } from 'ofetch'
import { MinusCircle, PlusCircle, XCircle, CheckCircle2 } from 'lucide-vue-next'
import { z } from 'zod'
import { DisciplineService, UserService } from '~/services'
import type { Response } from '~/types'
import { UserRole } from '~/types'

interface Props {
  id?: number
}

const props = withDefaults(defineProps<Props>(), {
  id: undefined
})

const { toast } = useToast()
const router = useRouter()

const validationSchema = z.object({
  name: z.string().min(1, 'Nome é obrigatório.'),
  teacher: z.object({
    id: z.number(),
    name: z.string()
  }, { required_error: 'Professor é obrigatório.' }),
  workload: z.number({ coerce: true }).min(1, 'Preencha o campo de carga horária.'),
  students: z.array(
    z.object({
      user_obj: z.object({
        id: z.number(),
        name: z.string()
      })
    })
  ).min(1, 'Preencha o campo de estudantes.'),
  student: z.object({
    id: z.number(),
    name: z.string()
  }).optional()
})

type Schema = z.infer<typeof validationSchema>

const initialValues = {
  name: '',
  teacher: undefined,
  workload: undefined,
  students: []
}

const { values, setValues, setFieldValue, setErrors, handleSubmit: submit } = useForm({
  initialValues,
  validationSchema: toTypedSchema(validationSchema)
})
const selecting = ref(false)
const loading = ref(false)
const userList = ref<Schema['students'][number]['user_obj'][]>([])
const teachers = ref<Schema['teacher'][]>([])
const removedUsers = ref<Schema['students'][number]['user_obj'][]>([])

const users = computed(
  () => userList.value.filter(
    user => values.students!.findIndex(student => student.user_obj.id === user.id) === -1
  ).concat(removedUsers.value)
)

/**
 * Function
 */

async function getItem () {
  try {
    loading.value = true

    const data = await DisciplineService.detail({
      id: props.id!,
      expand: ['students']
    })

    setValues({
      ...data,
      teacher: data.teacher_obj
    })
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  } finally {
    loading.value = false
  }
}

async function getUsers () {
  try {
    const data = await UserService.list({
      per_page: -1,
      role: UserRole.STUDENT,
      not_discipline: props.id
    })

    userList.value = data.results
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  }
}

function select (value: boolean) {
  selecting.value = value

  setFieldValue('student', undefined)
}

async function getTeachers () {
  try {
    const data = await UserService.list({
      per_page: -1,
      role: UserRole.TEACHER
    })

    teachers.value = data.results
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || 'Ocorreu um erro, tente novamente'

    toast({ type: 'error', message })
  }
}

function handleAdd () {
  const user = values.student as Required<NonNullable<typeof values.student>>
  setFieldValue('students', [
    ...values.students || [],
    { user_obj: user }
  ])

  if (!users.value.length) {
    select(false)
  } else {
    const previousDeleted = removedUsers.value.findIndex(student => student.id === user.id)

    if (previousDeleted !== -1) {
      removedUsers.value.splice(previousDeleted, 1)
    }

    setFieldValue('student', undefined)
  }
}

function handleRemove (item: Schema['students'][number]) {
  const students = values.students || []

  if (userList.value.findIndex(student => student.id === item.user_obj.id) === -1) {
    removedUsers.value.push(item.user_obj)
  }

  setFieldValue('students', students.filter(student => student.user_obj.id !== item.user_obj.id))
}

const handleSubmit = submit(async (values) => {
  try {
    loading.value = true
    let message

    if (props.id) {
      await DisciplineService.update({
        id: props.id,
        ...values,
        teacher: values.teacher.id,
        students: values.students.map(student => student.user_obj.id)
      })
      message = 'Disciplina atualizada com sucesso'
    } else {
      await DisciplineService.create({
        ...values,
        teacher: values.teacher.id,
        students: values.students.map(student => student.user_obj.id)
      })
      message = 'Disciplina criada com sucesso'
    }

    toast({ type: 'success', message })

    router.push({ name: 'discipline' })
  } catch (e) {
    const error = e as FetchError<Response | Record<string, string>>

    if (error.status === 400) {
      setErrors(error.data as Record<string, string>)
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

onMounted(() => {
  props.id && getItem()

  getUsers()
  getTeachers()
})
</script>
