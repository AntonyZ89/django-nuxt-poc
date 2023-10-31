<template>
  <UiTableCell>
    {{ item.note_1 ?? '-' }}
  </UiTableCell>
  <UiTableCell>
    {{ item.note_2 ?? '-' }}
  </UiTableCell>
  <UiTableCell>
    {{ item.media ?? '-' }}
  </UiTableCell>
</template>

<script setup lang="ts">
import type { Discipline } from '~/types'

interface Props {
  item: NonNullable<Discipline['students']>[number]
}

defineProps<Props>()
</script>
