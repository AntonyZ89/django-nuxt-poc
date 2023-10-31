<template>
  <DisciplineForm :id="id" />
</template>

<script setup lang="ts">
const route = useRoute()

const id = computed(() => Number(route.params.id as string))
</script>
