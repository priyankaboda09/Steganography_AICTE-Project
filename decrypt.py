import cv2

# Dictionaries for character-to-integer and integer-to-character mapping
dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)] = i
    dict2[i] = chr(i)

# Load the image with hidden text
img = cv2.imread(r"C:/Users/Admin/Downloads/steganography_project/encrypting.jpg")
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

height, width, channels = img.shape
print(f"IMAGE loaded: {height}x{width}, Channels: {channels}")

# User inputs
key = input("Enter Your Secret Key:868686 ")
msg_len = int(input("Enter the length of the hidden message:17 "))

kl = 0
klen = len(key)
x = 0
y = 0
z = 0

decrypted_text = ""

for i in range(msg_len):
    # Bounds checking
    if x >= height or y >= width or z >= channels:
        print("Error: Image dimensions exceeded while decoding.")
        exit()
    
    # Retrieve the encoded value and decrypt
    enc_val = img[x, y, z]
    dec_char = dict2[enc_val ^ dict1[key[kl]]]
    decrypted_text += dec_char

    y += 1
    x += 1
    kl = (kl + 1) % klen

print("Decrypted text:", decrypted_text)
