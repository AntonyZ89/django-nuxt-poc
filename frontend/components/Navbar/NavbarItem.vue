<template>
  <li>
    <NuxtLink :to="to">
      <UiButton :variant="focused ? 'default' : 'outline'">
        {{ name }}
      </UiButton>
    </NuxtLink>
  </li>
</template>

<script setup lang="ts">
interface IProps {
  to: string | { path: string, params?: Record<string, string | number> },
  name: string
}

const props = defineProps<IProps>()

const route = useRoute()

/**
 * Computed
 */

const focused = computed(
  () => route.path === (typeof props.to === 'string' ? props.to : props.to.path)
)
</script>
