import pandas as pd
import ast


path = "StorageDatabase/quantities_v2.xls"
data = pd.read_excel(open(path, 'rb', ))
df_whs = pd.DataFrame(data, columns=['whs', 'qtys', 'size_code'])
whs_list = []
qtys_list = []
j = 0
print(data)

for i in range(len(df_whs['qtys'])):
    qtys_temp = df_whs['qtys'][i]
    qtys_list.append(ast.literal_eval(qtys_temp))


def logic(a):
    counter = 0

    for i in range(len(qtys_list)):
        total = 0
        sold = 0
        for j in range(len(qtys_list[i]) - 1):
            value = int(qtys_list[i][j]) - int(qtys_list[i][j + 1])
            if value > 0:

                if abs(value) >= 7:
                    pass
                else:
                    sold += value
            # if value < 0:                 по просьбе сереги пока не надо
            #
            #     if abs(value) >= 7:
            #         pass
            #     else:
            #         sold += value
        print(sold)
        counter += 1

    return 'calculation complete ' + str(counter)


print(logic(qtys_list))
