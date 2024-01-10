import CSP
import crea_ricetta
import nearest_neighbors
import modifica_voti


def menu_consiglia_alimenti():
    scelta: int = 0

    while scelta != 3:
        print("\nSeleziona l'utente a cui consigliare una ricetta\n")
        print("(1) Michele")
        print("(2) Angelo")
        print("(3) Torna al menù principale\n")

        catch = 2
        while catch == 2:
            try:
                scelta = int(input("Effettuare una scelta: "))
            except ValueError:
                print("Scelta non valida, riprova.")
            else:
                catch = 1

        if scelta == 1:
            id = 1
            lista_ricette = alimenti_consigliati(id)
            modifica_voti.vota_ricetta(lista_ricette, id)

        elif scelta == 2:
            id = 2
            lista_ricette = alimenti_consigliati(id)
            modifica_voti.vota_ricetta(lista_ricette, id)


def alimenti_consigliati(id):
    lista_consigliati = nearest_neighbors.raccomanda_alimenti(id)
    print("\nIn base alle tue preferenze, ti consiglio:", str(lista_consigliati).replace("[", "").replace(
        "]", "").replace("'", "").replace("_", " ").replace('"', "").replace("danatra", "d'anatra"))
    return crea_ricetta.crea_ricette(lista_consigliati)


def verifica_alimenti_csp(lista_consigliati):
    for alimento in lista_consigliati:
        CSP.csp_alimento_disponibile(alimento)

    print("Lista alimenti presenti: ", CSP.lista_ali_presenti)
    print("Lista alimenti non presenti o scaduti: ", CSP.lista_ali_non_presenti)
