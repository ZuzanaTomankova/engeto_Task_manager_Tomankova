ukoly = []

def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    volba = input("Vyberte možnost(1 - 4) ")
    print("")
    
    if volba == "1":
        pridat_ukol()
        hlavni_menu()
    elif volba == "2":
        zobrazit_ukoly()
        hlavni_menu()
    elif volba == "3":
        odstranit_ukol()
        hlavni_menu()
    elif volba == "4":
        print("Konec programu")
        quit()
    else:
        print ("Neplatná volba")
        hlavni_menu()
        
def pridat_ukol():
    nazev = input("Zadej název úkolu: ")
    popis = input("Zadej popis úkolu: ")
    ukol = {"nazev": nazev, "popis": popis}
    ukoly.append(ukol)
    
def zobrazit_ukoly():
    i = 1
    for ukol in ukoly:
        print(str(i) + ". " + ukol["nazev"] + " - " + ukol["popis"])
        i += 1
        
def odstranit_ukol():
    zobrazit_ukoly()
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        hlavni_menu()
    else:
        cislo_vstup = input("Zadejte číslo úkolu, který chcete odstranit: ")

        if not cislo_vstup.isdigit():
            print("Neplatná volba - zadejte číslo.")
            odstranit_ukol()
        else:
            cislo = int(cislo_vstup)
            pocet_ukolu = len(ukoly)

            if cislo < 1 or cislo > pocet_ukolu:
                print("Neplatná volba - číslo mimo rozsah.")
                odstranit_ukol() 
            else:
                odstranovany_ukol = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstranovany_ukol['nazev']}' byl odstraněn.")