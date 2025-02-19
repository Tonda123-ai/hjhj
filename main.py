
pocetvstupenek = int(input("Kolik vstupenek chcete koupit? "))
celkovacena = 0
for i in range(pocetvstupenek):
    vek = int(input(f"Zadejte věk návštěvníka {i+1}: "))
    if vek < 6:
        cena = 0
    elif vek < 18:
        cena = 10
    elif vek < 65:
        cena = 20
    else:
        cena = 15
    celkovacena += cena
print(f"Celková cena za vstupenky je: {celkovacena}€")