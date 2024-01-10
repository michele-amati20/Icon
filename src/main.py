import lista_alimenti
import consiglia_alimenti


if __name__ == '__main__':
    scelta: int = 0
    lista_alimenti.ali_list = lista_alimenti.carica_lista()
    while scelta != 3:
        print("Seleziona l'operazione da effettuare:\n")
        print("(1) Gestisci alimenti")
        print("(2) Consigliami una ricetta")
        print("(3) Esci")
        catch = 2
        while catch == 2:
            try:
                scelta = int(input("\nEffettuare una scelta: "))
            except ValueError:
                print("Scelta non valida, riprova.")
            else:
                catch = 1

        if scelta == 1:
            lista_alimenti.menu_lista_alimenti()
        elif scelta == 2:
            consiglia_alimenti.menu_consiglia_alimenti()
