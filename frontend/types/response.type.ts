interface Response {
  message: string
}

interface Meta {
  count: number,
  per_page: number
  page: number,
  pages: number,
}

interface ResponseList<T> extends Meta {
  results: T[]
}

interface ResponseWithError extends Response {
  errors: Record<string, string>
}

export type {
  Response,
  ResponseList,
  ResponseWithError,
  Meta
}
