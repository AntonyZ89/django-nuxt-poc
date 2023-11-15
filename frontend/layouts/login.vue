<template>
  <LoadingScreen>
    <main class="h-screen flex flex-col justify-center items-center">
      <Toaster />
      <slot />

      <LangSwitcher class="mt-3 mr-7" />
    </main>
  </LoadingScreen>
</template>
