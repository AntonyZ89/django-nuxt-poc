<template>
  <UiCard class="flex-1">
    <UiCardContent class="h-full space-y-3 flex flex-col text-center justify-center items-center p-3">
      <h1 class="text-4xl font-bold">
        {{ t('welcome') }}
      </h1>

      <h2 class="text-2xl">
        {{ t('description') }}
      </h2>
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
const { t } = useI18n()
</script>

<i18n lang="json">
{
    "en": {
        "welcome": "Welcome",
        "description": "to the system of managing classes"
    },
    "pt": {
        "welcome": "Bem-vindo",
        "description": "ao sistema de gerenciamento de turmas"
    },
    "es": {
        "welcome": "Bienvenido",
        "description": "al sistema de gestión de clases"
    }
}
</i18n>
