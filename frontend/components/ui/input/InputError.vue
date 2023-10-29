<script setup lang="ts">
interface Props {
  name: string
}

const props = defineProps<Props>()

const { errorMessage } = useField(props.name)
</script>

<template>
  <small v-if="errorMessage" class="text-red-500">
    {{ errorMessage }}
  </small>
</template>
