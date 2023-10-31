<script setup lang="ts">
import { useVModel } from '@vueuse/core'
import { Pagination, PaginationList, PaginationListItem } from '.'
import type { Meta } from '~/types'

interface Props {
  meta: Meta
  modelValue: number
}

const props = defineProps<Props>()

const emits = defineEmits<{
  'update:modelValue': [number]
}>()

const binding = useVModel(props, 'modelValue', emits, {
  passive: true,
  defaultValue: 1
})
</script>

<template>
  <Pagination
    v-show="meta.pages > 1"
    v-slot="{ page }"
    :total="meta.pages"
    :items-per-page="1"
    :sibling-count="1"
    show-edges
    @update:page="binding = $event"
  >
    <PaginationList v-slot="{ items }" class="flex justify-center items-center gap-1">
      <UiPaginationFirst />
      <UiPaginationPrev />

      <template v-for="(item, index) in items">
        <PaginationListItem v-if="item.type === 'page'" :key="index" :value="item.value" as-child>
          <UiButton class="w-10 h-10 p-0" :variant="item.value === page ? 'default' : 'outline'">
            {{ item.value }}
          </UiButton>
        </PaginationListItem>
        <UiPaginationEllipsis v-else :key="item.type" :index="index" />
      </template>

      <UiPaginationNext />
      <UiPaginationLast />
    </PaginationList>
  </Pagination>
</template>
