import json
import requests

nazev_subjektu = input("Zadejte prosím název hledaného subjektu: ")
data = json.dumps({"obchodniJmeno": nazev_subjektu})

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

response_data = res.json()

pocet_subjektu = response_data.get("pocetCelkem", 0)
print(pocet_subjektu)

subjekty = response_data.get("ekonomickeSubjekty", [])

if subjekty:
    for subjekt in subjekty:
        print(f"{subjekt.get('obchodniJmeno')}, {subjekt.get('ico')}")
else:    
        print(f"nenalezeno")




