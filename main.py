import sqlite3

# 1. Inisialisasi Database SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Buat tabel users jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")
conn.commit()

# 2. Fungsi Registrasi (Buat Akun Baru)
def register():
    print("\n--- MENU REGISTRASI ---")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registrasi berhasil! Silakan login.")
    except sqlite3.IntegrityError:
        print("Username sudah terdaftar, gunakan username lain.")

# 3. Fungsi Login
def login():
    print("\n--- MENU LOGIN ---")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        print(f"\nLogin berhasil! Selamat datang, {username}.")
        program_utama()
    else:
        print("\nUsername atau password salah! Akses ditolak.")

# 4. Program Utama (Contoh Ganjil Genap)
def program_utama():
    print("\n--- PROGRAM UTAMA ---")
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"Angka {angka} adalah GENAP.")
    else:
        print(f"Angka {angka} adalah GANJIL.")

# 5. Menu Awal
def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Login")
        print("2. Buat Akun Baru (Registrasi)")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
