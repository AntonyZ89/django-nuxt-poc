<template>
  <UiDialog :open="dialog" @update:open="dialog = $event">
    <UiDialogTrigger as-child>
      <UiButton variant="destructive" class="px-3 h-auto">
        <Trash class="w-4 h-4" />
      </UiButton>
    </UiDialogTrigger>
    <UiDialogContent class="sm:max-w-[425px]">
      <UiDialogHeader>
        <UiDialogTitle>
          {{ title }}
        </UiDialogTitle>
        <UiDialogDescription>
          {{ t('modal.delete.message') }}
        </UiDialogDescription>
      </UiDialogHeader>
      <UiDialogFooter>
        <UiButton variant="destructive" @click="handleRemove">
          {{ t('modal.delete.button') }}
        </UiButton>
      </UiDialogFooter>
    </UiDialogContent>
  </UiDialog>
</template>

<script setup lang="ts">
import { Trash } from 'lucide-vue-next'
import type { FetchError } from 'ofetch'
import type { User, Response } from '~/types'
import { UserService } from '~/services'

interface Props {
  item: Pick<User, 'id' | 'name'>
}

const { t } = useI18n()
const { toast } = useToast()
const props = defineProps<Props>()
const userStore = useUserStore()

const dialog = ref(false)

const title = computed(() => {
  return t('modal.delete.title', [t('page.user').toLowerCase(), props.item.name])
})

/**
 * Function
 */

async function handleRemove () {
  try {
    await UserService.remove(props.item.id)

    toast({ type: 'success', message: t('deleted_successfully', [t('page.user').toLowerCase()]) })

    dialog.value = false

    if (userStore.meta.page > 1 && userStore.items.length === 1) {
      userStore.handlePage(userStore.meta.page - 1)
    } else {
      userStore.load()
    }
  } catch (e) {
    const error = e as FetchError<Response>

    const message = error.data?.message || t('occurred_an_error')

    toast({ type: 'error', message })
  }
}
</script>
