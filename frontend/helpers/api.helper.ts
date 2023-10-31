function parseExpand (value?: { expand?: string[] }) {
  let expand: string | undefined

  if (value && 'expand' in value) {
    expand = value.expand?.join(',')
  }

  return expand
}

export default {
  parseExpand
}
