import numpy as np
from datetime import date, datetime
from tabulate import tabulate
import onto

ali_list = {}


def menu_lista_alimenti():
    scelta: int = 0

    while scelta != 5:
        print("Seleziona l'operazione da effettuare:")
        print("(1) Aggiungi un alimento")
        print("(2) Rimuovi un alimento")
        print("(3) Lista alimenti presenti")
        print("(4) Ricerca di un alimento")
        print("(5) Torna al menù principale")

        catch = 2
        while catch == 2:
            try:
                scelta = int(input("Effettuare una scelta: "))
            except ValueError:
                print("Scelta non valida, riprova.")
            else:
                catch = 1

        if scelta == 1:
            inserisci_alimento()
        elif scelta == 2:
            elimina_alimento()
        elif scelta == 3:
            stampa_alimenti()
        elif scelta == 4:
            ricerca_alimento()


def carica_lista():
    return np.load("./data/list.npy", allow_pickle=True).item()


def salva_lista():
    np.save("./data/list.npy", ali_list)


def parse_date(scadenza):
    try:
        # strptime per convertire la stringa in un oggetto datetime
        datetime_object = datetime.strptime(scadenza, '%d/%m/%Y')
        # Estrai la parte della data
        data = datetime_object.date()
        return data
    except ValueError:
        print("Formato data non valido. Assicurati che la stringa sia nel formato gg/mm/aa.")
        raise Exception


def inserisci_alimento():
    try:
        nome = input("Inserisci nome alimento: ")
        if nome in ali_list:
            raise ValueError
        else:
            scadenza_str = input("Inserisci data di scadenza (nel formato gg/mm/aaaa): ")
            scadenza = parse_date(scadenza_str)
            ali_list[nome] = scadenza
            salva_lista()
    except ValueError:
        print("Alimento già presente")
    except Exception:
        print("Errore nell'inserimento, riprova")


def elimina_alimento():
    try:
        nome = input("Inserisci nome dell'alimento da eliminare: ")
        if nome in ali_list:
            del ali_list[nome]
        else:
            raise ValueError
    except ValueError:
        print("Alimento non presente")
    salva_lista()


def stampa_alimenti():
    print("Lista alimenti presenti in casa:")
    table_data = [("Nome Alimento", "Data di scadenza", "Calorie")]

    for alimento, data_scadenza in ali_list.items():
        try:
            cal_alimento = onto.query_cal_alimento(alimento)
            if cal_alimento is not None:
                table_data.append((alimento, data_scadenza.strftime("%d/%m/%Y"), cal_alimento))
        except Exception:
            table_data.append((alimento, data_scadenza.strftime("%d/%m/%Y")))
    table = tabulate(table_data, headers="firstrow", tablefmt="plane")
    print(table)
    input("Premere Invio per continuare")


def ricerca_alimento():
    alimento = input("Inserire nome dell'alimento per verificare se è presente: ")

    if alimento in ali_list:
        print("Alimento presente")
        try:
            cal_alimento = onto.query_cal_alimento(alimento)
            if cal_alimento is not None:
                table_data = [("Nome Alimento", "Data di scadenza", "Calorie"),
                              (alimento, ali_list[alimento].strftime("%d/%m/%Y"), cal_alimento)]
        except Exception:
            table_data = [("Nome Alimento", "Data di scadenza"), (alimento, ali_list[alimento].strftime("%d/%m/%Y"))]

        table = tabulate(table_data, headers="firstrow", tablefmt="plane")
        print(table)
    else:
        print("Alimento non presente")


if __name__ == '__main__':
    elimina_alimento()
    # inserisci_alimento()
    print(ali_list)
