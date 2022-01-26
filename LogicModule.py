whs_list = [507, 2737, 120762]  # unique whs
qtys_list = [[[100, 98, 95, 97, 91, 500, 985, 400]], [], []]  # []*len(whs_list)

quantity = [100, 98, 95, 97, 91, 500, 985, 400]
refund = 0
for i in range(len(quantity) - 1):
    if int(quantity[i]) < int(quantity[i + 1]):
        absolute = quantity[i + 1] - quantity[i]
        relative = quantity[i] / quantity[i + 1]
        print(relative, absolute, quantity[i], quantity[i+1])
        refund += absolute
# print(quantity[0], quantity[-1],refund)
# print((quantity[0] - quantity[-1] + refund))
dump = 0
for i in range(len(quantity) - 1):
    if int(quantity[i]) > int(quantity[i + 1]):
        absolute = quantity[i + 1] - quantity[i]
        relative = quantity[i] / quantity[i + 1]
        # print(relative, absolute, quantity[i], quantity[i + 1])
        dump += absolute


#по вендор коду прогнать алгоритм с 1 по 20 декабря
#функция отсечения абс*рел