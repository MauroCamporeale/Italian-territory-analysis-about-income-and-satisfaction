import pandas as pd
import os

datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")
integrated_datapath = os.path.join(datapath, "integrated")
constructed_datapath = os.path.join(datapath, "constructed")


def redditi_e_soddisfazione_media():

    MOLTO = 10
    ABBASTANZA = 6.66
    POCO = 3.33
    NIENTE = 0

    redditi_soddisfazione = pd.read_csv(os.path.join(integrated_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"))

    reddito_medio = []
    reddito_medio_lavoro = []
    sodd_eco = []
    sodd_sal = []
    sodd_fam = []
    sodd_ami = []
    sodd_tem = []
    sodd_avg = []

    for index, row in redditi_soddisfazione.iterrows():
        accumulatore_r = 0

        accumulatore_r += row["Reddito complessivo minore o uguale a zero euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 0 a 10000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 10000 a 15000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 15000 a 26000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 26000 a 55000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 55000 a 75000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 75000 a 120000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo oltre 120000 euro - Ammontare in euro"]
        reddito_medio.append(accumulatore_r / row["Numero contribuenti"])
        reddito_medio_lavoro.append(row["Reddito lavoro - Ammontare in euro"] / row["Reddito lavoro - Frequenza"])

        accumulatore_e = 0

        accumulatore_e += row["Eco_molto"] * MOLTO
        accumulatore_e += row["Eco_abbastanza"] * ABBASTANZA
        accumulatore_e += row["Eco_poco"] * POCO
        accumulatore_e += row["Eco_niente"] * NIENTE
        sodd_eco.append(accumulatore_e / 100)

        accumulatore_s = 0

        accumulatore_s += row["Salute_molto"] * MOLTO
        accumulatore_s += row["Salute_abbastanza"] * ABBASTANZA
        accumulatore_s += row["Salute_poco"] * POCO
        accumulatore_s += row["Salute_niente"] * NIENTE
        sodd_sal.append(accumulatore_s / 100)

        accumulatore_f = 0

        accumulatore_f += row["Famiglia_molto"] * MOLTO
        accumulatore_f += row["Famiglia_abbastanza"] * ABBASTANZA
        accumulatore_f += row["Famiglia_poco"] * POCO
        accumulatore_f += row["Famiglia_niente"] * NIENTE
        sodd_fam.append(accumulatore_f / 100)

        accumulatore_a = 0

        accumulatore_a += row["Amici_molto"] * MOLTO
        accumulatore_a += row["Amici_abbastanza"] * ABBASTANZA
        accumulatore_a += row["Amici_poco"] * POCO
        accumulatore_a += row["Amici_niente"] * NIENTE
        sodd_ami.append(accumulatore_a / 100)

        accumulatore_t = 0

        accumulatore_t += row["Tempo_molto"] * MOLTO
        accumulatore_t += row["Tempo_abbastanza"] * ABBASTANZA
        accumulatore_t += row["Tempo_poco"] * POCO
        accumulatore_t += row["Tempo_niente"] * NIENTE
        sodd_tem.append(accumulatore_t / 100)

        accumulatore_avg = 0
        accumulatore_avg = accumulatore_e / 100 + accumulatore_s / 100 + accumulatore_f / 100 + accumulatore_a / 100 + accumulatore_t / 100

        sodd_avg.append(accumulatore_avg / 5)

    redditi_soddisfazione['Reddito medio'] = reddito_medio
    redditi_soddisfazione['Reddito medio lavoro'] = reddito_medio_lavoro
    redditi_soddisfazione['Soddisfazione economica'] = sodd_eco
    redditi_soddisfazione['Soddisfazione salute'] = sodd_sal
    redditi_soddisfazione['Soddisfazione famiglia'] = sodd_fam
    redditi_soddisfazione['Soddisfazione amici'] = sodd_ami
    redditi_soddisfazione['Soddisfazione tempo'] = sodd_tem
    redditi_soddisfazione['Soddisfazione media'] = sodd_avg

    if not os.path.exists(constructed_datapath):
        os.mkdir(constructed_datapath)

    redditi_soddisfazione.to_csv(os.path.join(constructed_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"), index=False)

def redditi_e_indicatori_media():

    redditi_indicatori = pd.read_csv(os.path.join(integrated_datapath, "Redditi_e_indicatori_per_provincia_2020.csv"))

    reddito_medio = []
    reddito_medio_lavoro = []

    for index, row in redditi_indicatori.iterrows():
        accumulatore_r = 0

        accumulatore_r += row["Reddito complessivo minore o uguale a zero euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 0 a 10000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 10000 a 15000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 15000 a 26000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 26000 a 55000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 55000 a 75000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo da 75000 a 120000 euro - Ammontare in euro"]
        accumulatore_r += row["Reddito complessivo oltre 120000 euro - Ammontare in euro"]
        reddito_medio.append(accumulatore_r / row["Numero contribuenti"])
        reddito_medio_lavoro.append(row["Reddito lavoro - Ammontare in euro"] / row["Reddito lavoro - Frequenza"])

    redditi_indicatori['Reddito medio'] = reddito_medio
    redditi_indicatori['Reddito medio lavoro'] = reddito_medio_lavoro

    if not os.path.exists(constructed_datapath):
        os.mkdir(constructed_datapath)

    redditi_indicatori.to_csv(os.path.join(constructed_datapath, "Redditi_e_indicatori_per_provincia_2020.csv"), index=False)

redditi_e_indicatori_media()
redditi_e_soddisfazione_media()














