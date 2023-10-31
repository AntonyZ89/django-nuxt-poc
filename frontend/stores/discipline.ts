import type { FetchError } from 'ofetch'
import { DisciplineService } from '~/services'
import type { Meta, Discipline, Response } from '~/types'

type FilterType = Partial<Pick<Discipline, 'name'> & { teacher: string }>

const useDisciplineStore = defineStore('discipline', () => {
  const items = ref<Array<Discipline>>([])
  const filter = ref<FilterType>({ name: '', teacher: '' })
  const meta = ref<Meta>({ count: 0, page: 1, pages: 1, per_page: 10 })

  const { toast } = useToast()

  function handlePage (page: number) {
    if (page === meta.value.page || page < 1 || page > meta.value.pages) {
      return
    }

    meta.value.page = page
    load()
  }

  async function load () {
    try {
      const { results, ...rest } = await DisciplineService.list({
        ...filter.value,
        ...meta.value
      })

      items.value = results
      meta.value = rest
    } catch (e) {
      const error = e as FetchError<Response>
      const message = error.data?.message || 'Erro ao carregar as disciplinas'

      toast({ message, type: 'error' })
    }
  }

  watch(filter, () => {
    meta.value.page = 1

    load()
  })

  return {
    items,
    filter,
    meta,
    load,
    handlePage
  }
})

export { useDisciplineStore }
