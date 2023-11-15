<template>
  <UiCard v-if="item">
    <UiCardHeader class="pb-0 justify-between">
      <UiCardTitle>
        {{ item.name }}
      </UiCardTitle>

      <div class="text-sm">
        <div>
          {{ $t('discipline.field.teacher') }}: <b>{{ item.teacher_obj.name }}</b>
        </div>

        <div>
          {{ $t('discipline.field.workload') }}: <b>{{ item.workload }}h</b>
        </div>
      </div>
    </UiCardHeader>
    <UiCardContent class="p-3 space-y-3">
      <DisciplineViewStudentTable :discipline-students="item.students" />
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
const route = useRoute()
const disciplineViewStore = useDisciplineViewStore()

const item = computed(() => disciplineViewStore.item)

onMounted(() => {
  const id = Number(route.params.id as string)
  disciplineViewStore.load(id)
})
</script>
