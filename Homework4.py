immutable_war = (1, 3, 5, 'a', 'b', 'c') #пример кортежа
print(immutable_war)
print(immutable_war[2])  #из кортежа можно взять индексируемые данные
#immutable_war.append(73) #кортеж относится к неизменяемым обьектам и его нельзя редактировать или изменять
#print(immutable_war)
#immutable_war.remove('b') #так же из кортежа нельзя удалять данные
#print(immutable_war)
#immutable_war[1] = 25 #обращение по элементам в кортежах так же не поддерживается
#print(immutable_war)

mutable_list = [2, 19, 'cat', 73, 'dress']
print(mutable_list)
mutable_list.append(666)
print(mutable_list) #в списки можно добавлять новые данные, а так же удалять и изменя имеющиеся