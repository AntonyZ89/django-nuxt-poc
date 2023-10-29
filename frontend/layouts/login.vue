<template>
    <LoadingScreen>
        <main class="h-screen flex flex-col justify-center items-center">
            <Toaster />
            <slot />
        </main>
    </LoadingScreen>
</template>
