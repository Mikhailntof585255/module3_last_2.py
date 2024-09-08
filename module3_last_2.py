data_structure = [[1,2,3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def slovar_list(arg):                   # словарь в список, сумма элементов списка
    keys_ = list(arg.keys())
    value_ = list(arg.values())
    perem = keys_ + value_
    itog=0;sum_1=0;sum_2=0;n=0
    for n in range(len(perem)):
        if isinstance(perem[n], int):
            sum_1 += perem[n]
        if isinstance(perem[n], str):
            sum_2 += len(perem[n])
        itog=sum_1+sum_2
    return itog


def summa_spisok(arg):                    #cумма элементов списка
    perem=arg
    itog = 0
    sum_1 = 0
    sum_2 = 0
    n = 0
    for n in range(len(perem)):
        if isinstance(perem[n], int):
            sum_1 += perem[n]
        if isinstance(perem[n], str):
            sum_2 += len(perem[n])
        itog = sum_1 + sum_2
    return itog

def summa_tuple_(arg):                   #сумма элементов кортежа
    itog=0;sum_1=0;sum_2=0;j=0
    itog_1=0
    itog_1 = itog_1+arg[j]
    j+=1
    if isinstance(arg[j], dict):
        itog_2=slovar_list(arg[j])      #элемент кортежа словарь в список, сумма элементов списка
    itog=+itog_1+itog_2
    return itog

def element_5(arg):                     #распаковка 5 элемента в списке
    kort_1=arg[1]
    kort_2=kort_1[0]
    kort_3=kort_2.pop()
    kort_4=kort_3[0]
    kort_5=kort_3[1]
    kort_6=kort_3[2]
    kort_7=kort_6[0]
    kort_8=kort_6[1]
    list_kort=[]
    list_kort=[kort_4,kort_5,kort_7,kort_8]
    rezul=summa_spisok(list_kort)
    return rezul

def calculate_structure_sum(arg):
    i=0
    rez1=summa_spisok(arg[i])
    i+=1
    rez2=slovar_list(arg[i])
    i+=1
    rez3=summa_tuple_(arg[i])
    i+=1
    rez4=summa_spisok(arg[i])
    i+=1
    rez5=element_5(arg[i])
    itog_itogov=rez1+rez2+rez3+rez4+rez5
    return itog_itogov


rezult=calculate_structure_sum(data_structure)
print(rezult)


