a = {1:10, 2:20} 
b ={3:30, 4:40} 
c = {5:50,6:60}

conc_dict = dict(a)
[conc_dict.update(d) for d in [b,c]]
print("Dicts:", a, b, c, ". Concatenated dictionary:", conc_dict)