import { format as fnsFormat } from 'date-fns'

function formatDatetime (date: string) {
  return fnsFormat(new Date(date), 'dd/MM/yyyy HH:mm:ss')
}

export default {
  formatDatetime
}
