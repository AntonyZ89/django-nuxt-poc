<template>
  <UiCard>
    <UiCardContent class="p-3 relative">
      <UiButton
        :ref="({ element }) => buttonRef = element"
        class="md:hidden"
        @click="menu = !menu"
      >
        <Menu />
      </UiButton>

      <UiCard
        ref="menuRef"
        as="menu"
        class="transition-all absolute mt-6 inset-x-0 z-10 p-3 md:hidden flex flex-col justify-between gap-y-3"
        :class="{ 'visible opacity-100': menu, 'invisible opacity-0': !menu }"
      >
        <NavbarLeft />
        <NavbarRight />
      </UiCard>

      <div class="hidden md:flex flex-row justify-between gap-x-3">
        <NavbarLeft />
        <NavbarRight />
      </div>
    </UiCardContent>
  </UiCard>
</template>

<script setup lang="ts">
import { onClickOutside } from '@vueuse/core'
import { Menu } from 'lucide-vue-next'

const menu = ref(false)
const menuRef = ref<HTMLMenuElement>()
const buttonRef = ref<HTMLButtonElement>()

watch(menu, () => {
  const cancelClickOutside = onClickOutside(menuRef, (e) => {
    cancelClickOutside?.()
    const target = e.target as HTMLElement | null
    const button = target?.closest('button')

    button !== buttonRef.value && (menu.value = false)
  })
})
</script>
