import random
letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"
,"x","y","z"]
numbers = ["1","2","3","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","=","+"]
n_letters = int(input("enter no letters? \n"))
n_num = int(input("enter no numbers?\n"))
n_symbol = int(input("enter no symbols?\n"))
 
letters_p = ""
num_p = ""
sym_p = ""
for letter in range(1,n_letters+1):
    random_num = random.randint(0,25)
    let = letters[random_num]
    LorU = random.randint(0,1)
    
    if LorU == 0:
        let.lower()
        letters_p += let
        
    else:
        let.capitalize()
        letters_p += let
        
for x in range(1,n_num + 1):
    random_d = random.randint(0,9)
    no = numbers[random_d]
    num_p += no
for x in range(1,n_symbol+1):
    random_s = random.randint(0,12)
    sym = symbols[random_s]
    sym_p += sym
password = letters_p + num_p + sym_p
ly_password = list(password)
random.shuffle(ly_password)
sh_password = ''.join(ly_password)
print(sh_password)


    


