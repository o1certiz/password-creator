import random
def password_create():
    randomnum = random.randint(8,20)
    othran = random.randint(1,6)
    anrand = random.randint(1,6)
    ganrand = random.randint(1,6)

    keyboard_symbols = [
    "~", "`", "!", "@", "#", "$", "%", "^", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?","£"
]

    capital_letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

    
    
    newpass = ""

    for i in range(othran):
            othothran = random.randint(0,9)
            newpass += (str(othothran))  
    for i in range(anrand):
          newpass += keyboard_symbols[random.randint(0,len(keyboard_symbols)-1)]
    for i in range (ganrand):
          newpass += capital_letters[random.randint(0,len(capital_letters)-1)]

        
    while len(newpass) < randomnum:
        choice = random.choice(["letters","numbers","symbols"])
        
        if choice == "letters":
            
            newpass += random.choice("abcdefghijklmnopqrstuvwxyz")
        elif choice == "numbers":
            
            newpass += str(random.randint(0,9))
        elif choice == "symbols":
            newpass +=keyboard_symbols[random.randint(0,len(keyboard_symbols)-1)]
        
                
              
              
              
          
          
          
    
    print(newpass)
num = int(input("how many asswords do you want to create?(give your answer as an interger): "))
for i in range (num):
    password_create()
