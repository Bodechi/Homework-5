#immutable_var = tuple([1, "два", 3.0, True])
#print(immutable_var)
#immutable_var [1] = [123]
#print(immutable_var) # нельзя сменить элемент кортежа , если только в нем нет списка [1,2, и тд], в списке заменить значение возможно .
mutable_list = (["Было", 2, "яблока", "съели", 1, "сколлко осталось ?"], "!")
mutable_list[0][5] = "осталось 1"
print(mutable_list)