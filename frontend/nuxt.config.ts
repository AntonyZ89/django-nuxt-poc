// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  typescript: {
    shim: false,
    strict: true
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@vee-validate/nuxt',
    [
      '@pinia/nuxt',
      {
        autoImports: ['defineStore', 'acceptHMRUpdate']
      }
    ]
  ],

  imports: {
    dirs: ['stores', 'helpers']
  },

  components: [
    '~/components',
    {
      path: '~/components/ui',
      extensions: ['.vue'],
      prefix: 'Ui'
    }
  ]
})
