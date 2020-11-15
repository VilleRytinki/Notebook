# -*- coding: cp1252 -*-
import time
import pickle

muistionSisalto = []

def kirjoitamuistioon(merkinnat):
    muistio = open("notebook.dat", "wb")
    pickle.dump(merkinnat, muistio)
    muistio.close()



try:
    muistio = open("notebook.dat", "rb")
    muistio.close()
except:
    muistio = open("notebook.dat", "wb")
    print("No default notebook was found, created one.")
    muistio.close()

while True:
    print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
    toiminta = int(input("Please select one: "))

    if toiminta == 5:
        print("Notebook shutting down, thank you.")
        break
    elif toiminta == 2:
        pvm = time.strftime("%X %x")
        teksti = input("Write a new note: ")
        merkinta = teksti + ":::" + pvm
        muistionSisalto.append(merkinta)

        muistio = open("notebook.dat", "wb")
        pickle.dump(muistionSisalto, muistio)
        muistio.close()

    elif toiminta == 3:
        pvm = time.strftime("%X %x")
        muistio = open("notebook.dat", "rb")
        muistionSisalto = pickle.load(muistio)
        print("The list has", len(muistionSisalto), "notes.")
        muutettava = int(input("Which of them will be changed?: "))
        try:
            print(muistionSisalto[muutettava])
            korvaavaMerkinta = input("Give the new note: ")
            merkinta = korvaavaMerkinta + ":::" + pvm
            muistionSisalto[muutettava] = merkinta

        except Exception:
            "False input."

        kirjoitamuistioon(muistionSisalto)

    elif toiminta == 1:
        try:
            muistio = open("notebook.dat", "rb")
            muistionSisalto = pickle.load(muistio)
            for merkinta in muistionSisalto:
                print(merkinta)
        except Exception:
            continue

    elif toiminta == 4:
        lista = []
        muistio = open("notebook.dat", "rb")
        muistionSisalto = pickle.load(muistio)
        for i in muistionSisalto:
            lista.append(i)

        print("The list has", len(lista), "notes.")
        poistettava = int(input("Which of them will be deleted?: "))
        try:
            poistettava = lista.pop(poistettava)
            print("Deleted note", poistettava)
        except IndexError:
            poistettava = lista.pop()
            print("Deleted note", poistettava)

        kirjoitamuistioon(lista)
