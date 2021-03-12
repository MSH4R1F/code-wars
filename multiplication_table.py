def multiplication_table(size):
    table = []
    for row in range(1,size+1):
        for column in range(1,size+1):
            table.append(row*column)
    return [table[x:x+size] for x in range(0, len(table),size)]
