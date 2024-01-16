from owlready2 import get_ontology


def carica_ontologia():
    return get_ontology("../onto/food.owl").load()


def query_lista_alimenti():
    nomi_alimenti = []
    onto = carica_ontologia()
    ali = onto.search(type=onto.Alimento)

    for alimento in ali:
        nomi_alimenti.append(alimento.name)

    return nomi_alimenti


def query_cal_alimento(nome_alimento):
    onto = carica_ontologia()
    ali = onto.search_one(iri="*{}*".format(
        nome_alimento))
    return ali.n_calorie.first()


def query_tipo_alimento(nome_alimento):
    onto = carica_ontologia()
    ali = onto.search_one(iri="*{}*".format(
        nome_alimento))
    return ali.tipoDi.first()


def query_cottoIn_alimento(nome_alimento):
    new_ali = []
    onto = carica_ontologia()
    ali = onto.search_one(iri="*{}*".format(
        nome_alimento))

    for alimento in ali.cottoIn:
        new_ali.append(str(alimento).replace('food.', ''))

    return new_ali


def query_abbinatoCon_alimento(nome_alimento):
    new_ali = []
    onto = carica_ontologia()
    ali = onto.search_one(iri="*{}*".format(
        nome_alimento))

    for alimento in ali.abbinatoCon:
        new_ali.append(str(alimento).replace('food.', ''))

    return new_ali
