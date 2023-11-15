<script setup lang="ts">
import { ptBR } from 'date-fns/locale'
import { format } from 'date-fns'
import { Calendar as CalendarIcon } from 'lucide-vue-next'
import { cn } from '@/lib/utils'

interface Props {
  name: string,
  placeholder?: string
}

const props = defineProps<Props>()
const emits = defineEmits<{
  'update:modelValue': [Date]
}>()

const { value } = useField<Date>(props.name)

const binding = computed({
  get: () => value.value,
  set: (v) => {
    emits('update:modelValue', v)
    value.value = v
  }
})
</script>

<template>
  <UiPopover>
    <UiPopoverTrigger as-child>
      <div>
        <UiButton
          type="button"
          variant="outline"
          :class="cn(
            'justify-start w-full text-left font-normal',
            !binding && 'text-muted-foreground',
          )"
        >
          <CalendarIcon class="inline-block mr-2 h-4 w-4" />
          <span>{{ binding ? format(binding, "PPP", { locale: ptBR }) : placeholder }}</span>
        </UiButton>
      </div>
    </UiPopoverTrigger>
    <UiPopoverContent class="w-auto p-0">
      <UiCalendar v-model="binding" />
    </UiPopoverContent>
  </UiPopover>
</template>
