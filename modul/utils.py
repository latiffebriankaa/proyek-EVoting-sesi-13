import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def garis_pemisah():
    print("=" * 40)

def input_non_kosong(prompt):
    while True:
        data = input(prompt)
        if data.strip():
            return data
        print("Input tidak boleh kosong.")