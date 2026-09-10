from back import logo,cipher

print(logo)
game_over = False
while not game_over:



    #take input from user
    user = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Enter your message: ")
    try:
        shift_num = int(input("Enter shift number: "))
    except ValueError:
        print("Only integers are allowed as Shift Number")
        shift_num = int(input("Enter shift number: "))



    # calling function
    result = cipher(user,message,shift_num)
    if result != 0:
        print(f"\nThe {user}d messege is : \n{result}\n")



    #asking user to continue
    stop = False
    while not stop:
        choice = input("Type 'yes' if you wanna go again. Otherwise type 'no': ").lower()
        if choice == "no":
            game_over = True
            print("Good Bye! ")
        elif choice == "yes":
            pass
        else:
            print("Not correct input. Therefore moving forward!.\n")
            continue
            
        stop = True



