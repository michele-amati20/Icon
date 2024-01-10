import random
import onto
import CSP
from tabulate import tabulate


def crea_ricette(consigliati):
    ricette = []

    for i in range(0, len(consigliati)):
        ingredienti = crea_abbinamenti(consigliati[i])
        print(f"\nRicetta {i + 1}:")
        ricette.append(ingredienti)
        stampa_ricetta(ingredienti)
    return ricette


def crea_abbinamenti(ing):
    lista_abbinamenti = [ing]

    abbinamenti = onto.query_abbinatoCon_alimento(ing)

    n = random.randint(3, 4)
    while True:

        ing = str(abbinamenti[random.randint(0, len(abbinamenti) - 1)])
        lista_abbinamenti.append(ing)
        n -= 1
        intersezione = list(set(abbinamenti).intersection(onto.query_abbinatoCon_alimento(ing)))
        if len(intersezione) == 0 or n == 0:
            return lista_abbinamenti

        abbinamenti = intersezione


def stampa_ricetta(ingredienti):

    table = []
    headers = ["Alimento e Cottura", "Quantità", "Disponibilità"]

    for elem in ingredienti:
        cal = onto.query_cal_alimento(elem)
        tipo = str(onto.query_tipo_alimento(elem)).replace("food.", '')
        cottura = scegli_cottura(elem)
        peso = calcola_peso(elem, cal, tipo)
        disponibilita = CSP.csp_alimento_disponibile(elem)

        nome_completo = f"{elem.replace('_', ' ')} {cottura}" if cottura != "purea" else f"purea di {elem}"

        if elem == "piadine" or elem == "uova" or elem == "panino":
            table.append([nome_completo, f"{int(peso)}", f"{disponibilita}"])
        else:
            table.append([nome_completo, f"{int(peso)}g", f"{disponibilita}"])

    print(tabulate(table, headers=headers, tablefmt="plane"))


def calcola_peso(nome, cal, tipo):
    MIN_CAL_CARNE = 250
    MAX_CAL_CARNE = 280

    MIN_CAL_VERDURA = 10
    MAX_CAL_VERDURA = 15

    MIN_CAL_CARBO = 300
    MAX_CAL_CARBO = 450

    MIN_CAL_LEGUMI = 150
    MAX_CAL_LEGUMI = 180

    MIN_CAL_DERIVATI = 100
    MAX_CAL_DERIVATI = 130

    MIN_CAL_PESCE = 150
    MAX_CAL_PESCE = 200

    MIN_CAL_MOZZ_BURRATA = 80
    MAX_CAL_MOZZ_BURRATA = 100

    MIN_UOVA = 1
    MAX_UOVA = 2

    if nome == "mozzarella" or nome == "burrata":
        return 100 * round(random.randrange(MIN_CAL_MOZZ_BURRATA, MAX_CAL_MOZZ_BURRATA, 10) / cal, 1)

    elif nome == "uova":
        return random.randrange(MIN_UOVA, MAX_UOVA + 1)

    elif nome == "piadine":
        return 1

    elif nome == "panino":
        return 1

    elif tipo == "carne":
        return 100 * round(random.randrange(MIN_CAL_CARNE, MAX_CAL_CARNE, 10) / cal, 1)

    elif tipo == "pesce":
        return 100 * round(random.randrange(MIN_CAL_PESCE, MAX_CAL_PESCE, 10) / cal, 1)

    elif tipo == "verdura":
        return 100 * round(random.randrange(MIN_CAL_VERDURA, MAX_CAL_VERDURA, 10) / cal, 1)

    elif tipo == "legumi":
        return 100 * round(random.randrange(MIN_CAL_LEGUMI, MAX_CAL_LEGUMI, 10) / cal, 1)

    elif tipo == "carboidrati" and nome != "piadine":
        return 100 * round(random.randrange(MIN_CAL_CARBO, MAX_CAL_CARBO, 10) / cal, 1)

    elif tipo == "derivati_animali" and nome != "mozzarella" and nome != "burrata" and nome != "uova":
        return 100 * round(random.randrange(MIN_CAL_DERIVATI, MAX_CAL_DERIVATI, 10) / cal, 1)


def scegli_cottura(ing):
    tipi_cottura = onto.query_cottoIn_alimento(ing)

    if len(tipi_cottura) == 0:
        return ""

    scelta = tipi_cottura[(random.randint(0, len(tipi_cottura)-1))]

    if scelta == "padella":
        return "in padella"

    elif scelta == "forno":
        return "al forno"

    elif scelta == "piastra":
        return "alla piastra"

    elif scelta == "brace":
        return "alla brace"

    return scelta


if __name__ == '__main__':
    stampa_ricetta(["pasta", "salsiccia", "funghi", "peperoni"])
