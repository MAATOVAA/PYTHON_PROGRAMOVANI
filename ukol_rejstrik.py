
import json
import requests

ico = input("Zadejte prosím IČO hledaného subjektu: ")
subjekt = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = subjekt.json()
obchodni_jmeno = data.get("obchodniJmeno", "Obchodní jméno není k dispozici")
adresa = data.get("sidlo", {}).get("textovaAdresa", "Adresa není k dispozici")

print(obchodni_jmeno)
print(adresa)













