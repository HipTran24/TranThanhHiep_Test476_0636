import tkinter as tk
import rsa

# Tạo key RSA
(public_key, private_key) = rsa.newkeys(512)

# Encrypt
def encrypt_text():
    message = input_text.get().encode()
    encrypted = rsa.encrypt(message, public_key)
    result.set(encrypted.hex())

# Decrypt
def decrypt_text():
    try:
        encrypted = bytes.fromhex(input_text.get())
        decrypted = rsa.decrypt(encrypted, private_key)
        result.set(decrypted.decode())
    except:
        result.set("Error")

# UI
root = tk.Tk()
root.title("RSA Cipher")

tk.Label(root, text="Input").pack()
input_text = tk.Entry(root, width=50)
input_text.pack()

tk.Button(root, text="Encrypt", command=encrypt_text).pack()
tk.Button(root, text="Decrypt", command=decrypt_text).pack()

result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result, width=50).pack()

root.mainloop()
