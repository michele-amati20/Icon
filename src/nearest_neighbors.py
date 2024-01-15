import random
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler


def carica_dataset_alimenti():
    dataset_path = "./dataset/food-dataset.csv"
    df = pd.read_csv(dataset_path)
    return df


def preprocessing_dataset_alimenti(df):
    # Rimuovi gli apici singoli dalla colonna 'n_calorie'
    df['n_calorie'] = df['n_calorie'].str.replace("'", '')

    # Rimuovi gli apici singoli dalla colonna 'tipoDi'
    df['tipoDi'] = df['tipoDi'].str.replace("'", '')

    df['n_carboidrati'] = df['n_carboidrati'].str.replace("'", '')

    df['n_proteine'] = df['n_proteine'].str.replace("'", '')

    df['n_grassi'] = df['n_grassi'].str.replace("'", '')
    # Rimuovi l'ultima colonna vuota
    df = df.iloc[:, :-1]
    return df


def carica_dataset_voti():
    dataset_voti_path = "./dataset/voti-dataset.csv"
    df_voti = pd.read_csv(dataset_voti_path)
    return df_voti


def unisci_dataset(df1, df2):
    df = pd.merge(df1, df2, on='Entity')
    return df


def estrai_features(df, id):
    voto_id = f"VotoID{id}"
    X = df[["tipoDi", "n_calorie", "n_carboidrati", "n_proteine", "n_grassi", voto_id]]
    X_encoded = pd.get_dummies(X, columns=["tipoDi"])
    return X_encoded


def alimenti_max_voti(df, id):
    return df.nlargest(3, f"VotoID{id}")


def normalizza_dati(df):
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    return df_scaled


def nn(X_scaled, input_scaled, df):
    nn_model = NearestNeighbors(n_neighbors=3)

    # Addestra il modello
    nn_model.fit(X_scaled)

    # Effettua delle predizioni sugli alimenti dell'input
    d, i = nn_model.kneighbors(input_scaled)

    # prende dal dataframe i valori delle posizioni fornite dal modello nn
    alimenti_output = []
    for x in range(0, 3):
        ali_simili = df.iloc[i[x]]
        #print(ali_simili.values, "\n", d[x], end="\n\n")
        array_ali = ali_simili.values
        while True:
            nome_alimento = array_ali[random.randint(0, 2), 0]
            if nome_alimento not in alimenti_output:
                alimenti_output.append(nome_alimento)
                break
    return alimenti_output


def raccomanda_alimenti(id):
    df_alimenti = preprocessing_dataset_alimenti(carica_dataset_alimenti())
    df_voti = carica_dataset_voti()

    df = unisci_dataset(df_alimenti, df_voti)
    X_encoded = estrai_features(df, id)

    df_scelti = alimenti_max_voti(X_encoded, id)

    X_scaled = normalizza_dati(X_encoded)
    df_scelti_scaled = normalizza_dati(df_scelti)

    return nn(X_scaled, df_scelti_scaled, df_alimenti)











