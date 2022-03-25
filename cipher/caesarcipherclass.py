def encrypt(text,s):
  result = ""
     # transverse the plain text
  for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters in plain text  
    if (char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
    # Encrypt lowercase characters in plain text
    else:
      result += chr((ord(char) + s-97) % 26 + 97)
  return result

#enter alphabetic text without spaces and a desired shift
text = "CAESARCIPHERDEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))

#write a decryption cipher??
text = "GEIWIVGMTLIVHIQS"

#mild async - given key
s = 4

#spicy async - guess the key