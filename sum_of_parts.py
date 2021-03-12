def parts_sums(ls):
    total = sum(ls)
    arr = [total]
    for i in range(len(ls)):
        total -= ls[i]
        arr.append(total)
    return arr
