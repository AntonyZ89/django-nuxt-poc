<template>
  <li>
    <UiButton
      :as="NuxtLink"
      :to="to"
      class="md:inline-flex flex"
      :variant="focused ? 'default' : 'outline'"
      @click="$emit('click')"
    >
      {{ name }}
    </UiButton>
  </li>
</template>

<script setup lang="ts">
import { NuxtLink } from '#components'

interface IProps {
  to?: string | { path: string, params?: Record<string, string | number> },
  name: string
}

const props = defineProps<IProps>()
defineEmits<{
  click: []
}>()

const route = useRoute()

/**
 * Computed
 */

const focused = computed(
  () => {
    if (!props.to) {
      return false
    }

    return route.path === (typeof props.to === 'string' ? props.to : props.to.path)
  }
)
</script>
