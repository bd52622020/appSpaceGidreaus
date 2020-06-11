class User:
    
    strng = ""
        
    def get_String(self,strng):
        self.strng = input("Please enter a string: ")
    
    def print_String(self):
        print(self.strng.upper())
        
print("Q2")       
us = User()
us.get_String("string")
us.print_String()