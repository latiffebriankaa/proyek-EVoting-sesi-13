import os
def clear_screen():
    # Membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def garis_pemisah():
    print("=" * 30)

def input_non_kosong(prompt):
    # Meminta input sampai tidak kosong
    while True:
        data = input(prompt)
        if data.strip():
            return data
        print("Input tidak boleh kosong.")