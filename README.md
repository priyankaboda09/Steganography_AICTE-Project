🔐 Secure Data Hiding in Images using Steganography
📌 Project Overview
This project implements a simple, effective steganography technique to hide and retrieve secret messages in image pixels using XOR-based encryption and a user-defined password key. The message is embedded directly into the image using OpenCV and NumPy without changing the image format.

🧪 Technologies Used
🐍 Python – Core programming language

📷 OpenCV – Image handling and manipulation

🧮 NumPy – Efficient array operations for pixel data

💻 OS module – To open files automatically after saving

🔥 Features
🔒 Pixel-level XOR encryption – Hides messages by modifying RGB values based on a secret key

🔑 Password-protected decoding – Only users with the correct password can retrieve the message

📁 Works directly with image pixels – No third-party storage or tools required

🖼️ Supports JPG/PNG formats – Can be used with common image types

🚫 No external storage needed – Message is saved within the image file itself![encrypt.py](https://github.com/user-attachments/assets/f9b85c8b-89f2-4eca-a180-439dd8d7855f)


![decrypt.py](https://github.com/user-attachments/assets/25456f22-7ac5-4970-adc4-496039f49094)
