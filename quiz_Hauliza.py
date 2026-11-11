print("================================")
print("  PROGRAM KELULUSAN MAHASISWA   ")
print("================================")

nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak ditemukan!")
    target = 0

if target != 0:
    print("Nama mahasiswa:", nama)
    print("Target nilai:", target)

    percobaan = 0
    nilai = 0

    # Perulangan maksimal 3 kali
    while percobaan < 3 and nilai < target:

        percobaan += 1

        nilai = int(input(
            f"Masukkan nilai ujian ke-{percobaan}: "
        ))

        if nilai >= target:
            print("Selamat, kamu berhasil mencapai target!")

        else:
            print("Nilai belum mencapai target.")

    # Menentukan hasil akhir
    if nilai >= target:
        print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
    else:
        print(f"{nama} tidak lulus setelah 3 kali percobaan.")