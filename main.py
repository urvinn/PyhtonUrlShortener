import requests
import os
import platform
import json

###############################
# Bebas untuk diedit tanpa 
# menghapus nama developer !
###############################
# Free to edit without 
# removing the developer name !
###############################
operating = platform.system() 
os.system('cls||clear')
url_header = """
=============================================================
_  _ ____ _     ____ _  _ ____ ____ ___ ____ _  _ ____ ____ 
|  | |__/ |     [__  |__| |  | |__/  |  |___ |\ | |___ |__/ 
|__| |  \ |___  ___] |  | |__| |  \  |  |___ | \| |___ |  \ 

================== [ Created By Vinn ]=======================\n\n"""
print(url_header)
url = input("Masukan Url Asli : ")
os.system('cls||clear')
print(url_header)
customnya = input("Masukan Custom URL\n(OPTIONAL - Press Enter To Skip) : ")
os.system('cls||clear')
print(url_header)
print("Loading Data...\n")
payload = {
  'url': url,
  'costum': customnya
}
res = requests.post('https://1nz.me/create', data=payload)
data = res.json()
os.system('cls||clear')
print(url_header)
status = (f"{data['status']}") 
print(f"Status : {data['status']}")
print(f"Message : {data['message']}")
if status == "True":
    print("\n======[ RESULTS ]======\n")
    print(f"Origin Links :", url)
    print(f"Short Links  : https://1nz.me/{data['result']['id']}")
    print(f"Delete Links : https://1nz.me/{data['result']['delete']}")
    print("\n======================\n")
    if operating == "Windows":
        tanya = input("Apakah Anda ingin Membuka URL (Y/N) ? ")
        if tanya == "Y":
            os.system(f"start https://1nz.me/{data['result']['id']}")
        else:
            os.system('cls||clear')
        if tanya == "y":
            os.system(f"start https://1nz.me/{data['result']['id']}")
        else:
            os.system('cls||clear')
            print("\nThanks You\n")
            print("\n======================\n")
