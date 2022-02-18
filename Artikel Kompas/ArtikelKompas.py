import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    try:
        content=requests.get('https://kompas.com')
    except Exception:
        return None

    if content.status_code==200:
        soup=BeautifulSoup(content.text,'html.parser')
        result=soup.find('div',{'class':'most ga--most mt1 clearfix'})
        result=result.findChildren('h4',{'class':'most__title'})
        i=0
        berita1=None
        berita2=None
        berita3= None
        berita4= None
        berita5 = None
        berita6 = None
        berita7 = None
        berita8 = None
        berita9 = None
        berita10 = None

        for res in result:
            if i==0:
                berita1=res.text
            elif i==1:
                berita2=res.text
            elif i==2:
                berita3=res.text
            elif i==3:
                berita4 = res.text
            elif i==4:
                berita5=res.text
            elif i==5:
                berita6=res.text
            elif i==6:
                berita7=res.text
            elif i==7:
                berita8=res.text
            elif i==8:
                berita9=res.text
            elif i==9:
                berita10=res.text
            i=i+1

        hasil=dict()
        hasil['berita1']=berita1
        hasil['berita2']=berita2
        hasil['berita3']=berita3
        hasil['berita4']=berita4
        hasil['berita5']=berita5
        hasil['berita6']=berita6
        hasil['berita7']=berita7
        hasil['berita8'] = berita8
        hasil['berita9'] = berita9
        hasil['berita10'] = berita10
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data artikel kompas terkini")
        return
    print('Sepuluh Artikel Terpopuler Kompas')
    print(f"1.  {result['berita1']}")
    print(f"2.  {result['berita2']}")
    print(f"3.  {result['berita3']}")
    print(f"4.  {result['berita4']}")
    print(f"5.  {result['berita5']}")
    print(f"6.  {result['berita6']}")
    print(f"7.  {result['berita7']}")
    print(f"8.  {result['berita8']}")
    print(f"9.  {result['berita9']}")
    print(f"10.  {result['berita10']}")
