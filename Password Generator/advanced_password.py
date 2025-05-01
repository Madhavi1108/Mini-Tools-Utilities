#Creating a function password_generator to ensure that the user gets a new password
def password_generator() :
    
    #Creating a list containing characters a to z and A to Z
    list_a = []
    
    #Since ascii codes of A to Z lie between 65 and 90 while the ascii codes for a to z between 97 and 122
    for i in range(65 , 123):
        if i > 90 and i < 97 :
            continue
        else :
            character = chr(i)
            list_a = list_a + [character]
            
    #Creating a list containing numbers from 0 to 10
    list_b = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
    
    #Creating a list containing special characters
    list_c = [ '!', '@' , '#' , '%' , '^' , '&' , '*' , '(' , ')' , '+' ]
    
    letters = int(input("How many letters you want in your password:"))
    numbers = int(input("How many numbers you want in your password:"))
    symbols = int(input("How many letters you want in your password:"))
    
    #Checking if the password has atleast 8 characters
    if letters + numbers + symbols >= 8 :
        
        #Appending all the random letters in our password
        password_list = []
        for i in range(0,letters):
            a = random.choice(list_a)
            password_list = password_list + [a]
            
        #Appending all the random numbers in our password
        for i in range(0,numbers):
            b = random.choice(list_b)
            password_list = password_list + [b]
            
        #Appending all the random symbols in our password
        for i in range(0,symbols):
             c = random.choice(list_c)
             password_list = password_list + [c]
             
        #Shuffling the variables so that we get a strong password
        random.shuffle(password_list)
        
        #Converting the strong_password variable from list to a string
        password = ''
        for letter in password_list :
            password = password + letter
        print(f"Your password is {password}")
        
    else :
        print("Kindly select atleast an 8 digit password")
        password_generator()
        
print("Welcome to 'MY PASSWORD GENERATOR")
password_generator()

while input("Are you satisfied with your password 'yes' or 'no' :").lower() == 'no' :
    password_generator()
