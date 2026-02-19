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