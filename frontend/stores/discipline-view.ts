import type { FetchError } from 'ofetch'
import { DisciplineService } from '~/services'
import type { Discipline, Response } from '~/types'

const useDisciplineViewStore = defineStore('disciplineView', () => {
  const item = ref<RequiredSelect<Discipline, 'students'>>()

  const { toast } = useToast()
  const { t } = useI18n()

  async function load (id: Discipline['id']) {
    try {
      const data = await DisciplineService.detail({
        id,
        expand: ['students']
      })

      item.value = data
    } catch (e) {
      const error = e as FetchError<Response>
      const message = error.data?.message || t('occurred_an_error')

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
