import requests
import os
import json
os.system('cls||clear')
url_header = "=======================\n Simple URL Shortener\n   Created By Vinn\n=======================\n"
print(url_header)
url = input("Masukan Url Asli : ")
os.system('cls||clear')
print(url_header)
customnya = input("Masukan Custom URL\n(OPTIONAL - Press Enter To Skip) : ")
os.system('cls||clear')
print(url_header)
print("Loading Data...")
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
else:
    print("\n======================\n")
