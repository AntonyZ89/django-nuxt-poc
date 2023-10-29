<template>
  <div v-if="globalStore.user === undefined" class="flex items-center justify-center h-screen">
    <div class="max-w-3xl w-[80%]">
      <UiProgress :model-value="progress" class="[transition-duration:_3000ms]" />
    </div>
  </div>
  <slot v-else />
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

const globalStore = useGlobalStore()

const progress = ref(0)

onMounted(() => (progress.value = 100))
</script>
