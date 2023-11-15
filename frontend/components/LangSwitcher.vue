<template>
  <div class="flex gap-x-3 items-center">
    <Languages />
    <UiSelect
      :value="selected"
      :items="locales as LocaleObject[]"
      object-key="code"
      object-value="name"
      @update:model-value="setLocale($event.code)"
    />
  </div>
</template>

<script setup lang="ts">
import type { LocaleObject } from '@nuxtjs/i18n/dist/runtime/composables'
import { Languages } from 'lucide-vue-next'
const { locale, setLocale, locales } = useI18n()

const selected = computed(
  () => (locales.value as LocaleObject[]).find(lang => lang.code === locale.value)
)
</script>
