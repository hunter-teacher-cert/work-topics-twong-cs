#In Class Demo
#encrypt letters such that capital Z shifted 1 is capital A and lowercase z shifted 1 is lowercase a
def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
  # traverse the plain text
    if(char.isupper()):
      #chr(84) = T
      #ord(T) = 84
      result += chr((ord(char) + s - 65) % 26 + 65)
    else:
    # Async Work: Encrypt lowercase characters in plain text
      result += "replace me with code"
  return result

#enter alphabetic text without spaces and a desired shift
text = "AZaz"
s = 1

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encrypted Text: " + encrypt(text,s))
print()

#Homework Bell Pepper Version: Write a function that decrypts a symmetric cipher with a given shift
text = " "
s = 27

def decrypt(text,s):
  result = ""
  return result

#print("Encrypted Text : " + text)
#print("Shift pattern : " + str(s))
#print("Decrypted Text: " + decrypt(text,s))