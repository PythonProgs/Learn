def ekstraksi_data():
    hasil=dict()
    hasil['tanggal']='24 Agustus 2021'
    hasil['waktu']='14:32'
    return hasil

def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")

