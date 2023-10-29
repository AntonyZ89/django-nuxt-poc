<template>
  <div v-auto-animate class="fixed pointer-events-none inset-3 flex flex-col items-end space-y-3">
    <UiCard
      v-for="({ type, title, message, remove }, index) in toast.messages"
      :key="index"
      class="pointer-events-auto cursor-pointer min-w-[200px] max-w-[500px] inline-flex items-center"
      :class="[borderColor[type], backgroundColor[type]]"
      @click="remove"
    >
      <div class="pl-3 py-3" :class="color[type]">
        <component :is="icon[type]" :size="32" :stroke-width="1.25" />
      </div>
      <div class="flex-1">
        <UiCardHeader v-if="title" class="p-3 text-xl font-bold">
          {{ title }}
        </UiCardHeader>
        <UiCardContent class="p-3 pt-0 text-center" :class="[{ 'pt-3': !title }, textColor[type]]">
          {{ message }}
        </UiCardContent>
      </div>
    </UiCard>
  </div>
</template>

<script setup lang="ts">
const toast = useToast()

const color = {
  success: 'text-green-500',
  error: 'text-red-500',
  warning: 'text-yellow-500',
  info: 'text-blue-500'
}

const textColor = {
  success: 'text-green-400',
  error: 'text-red-400',
  warning: 'text-yellow-400',
  info: 'text-blue-400'
}

const borderColor = {
  success: 'border-green-500',
  error: 'border-red-500',
  warning: 'border-yellow-500',
  info: 'border-blue-500'
}

const backgroundColor = {
  success: 'bg-green-50',
  error: 'bg-red-50',
  warning: 'bg-yellow-50',
  info: 'bg-blue-50'
}

const icon = {
  success: defineAsyncComponent(async () => (await import('lucide-vue-next')).CheckCircle2),
  error: defineAsyncComponent(async () => (await import('lucide-vue-next')).XCircle),
  warning: defineAsyncComponent(async () => (await import('lucide-vue-next')).AlertTriangle),
  info: defineAsyncComponent(async () => (await import('lucide-vue-next')).Info)
}
</script>
