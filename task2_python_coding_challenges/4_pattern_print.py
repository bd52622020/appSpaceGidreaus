def construct_pattern():
    
    d, sym_qnt = 1, 0
    
    for i in range(9):
        
        sym_qnt += d
        if sym_qnt ==5:
            d = -1
        for i in range(sym_qnt):
            print("*", end="")
        print("")

construct_pattern()