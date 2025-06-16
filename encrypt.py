import cv2
import os

dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)] = i
    dict2[i] = chr(i)

# Reading and analyzing our image
img = cv2.imread(r"C:/Users/Admin/Downloads/encrypting.jpg")
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print(f"IMAGE loaded: {height}x{width}, Channels: {channels}")

# Encryption
key = input("Enter Your Secret Key: ")
text = input("Enter text to hide in the Image: ")

kl = 0
tlen = len(text)
klen = len(key)
x = 0  # No of rows
y = 0  # No of columns
z = 0  # Plane selection

l = len(text)

for i in range(l):
    # Bounds checking
    if x >= height or y >= width or z >= channels:
        print("Error: Image dimensions exceeded while encoding.")
        exit()
    
    img[x, y, z] = dict1[text[i]] ^ dict1[key[kl]]
    y = y + 1
    x = x + 1
    kl = (kl + 1) % klen

# Save the modified image
cv2.imwrite(r"C:/Users/Admin/Downloads/steganography_project/encrypting.jpg", img)
os.startfile(r"C:/Users/Admin/Downloads/steganography_project/encrypting.jpg")
print("Data Hiding in the IMAGE completed successfully.")
