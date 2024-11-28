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

data = json.dumps({"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"})
res_ciselnik = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data) 
ciselnik_data = res_ciselnik.json()
ciselnik = ciselnik_data.get("ciselniky", [])[0].get("polozkyCiselniku", [])

def find_legal_form(kod, polozky_ciselniku):
    for polozka in polozky_ciselniku:
        if polozka.get("kod")==str(kod):
            return polozka.get("nazev")[0]["nazev"]
        else:
            continue

if subjekty:
    for subjekt in subjekty:
        pravni_forma_kod = subjekt.get("pravniForma")
        pravni_forma = find_legal_form(pravni_forma_kod, ciselnik) if pravni_forma_kod else "Neznámá právní forma"
        print(f"{subjekt.get('obchodniJmeno')}, {subjekt.get('ico')}, {pravni_forma}")                                                                                   
else:    
        print(f"nenalezeno")















