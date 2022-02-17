from Gempa import ekstraksi_data,tampilkan_data

if __name__=='__main__':
    print("Aplikasi Utama")
    result=ekstraksi_data()
    tampilkan_data(result)

"""atau"""
import Gempa

if __name__=='__main__':
    print("\nAplikasi Utama")
    result=Gempa.ekstraksi_data()
    Gempa.tampilkan_data(result)