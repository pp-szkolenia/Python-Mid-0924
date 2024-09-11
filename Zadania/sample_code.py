my_money=10
unit_price=5


def isAdult(wiek):
    return wiek < 18

def price_calculation(number,unit_price):
    return number *unit_price
print(f"Dzień dobry, chciałbym kupić piwo.\n")

age = input("Proszę podać swój wiek: ")
if isAdult(age):
    print("Nieletnim nie sprzedajemy alkoholu, do widzenia!")
else:
        while True:
            n_of_beers = int(input("\nIle sztuk?: "))
            totalprice = price_calculation(n_of_beers,unit_price)

            print(f"\nPiwo kosztuje {unit_price}zł. To będzie razem {totalprice}zł\n")
            print(f"Mam {my_money}zł\n")

            if my_money>=total_price:
                print(f"Proszę, oto piwa, sztuk - {n_of_beers} oraz reszta: {my_money - totalprice}zł")
                break
            elif my_money < total_price:
                print(f"To za mało, brakuje {totalprice- my_money}zł")
            else:
                break
                print(f"Proszę, oto piwa, sztuk - {n_of_beers}")
                
