def encrypting(): 
    n = int(input("Enter the shift value for encrypting:   "))
    m = input("Now, whisper your secret message to me: ")
    encrypted_message=""
    for char in m:
        if char.isalpha():
                encrypted_message+=chr(ord(char)+n)
        else:
            encrypted_message+=char
    print("Your encrypted message is: ",encrypted_message)

def decrypting():
        n = int(input("Enter the shift value for decrypting:   "))
        decrypted_msg=''
        m = input("Enter the unknown code: ")
        for char in m:
              if char.isalpha():
                    decrypted_msg+=chr(ord(char)-n)
              else:
                    decrypted_msg+=char
        print("Decrypted Message: ", decrypted_msg)

c=""
while c!='y':
      print("1.  ENCRYPT A MESSAGE...\n2. DECRYPT A MESSAGE...\n")
      n1=int(input("Selected Option : "))
      if n1==1:
            encrypting()
      elif n1==2:
            decrypting()
      else:
            break
      
      c=input("Press ""y"" to exit...")


            