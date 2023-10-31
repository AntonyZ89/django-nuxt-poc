<template>
  <li>
    <NuxtLink :to="to">
      <UiButton :variant="focused ? 'default' : 'outline'" @click="$emit('click')">
        {{ name }}
      </UiButton>
    </NuxtLink>
  </li>
</template>

<script setup lang="ts">
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
