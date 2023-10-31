<script setup lang="ts">
import { cn } from '@/lib/utils'

const props = defineProps<{ class?: string }>()
</script>

<template>
  <UiCard>
    <UiCardContent class="p-0">
      <div class="w-full overflow-auto">
        <table :class="cn('w-full caption-bottom text-sm', props.class)">
          <slot />
        </table>
      </div>
    </UiCardContent>
  </UiCard>
</template>
