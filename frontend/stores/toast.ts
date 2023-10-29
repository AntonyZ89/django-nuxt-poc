interface Message {
  type: 'success' | 'error'| 'warning' | 'info'
  title?: string
  message: string
}

interface StorageMessage extends Message {
  remove (): void
}

const useToast = defineStore('toast', () => {
  const messages = ref<Array<StorageMessage>>([])

  function toast (message: Message) {
    const obj = {
      ...message,
      remove () {
        const index = messages.value.indexOf(obj)

        if (index !== -1) {
          messages.value.splice(index, 1)
        }
      }
    }

    messages.value.push(obj)

    setTimeout(obj.remove, 5000)
  }

  return { messages, toast }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useToast, import.meta.hot))
}

export { useToast }
