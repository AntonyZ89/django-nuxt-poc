<template>
  <template v-if="can">
    <slot />
  </template>
</template>

<script setup lang="ts">
import type { User } from '~/types'

interface Props {
  role: `${User['role']}` | `${User['role']}`[]
}

const globalStore = useGlobalStore()

const props = defineProps<Props>()

/**
 * Computed
 */

const can = computed(() => {
  const role = Array.isArray(props.role) ? props.role : [props.role]

  return globalStore.user && role.includes(globalStore.user.role)
})
</script>
