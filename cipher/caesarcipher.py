#in class example is just encrypting uppercase letters?

def encrypt(text,s):
  result = ""
     # traverse the plain text
  for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters in plain text  
    if (char.isupper()):
      #convert the letter into unicode
      #make A unicode 0 by subtracting 65
      #add shift
      #allow wraparound by mod 26
      #make A's unicode 65 again by adding 65
      #convert back from unicode to letter
      result += chr((ord(char) - 65 + s) % 26 + 65)
    # Encrypt lowercase characters in plain text  
    else:
      result += chr((ord(char) - 97 + s) % 26 + 97)
  return result

#enter alphabetic text without spaces and a desired shift
text = "AZaz"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))
print()

def decrypt(text,s):
  result = ""
     # transverse the plain text
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) - 65 - s) % 26 + 65)
    else:
      result += chr((ord(char) - 97 - s) % 26 + 97)
  return result

#write a decryption cipher??
text = "BAba"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + decrypt(text,s))