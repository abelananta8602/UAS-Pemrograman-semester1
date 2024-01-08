def start():
    global portofolio_investasi
    portofolio_investasi = []
    while True:
        print("Mohon Untuk Mengisi Dengan Benar")
        print("Silahkan Untuk Memilih Layanan:")
        print("1. Kredit")
        print("2. investasi / Tabungan")
        print("3. Keluhan")
        print("4. Keluar")
        service = input("Masukkan pilihan (1/2/3/4): ")
        
        if service in ['1', '2', '3', '4']:
            if service == "1":
                pengajuan_kredit()
            elif service == "2":
                investasi()
            elif service == "3":
                penerimaan_keluhan()   
            elif service == "4":
                print("Terima kasih telah menggunakan layanan kami.")
            break          
        else:
            print("Pilihan Anda tidak valid. Silakan coba lagi.")
        
            
def investasi():
    keuntungan = input("Apakah Anda ingin berinvestasi untuk keuntungan? (ya/tidak): ").lower()
    if keuntungan == "ya":
        pemilihan_produk_investasi()
    else:
        pemilihan_produk_tabungan()
        
def pemilihan_produk_investasi():
    global portofolio_investasi
    print("Pemilihan Produk Investasi:")
    investasi_options = ["1.Reksadana", "2.Obligasi", "3.Derivatif"]
    for option in investasi_options:
        print(f"- {option}")
    pilihan_investasi = input("Pilih jenis investasi yang diinginkan: ").title()
    if pilihan_investasi == "1" and "reksadana":
        pilihan_reksadana()
    elif pilihan_investasi == "2" and "Obligasi":
        pilihan_obligasi()
    elif pilihan_investasi == "3" and "Derivatif":
        pilihan_derivatif()
    else:
        print("Pilihan investasi tidak valid. Silakan coba lagi.")
        pemilihan_produk_investasi()
        
def pemilihan_produk_tabungan():
    print("Pilihan Tabungan atau Deposito:")
    tabungan_options = ["Tabungan", "Deposito"]
    for option in tabungan_options:
        print(f"- {option}")
    pilihan_tabungan = input("Pilih jenis yang anda diinginkan: ").title()
    if setujui_resiko():
        if setujui_syarat_dan_ketentuan():
                            jumlah_deposit = input_deposit_tabungan_deposito()
                            tambah_ke_portofolio("Reksadana Campuran", jumlah_deposit)
                            pemantauan_portofolio_investasi()          
    
def pilihan_reksadana():
        print("Pilih jenis Reksadana:")
        print("1. Reksadana Pasar Uang")
        print("2. Reksadana Saham")
        print("3. Reksadana Campuran")
        pilihan_reksadana = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan_reksadana in ['1', '2', '3']:
            if pilihan_reksadana == '1':
               print("Anda memilih Reksadana Pasar Uang.")
            if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Reksadana Pasar Uang", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_reksadana == '2':
                print("Anda memilih Reksadana Saham.")
                if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Reksadana Saham", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_reksadana == '3':
                print("Anda memilih Reksadana Campuran.")
                if setujui_resiko():
                         if setujui_syarat_dan_ketentuan():
                            jumlah_deposit = input_jumlah_deposit()
                            tambah_ke_portofolio("Reksadana Campuran", jumlah_deposit)
                            pemantauan_portofolio_investasi()          
    
            
        else:
            print("Pilihan Anda tidak valid. Silakan coba lagi.")
        investasi_lagi()

def pilihan_obligasi():
        print("Pilih jenis obligasi:")
        print("1. Obligasi pemerintah")
        print("2. Obligasi Korporasi")
        print("3. Obligasi Komunal")
        pilihan_obligasi = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan_obligasi in ['1', '2', '3']:
            if pilihan_obligasi == '1':
               print("Anda memilih Obligasi pemerintah.")
            if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Obligasi pemerintah", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_obligasi == '2':
                print("Anda memilih Obligasi Korporasi.")
                if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Obligasi Korporasi", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_obligasi == '3':
                print("Anda memilih Obligasi Komunal.")
                if setujui_resiko():
                         if setujui_syarat_dan_ketentuan():
                            jumlah_deposit = input_jumlah_deposit()
                            tambah_ke_portofolio("Obligasi Komunal", jumlah_deposit)
                            pemantauan_portofolio_investasi()          
    
            
        else:
            print("Pilihan Anda tidak valid. Silakan coba lagi.")
        investasi_lagi()

        
def pilihan_derivatif():
        print("Pilih jenis Reksadana:")
        print("1. Option")
        print("2. Future")
        print("3. Swap")
        pilihan_derivatif = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan_derivatif in ['1', '2', '3']:
            if pilihan_derivatif == '1':
               print("Anda memilih Option.")
            if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Option", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_derivatif == '2':
                print("Anda memilih Future.")
                if setujui_resiko():
                    if setujui_syarat_dan_ketentuan():
                        jumlah_deposit = input_jumlah_deposit()
                        tambah_ke_portofolio("Future", jumlah_deposit)
                        pemantauan_portofolio_investasi()
            elif pilihan_derivatif == '3':
                print("Anda memilih Swap.")
                if setujui_resiko():
                         if setujui_syarat_dan_ketentuan():
                            jumlah_deposit = input_jumlah_deposit()
                            tambah_ke_portofolio("Swap", jumlah_deposit)
                            pemantauan_portofolio_investasi()          
    
            
        else:
            print("Pilihan Anda tidak valid. Silakan coba lagi.")
        investasi_lagi()
        

def input_deposit_tabungan_deposito():
    jumlah = float(input("Masukkan jumlah yang anda inginkan: "))
    return jumlah

def setujui_resiko():
    persetujuan = input("Apakah Anda memahami dan menyetujui risiko investasi? (ya/tidak): ").lower()
    return persetujuan == "ya"

def setujui_syarat_dan_ketentuan():
    persetujuan = input("Apakah Anda menyetujui syarat dan ketentuan investasi? (ya/tidak): ").lower()
    return persetujuan == "ya"

def input_jumlah_deposit():
    jumlah = float(input("Masukkan jumlah deposit untuk investasi: "))
    return jumlah

def tambah_ke_portofolio(jenis_investasi, jumlah):
    global portofolio_investasi
    portofolio_investasi.append({'jenis': jenis_investasi, 'nilai': jumlah})
    print(f"Jumlah Rp{jumlah} telah diinvestasikan pada {jenis_investasi}.")

def pemantauan_portofolio_investasi():
    global portofolio_investasi
    print("Memantau portofolio investasi Anda:")
    if portofolio_investasi:
        for investasi in portofolio_investasi:
            print(f"Investasi: {investasi['jenis']}, Nilai: {investasi['nilai']}")
    else:
        print("Belum ada investasi yang dicatat.")
        
def investasi_lagi():
    ulangi = input("Apakah Anda ingin berinvestasi lagi? (ya/tidak): ").lower()
    if ulangi == "ya":
        pemilihan_produk_investasi()
    else:
        print("Kembali ke menu utama.")
        
def pengajuan_kredit():
    print("Silakan masukkan data untuk pengajuan kredit")
    nomor_ktp = input("Nomor KTP: ")
    nomor_npwp = input("Nomor NPWP: ")
    jumlah_penghasilan = input("Jumlah Penghasilan per bulan: ")
    jaminan = input("Jaminan (Rumah/Mobil/Motor): ").lower()

    if jaminan not in ['rumah', 'mobil', 'motor']:
        print("Jaminan harus salah satu dari Rumah, Mobil, atau Motor, Jika tidak anda tidak bisa mengajukan kredit!")
        return  
    print("Proses pencairan dana kredit sedang diproses.....")
    
    if not tanya_lanjut():
        start()  


def tanya_lanjut():
    lanjut = input("Apakah Anda ingin melanjutkan ke layanan lain? (ya/tidak): ").lower()
    return lanjut == "ya"

def penerimaan_keluhan():
    
    keluhan = input("Apakah ada keluhan atau pertanyaan? (ya/tidak): ").lower()
    if keluhan == "ya":
        tampilkan_pertanyaan()
    print("Kembali ke menu utama.")

def tampilkan_pertanyaan():
    
    pertanyaan = [
        "1. Informasi tentang keamanan dan privasi nasabah.",
        "2. Cara menghubungi layanan pelanggan untuk bantuan.",
        "3. Kebijakan tentang biaya dan suku bunga.",
        "4. Prosedur untuk mengatasi masalah pada akun atau transaksi."
    ]
    for p in pertanyaan:
        print(p)
    pilihan = input("Pilih nomor pertanyaan: ")

    jawaban = {
        "1": "prioritas tinggi pada keamanan dan privasi nasabah. Ini termasuk penggunaan teknologi enkripsi, autentikasi dua faktor untuk transaksi, serta kebijakan privasi yang ketat untuk melindungi data pribadi nasabah. Bank juga sering memberi nasihat tentang bagaimana nasabah dapat melindungi diri dari penipuan online dan pencurian identitas.",
        "2": "nasabah dapat menghubungi layanan pelanggan melalui berbagai cara seperti telepon, email, atau live chat.",
        "3": " Informasi tentang biaya layanan, seperti biaya administrasi bulanan, biaya transaksi, dan suku bunga untuk pinjaman atau tabungan, biasanya tersedia di situs web bank. Suku bunga bisa berubah dan tergantung pada kondisi pasar serta kebijakan bank.",
        "4": "Jika terjadi masalah pada akun atau transaksi, nasabah harus segera menghubungi bank. Proses penanganan termasuk verifikasi identitas nasabah dan peninjauan transaksi yang bermasalah. "
    }

    print(jawaban.get(pilihan, "Pilihan tidak valid. Silakan coba lagi."))
    
    ulangi_pertanyaan()

def ulangi_atau_tidak():
    ulangi = input("Apakah Anda ingin menggunakan layanan lainnya? (ya/tidak): ").lower()
    if ulangi != "ya":
        print("Terima kasih telah menggunakan layanan kami.")
        exit()
        
def ulangi_pertanyaan():
    ulangi = input("Apakah Anda ingin pertanyaan lagi? (ya/tidak): ").lower()
    if ulangi == "ya":
        tampilkan_pertanyaan()
    else:
        print("Kembali ke menu utama.")
   

start()
