<script setup lang="ts">
import type { DefineComponent, ConcreteComponent } from 'vue'
import { buttonVariants } from '.'
import { cn } from '@/lib/utils'

interface Props {
  variant?: NonNullable<Parameters<typeof buttonVariants>[0]>['variant']
  size?: NonNullable<Parameters<typeof buttonVariants>[0]>['size']
  as?: string | DefineComponent | ConcreteComponent
  disabled?: boolean
  loading?: boolean
}

const element = ref<HTMLElement>()

withDefaults(defineProps<Props>(), {
  as: 'button'
})

defineExpose({ element })
</script>

<template>
  <component
    :is="as"
    ref="element"
    :class="cn(buttonVariants({ variant, size }), $attrs.class ?? '')"
    :disabled="disabled || loading"
  >
    <slot />
  </component>
</template>
