from datetime import date, timedelta
from constraint import Problem
import lista_alimenti
import onto


lista_ali_presenti = []
lista_ali_non_presenti = []


def dominio_date():
    oggi = date.today()
    anno_fa = date.today() - timedelta(days=365 * 4)
    anno = oggi + timedelta(days=365 * 2)
    range_date = [date(1, 1, 1)]
    for x in range((anno - anno_fa).days):
        range_date.append((anno_fa + timedelta(days=x)))

    return range_date


def csp_alimento_disponibile(name):
    for nome in csp():
        if nome['alimento'] == name:
            return "disponibile in casa"
    return "non presente in casa o scaduto"


def csp():
    lista_alimenti.ali_list = lista_alimenti.carica_lista()

    problem = Problem()

    problem.addVariable("alimento", onto.query_lista_alimenti())
    problem.addVariable("data", dominio_date())

    problem.addConstraint(vincolo_alimento_presente, ("alimento",))
    problem.addConstraint(vincolo_data_scadenza, ("alimento", "data",))

    soluzioni = problem.getSolutions()
    return soluzioni


def vincolo_alimento_presente(name):
    return name in lista_alimenti.ali_list


def vincolo_data_scadenza(name, data_scadenza):
    return data_scadenza == lista_alimenti.ali_list[name] and data_scadenza >= date.today()
