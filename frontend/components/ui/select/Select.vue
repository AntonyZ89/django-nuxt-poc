<script setup lang="ts" generic="T extends object">
import { useVModel } from '@vueuse/core'
import { X } from 'lucide-vue-next'
import type { SelectRootEmits, SelectRootProps } from 'radix-vue'
import { SelectRoot, useForwardPropsEmits } from 'radix-vue'

interface Props extends Omit<SelectRootProps, 'modelValue'> {
  modelValue?: T
  items: Array<T>
  placeholder?: string
  objectKey?: string
  objectValue: string
  name?: string
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: undefined,
  placeholder: undefined,
  name: undefined,
  objectKey: 'id'
})
const emits = defineEmits<
  Omit<SelectRootEmits, 'update:modelValue'>
    & { 'update:modelValue': [T] }
>()

const forwarded = useForwardPropsEmits(props, emits)
// @ts-ignore
const { value } = useField<string | number | undefined>(props.name)

const modelValue = useVModel(props, 'modelValue', emits, {
  passive: true,
  defaultValue: props.defaultValue
})

const binding = computed({
  get: () => modelValue.value || value.value,
  set: (v) => {
    emits('update:modelValue', v)
    value.value = v
  }
})

/**
 * Function
 */

function getKey (value: T) {
  // @ts-ignore
  return String(value[props.objectKey])
}

function getValue (value: T) {
  // @ts-ignore
  return String(value[props.objectValue])
}

function handleEmit (value: string) {
  // @ts-ignore
  if (binding.value && value === getKey(binding.value)) {
    binding.value = undefined
    return
  }

  // @ts-ignore
  const item = props.items.find(item => getKey(item) === value)!

  // @ts-ignore
  binding.value = item
}
</script>

<template>
  <SelectRoot v-bind="forwarded">
    <UiSelectTrigger :disabled="disabled">
      <div>
        {{ binding ? getValue(binding) : placeholder }}
      </div>
    </UiSelectTrigger>
    <UiSelectContent>
      <UiSelectItem
        v-for="item in items"
        :key="getKey(item)"
        :value="getKey(item)"
        @click="handleEmit(getKey(item))"
      >
        {{ getValue(item) }}
      </UiSelectItem>
    </UiSelectContent>
  </SelectRoot>
</template>
