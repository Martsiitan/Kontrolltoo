
#loob klassi kalkulaator et saaks kasutada kalkulaatori funktsioone
class kalkulaator:
    def liida(self, x, y):return x + y
    def lahuta(self, x, y):return x - y
    def korruta(self, x, y):return x * y
    def jaga(self, x, y):return x / y
    def astenda(self, x, y):return x ** y
    def jääk(self, x, y):return x % y
#def defineerib iga arvutuse nimega, kas liida, lahuta jne.
# return tagastab tehted sõna asemel
    
calc = kalkulaator()
# asendab kalkulaator calc
tehted = {
    "1": calc.liida,
    
    "2": calc.lahuta,
    
    "3": calc.korruta,
    
    "4": calc.jaga,
    
    "5": calc.astenda,
    
    "6": calc.jääk}
#asendab kasutaja sesestatud inputi numbri tulemusega. Et ei peaks kõike välja kirjutama.
    
print(" 1. Liitmine\n 2. Lahutamine\n 3. Korrutamine\n 4. Jagamine\n 5. Astendamine\n 6. Jääk ")
# Prindib ekraanile valikud et kasutaja saaks teada mida kalkulaator teha saab.

vastus = input("Mida tahad kasutada? (1/2/3/4/5/6): ")
#küsib kasutajalt vastust kas 1-6

if vastus in tehted:
    # kui kasutaja sisestatud input on 1-6 number siis valib vajaliku tehte, kas calc.jaga jne.
    num1 = float(input(" Sisestage esimene number: "))
    # Küsib numbrilist vastust kasutajalt mida saaks arvutuses kasutada, kasutaja saab sisestada
    num2 = float(input(" Sisestage teine number: "))
    # Küsib teist numbrilist vastust kasutajalt mida saaks arvutuses kasutada, kasutaja saab sisestada
    tulemus = tehted[vastus](num1, num2)
    # tulemus on võrdne vastusega sisestatud number 1 ja number 2
    print(" Tulemus: ", tulemus)
    #Kuvab kirjuta "Tulemus ja ka funktsiooni tulemus
    
    