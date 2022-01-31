import pandas as pd
import ast
path = "StorageDatabase/quantities_v2.xls"
data = pd.read_excel(open(path, 'rb', ))
df_whs = pd.DataFrame(data, columns=['whs', 'qtys', 'size_code'])
whs_list = []
qtys_list = []
j = 0
print(data)


for i in range(len(df_whs)):

    whs_temp = df_whs['whs'][i]
    qtys_temp = df_whs['qtys'][i]

    if whs_temp not in whs_list:
        whs_list.append(whs_temp)
        qtys_list.append([])

    qtys_temp = qtys_temp.replace("','", '')

    qtys_temp = qtys_temp.split(',')
    for j in range(len(qtys_temp)):
        qtys_temp[j] = qtys_temp[j].replace('[', '')
        qtys_temp[j] = qtys_temp[j].replace(']', '')

    index = whs_list.index(whs_temp)
    value = qtys_temp

    qtys_list[index].append((value))

results = []

def logic(a):
    counter = 0

    for i in range(len(qtys_list)):
        for j in range(len(qtys_list[i])):
            total = 0
            sold = 0

            for k in range(len(qtys_list[i][j]) - 1):
                value = int(qtys_list[i][j][k]) - int(qtys_list[i][j][k + 1])
                initial = int(qtys_list[i][j][0]) - int(qtys_list[i][j][-1])
                if value > 0:
                    # print('найдено положительное отклонение в размере ' + str(abs(value)))
                    if abs(value) >= 7:
                        pass
                    else:
                        sold -= value
                if value < 0:
                    # print('найдено отрицательное отклонение в размере ' + str(abs(value)))
                    if abs(value) >= 7:
                        pass
                    else:
                        sold += value

                if value not in results:
                    results.append(value)
            # print('index of item ' + str(i) + str(j) + str(k))
            # print('real number of items sold ' + str(sold))
            # print('sold without correction ' + str(initial))
                total += sold
                # if sold != initial:
                #     print('item with unexpected value on index ' + str(i) + str(j) + str(k))
                    # print('expected sales = '+ str(initial) + ' corrected sales = ' + str(sold))
                # print((total))
                print(sold)
                counter += 1

    return print('calculation complete ' + str(counter))

# print(logic(qtys_list))

print()
# for i in range(len(df_whs)):
#     print(df_whs['a'][i])