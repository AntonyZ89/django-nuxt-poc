<template>
  <LoadingScreen>
    <main>
      <div class="flex flex-col container space-y-3 p-3 h-screen">
        <Navbar />

        <div class="flex flex-col flex-1">
          <slot />
        </div>

        <!-- <Footer /> -->
        <Toaster />
      </div>
    </main>
  </LoadingScreen>
</template>
