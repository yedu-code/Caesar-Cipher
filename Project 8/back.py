logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""



#cipher function to encode and decode
def cipher(choice,message,shift_num):
    placeholder = ""
    if choice == "encode":
        n=1
    elif choice=="decode":
        n=-1
    else:
        print("Error in specifying encrypt / decrypt")
        return 0
    for i in message:
        if 65<=ord(i)<=90:
            res = ord(i)+ n*shift_num
            if res >90:
                res-=26
            elif res<65:
                res+=26
            placeholder += chr(res)
        elif 97<=ord(i)<=122:
            res = ord(i)+ n*shift_num
            if res >122:
                res-=26
            elif res<97:
                res+=26
            placeholder += chr(res)
        else:
            placeholder+= i
            
    return placeholder

