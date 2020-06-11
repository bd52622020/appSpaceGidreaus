def print_prime(limit):
   
    for num in range(2, limit+1): 
            is_prime = True
            for i in range(2,num):
                if (num % i) == 0: 
                    is_prime = False
                    break       
            if is_prime:
                print(num, end= " ") 
                
print_prime(15)