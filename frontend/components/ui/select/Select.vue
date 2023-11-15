<script setup lang="ts" generic="T extends object | undefined">
import { useVModel } from '@vueuse/core'
import type { SelectRootEmits, SelectRootProps } from 'radix-vue'
import { SelectRoot, useForwardPropsEmits } from 'radix-vue'
import type { FieldContext } from 'vee-validate'

interface Props extends Omit<SelectRootProps, 'modelValue'> {
  value?: T
  modelValue?: T
  items: Array<T>
  placeholder?: string
  objectKey?: string
  objectValue: string
  name?: string
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  value: undefined,
  modelValue: undefined,
  placeholder: undefined,
  name: '',
  objectKey: 'id'
})
const emits = defineEmits<
  Omit<SelectRootEmits, 'update:modelValue'>
    & { 'update:modelValue': [T] }
>()

const forwarded = useForwardPropsEmits(props, emits)
const { value: fieldValue } = useField<string | number>(props.name)

const modelValue = useVModel(props, 'modelValue', emits, {
  passive: true,
  // @ts-ignore
  defaultValue: props.defaultValue
})

const binding = computed({
  get: () => props.value || modelValue.value || fieldValue?.value,
  set: (v) => {
    // @ts-ignore
    emits('update:modelValue', v)
    fieldValue && (fieldValue.value = v)
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
    // @ts-ignore
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
