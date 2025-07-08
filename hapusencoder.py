import pickle
import os

def hapus_semua_encoding():
    try:
        # Mengecek apakah file EncodeFile.p ada
        if os.path.exists('EncodeFile.p'):
            # Menulis ulang file EncodeFile.p dengan data kosong
            with open('EncodeFile.p', 'wb') as file:
                pickle.dump([[], []], file)
    
            print("Semua encoding berhasil dihapus.")
        else:
            print("File EncodeFile.p tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    hapus_semua_encoding()
