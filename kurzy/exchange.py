import httpx

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

odpoved = httpx.get(URL)
print("Stav odpovědi:", odpoved.status_code)

if odpoved.status_code != 200:
    print("Data se nepodařilo stáhnout.")
    exit()

radky = odpoved.text.split("\n")
den = radky[0].split(" ")[0]
print("Kurzy pro den:", den)

eur_radek = ""
for r in radky:
    if "|EUR|" in r:
        eur_radek = r
        break

if eur_radek == "":
    print("Kurz pro EUR nebyl nalezen.")
    exit()

casti = eur_radek.split("|")
pocet = int(casti[2])
hodnota = float(casti[4].replace(",", "."))

kurz_1_eur = hodnota / pocet
print("1 EUR =", round(kurz_1_eur, 4), "CZK")

print()
print("Zvol převod:")
print("1 - EUR na CZK")
print("2 - CZK na EUR")

volba = input("Tvoje volba: ").strip()
if volba != "1" and volba != "2":
    print("Špatná volba.")
    exit()

while True:
    vstup = input("Zadej částku: ").replace(",", ".")
    try:
        cislo = float(vstup)
        if cislo <= 0:
            print("Částka musí být větší než nula.")
            continue
        break
    except ValueError:
        print("Tohle není číslo.")

if volba == "1":
    vysledek = cislo * kurz_1_eur
    print(cislo, "EUR =", round(vysledek, 2), "CZK")
else:
    vysledek = cislo / kurz_1_eur
    print(cislo, "CZK =", round(vysledek, 2), "EUR")
