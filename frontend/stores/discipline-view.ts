import type { FetchError } from 'ofetch'
import { DisciplineService } from '~/services'
import type { Discipline, Response } from '~/types'

const useDisciplineViewStore = defineStore('disciplineView', () => {
  const item = ref<RequiredSelect<Discipline, 'students'>>()

  const { toast } = useToast()

  async function load (id: Discipline['id']) {
    try {
      const data = await DisciplineService.detail({
        id,
        expand: ['students']
      })

      item.value = data
    } catch (e) {
      const error = e as FetchError<Response>
      const message = error.data?.message || 'Erro ao carregar a disciplina'

      toast({ message, type: 'error' })
    }
  }

  return {
    item,
    load
  }
})

export {
  useDisciplineViewStore
}
