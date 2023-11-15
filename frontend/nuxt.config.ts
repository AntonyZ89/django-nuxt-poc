// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  typescript: {
    shim: false,
    strict: true
  },

  modules: [
    '@nuxtjs/i18n',
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
  ],

  i18n: {
    lazy: true,
    langDir: 'lang',
    strategy: 'no_prefix',
    locales: [
      { code: 'en', file: 'en-US.json', name: 'English' },
      { code: 'es', file: 'es-ES.json', name: 'Espãnol' },
      { code: 'pt', file: 'pt-BR.json', name: 'Português' }
    ],
    detectBrowserLanguage: {
      useCookie: true
    }
  }
})
