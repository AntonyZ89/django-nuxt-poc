import type { FetchError } from 'ofetch'
import { UserService } from '~/services'
import type { Meta, User, Response } from '~/types'

type FilterType = Partial<Pick<User, 'name' | 'email' | 'role'>>

const useUserStore = defineStore('user', () => {
  const items = ref<Array<User>>([])
  const filter = ref<FilterType>({ name: '', email: '', role: undefined })
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
      const { results, ...rest } = await UserService.list({
        ...filter.value,
        ...meta.value
      })

      items.value = results
      meta.value = rest
    } catch (e) {
      const error = e as FetchError<Response>
      const message = error.data?.message || 'Erro ao carregar os usuários'

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

export { useUserStore }
