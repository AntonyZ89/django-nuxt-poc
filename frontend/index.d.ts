type RequiredSelect<TObject extends object, TKey extends keyof T> = TObject & Required<Pick<TObject, TKey>>
