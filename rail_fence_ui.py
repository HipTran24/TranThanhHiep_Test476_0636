import tkinter as tk


def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down

        rail[row][col] = char
        col += 1

        row += 1 if dir_down else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
        col += 1

        row += 1 if dir_down else -1

    return "".join(result)


def encrypt_text():
    text = input_text.get()
    key = int(key_entry.get())
    result.set(rail_fence_encrypt(text, key))

def decrypt_text():
    text = input_text.get()
    key = int(key_entry.get())
    result.set(rail_fence_decrypt(text, key))


root = tk.Tk()
root.title("Rail Fence Cipher")

tk.Label(root, text="Input Text").pack()
input_text = tk.Entry(root, width=50)
input_text.pack()

tk.Label(root, text="Key").pack()
key_entry = tk.Entry(root)
key_entry.pack()

tk.Button(root, text="Encrypt", command=encrypt_text).pack()
tk.Button(root, text="Decrypt", command=decrypt_text).pack()

result = tk.StringVar()
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result, width=50).pack()

root.mainloop()
