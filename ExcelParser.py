import pandas as pd

path = "StorageDatabase/Result_7.xls"
data = pd.read_excel(open(path, 'rb',))
df_whs = pd.DataFrame(data, columns=['whs', 'qtys'])
whs_list = []
qtys_list = [[]]
for i in range(len(df_whs)):

    whs_temp = df_whs['whs'][i]
    whs_temp = whs_temp.split(',')
    qtys_temp = df_whs['qtys'][i]
    qtys_temp = qtys_temp.split(',')

    for j in range(len(whs_temp)):

        whs_temp[j] = whs_temp[j].replace('[','')
        whs_temp[j] = whs_temp[j].replace(']','')
        qtys_temp[j] = qtys_temp[j].replace('[', '')
        qtys_temp[j] = qtys_temp[j].replace(']', '')

        if whs_temp[j] not in whs_list:
            whs_list.append(whs_temp[j])
            qtys_list.append([])

        index = whs_list.index(whs_temp[j])
        value = qtys_temp[j]
        qtys_list[index].append((value))



whs_list = whs_list[:-1]
qtys_list = qtys_list[:-1]

print(whs_list)
for a in range(len(qtys_list) - 1):
    print(qtys_list[a])


