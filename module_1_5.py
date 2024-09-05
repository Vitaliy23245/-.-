immutable_var=1,2,3,4 # 1st program
print(immutable_var)
#immutable_var[1]=6#2nd program данный кортедж не поддерживает обращения по элементам
mutable_list=[1,2,[3,4]]
mutable_list[2] =4
mutable_list.append(6)
print('mutable_list:',mutable_list,'Modified')