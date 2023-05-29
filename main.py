class Samochod:
    def __init__(self, marka, model, rok_produkcji, kolor, przebieg, cena, dodatkowe_parametry=None, inne_dane=None):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor
        self.przebieg = przebieg
        self.cena = cena
        self.dodatkowe_parametry = dodatkowe_parametry
        self.inne_dane = inne_dane

    def __str__(self):
        return f"Samochód: {self.marka} {self.model} ({self.rok_produkcji}), kolor: {self.kolor}, cena: {self.cena} PLN"

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor

    def dodaj_parametr(self, nazwa, wartosc):
        if self.dodatkowe_parametry is None:
            self.dodatkowe_parametry = {}
        self.dodatkowe_parametry[nazwa] = wartosc

# Przykład użycia klasy Samochod:
auto = Samochod("Fiat", "Punto", 2010, "czerwony", 100000, 15000)
auto.zmien_kolor("zielony")
auto.dodaj_parametr("Moc", "75 KM")
print(auto)
