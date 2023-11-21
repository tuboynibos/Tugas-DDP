def cek_kelulusan(nilai):
    if nilai <60 :
        return "Gagal"
    elif 61 <= nilai <= 70 :
        return "Baik"
    elif 71 <= nilai <= 80 :
        return "Sangat Baik"
    elif 81 <= nilai <= 100 :
        return "Istimewa"
    else :
        return "Nilai Tidak Falid"

nilaiMahasiswa = 99
statusKelulusan = cek_kelulusan(nilaiMahasiswa)
print(f"Nilai : {nilaiMahasiswa}, Status Kelulusan : {statusKelulusan}")
    

