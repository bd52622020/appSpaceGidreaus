def print_pasckal_trangle(rows):
    line = []
    for i in range(0, rows):
        new_line = [1]
        if i > 1:
            for j in range(i-1):
                new_line.append(sum(line[j:j+2]))
        if i > 0:
            new_line.append(1)
        line = new_line
        [print(e, end=" ") for e in line]
        print("")
        
       
print_pasckal_trangle(8)