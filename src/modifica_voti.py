from nearest_neighbors import carica_dataset_voti


def vota_ricetta(lista_ricette, id):
    n_ricetta = 1

    while n_ricetta != 0:
        print("\nInserisci il numero della ricetta da preparare [0 se non vuoi effettuare una scelta]:", end=" ")

        catch = 2
        while catch == 2:
            try:
                scelta = int(input())
                if 0 <= scelta <= 3:
                    n_ricetta = scelta
                    if n_ricetta != 0:
                        inserisci_voto(lista_ricette, n_ricetta, id)
                        n_ricetta = 0
                else:
                    raise Exception
            except Exception:
                print("Scelta non valida, riprova inserendo un numero valido:", end=" ")
            else:
                catch = 1


def inserisci_voto(lista_ricette, n_ricetta, id):
    print("\nInserisci il voto tra 1 e 10 da assegnare alla ricetta[0 se non vuoi assegnare un voto]:", end=" ")
    catch = 2
    while catch == 2:
        try:
            scelta = int(input())
            if 0 <= scelta <= 10:
                voto = scelta
                if voto != 0:
                    modifica_voto_alimenti(lista_ricette[n_ricetta - 1], voto, id)

            else:
                raise Exception
        except Exception:
            print("Scelta non valida, riprova inserendo un numero valido:", end=" ")
        else:
            catch = 1


def modifica_voto_alimenti(ingredienti, voto, id):
    df_voti = carica_dataset_voti()
    voto_id = f'VotoID{id}'

    for ali in ingredienti:
        # inserisce il nuovo voto prendendo il vecchio dal dataset e facendo la media con quello preso in input dalla funzione
        voto_dataset = df_voti.loc[df_voti['Entity'] == ali, voto_id].iloc[0]
        nuovo_voto = (voto + voto_dataset) / 2
        idx = df_voti.loc[df_voti['Entity'] == ali].index
        df_voti.loc[idx, voto_id] = float(nuovo_voto)

    df_voti.to_csv('./dataset/voti-dataset.csv', index=False)
