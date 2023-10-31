<template>
  <UiCard v-if="item">
    <UiCardHeader class="pb-0 justify-between">
      <UiCardTitle>
        {{ item.name }}
      </UiCardTitle>

      <div class="text-sm">
        <div>
          Professor: <b>{{ item.teacher_obj.name }}</b>
        </div>

        <div>
          Carga horária: <b>{{ item.workload }}h</b>
        </div>
      </div>
    </UiCardHeader>
    <UiCardContent class="p-3 space-y-3">
      <DisciplineViewStudentTable />
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { DisciplineService } from '~/services'
import type { Discipline } from '~/types'

const route = useRoute()

const item = ref<RequiredSelect<Discipline, 'students'>>()

onMounted(async () => {
  const id = Number(route.params.id as string)
  item.value = await DisciplineService.detail({ id, expand: ['students'] })
})
</script>
