import requests
from bs4 import BeautifulSoup

link = f"https://www.worldometers.info/coronavirus/"
istek = requests.get(link)
soup = BeautifulSoup(istek.text, "html5lib")

sozluk = {"koronaVerileri": []}

dunya = soup.select("#maincounter-wrap > div")
dunyaVaka = dunya[0].text.strip()
dunyaOlu = dunya[1].text.strip()
dunyaKurtulan = dunya[2].text.strip()

turkiye = soup.select("#main_table_countries_today > tbody:nth-child(2) > tr:nth-child(16)")
turkiye = turkiye[0].text.split()
trVaka = turkiye[1]
trOlu = turkiye[3]
trKurtulan = turkiye[5]

sozluk["koronaVerileri"].append({
    "vaka Sayısı": {"TR": trVaka, "Dünya Geneli": dunyaVaka},
    "ÖLÜ Sayısı": {"TR": trOlu, "Dünya Geneli": dunyaOlu},
    "İyileşen Sayisi": {"TR": trKurtulan, "Dünya Geneli": dunyaKurtulan}
})

print(sozluk)
