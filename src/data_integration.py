import pandas as pd
import os
import math

datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")
integrated_datapath = os.path.join(datapath, "integrated")

# join between redditi per comune e comune per provincia &dataintegration&
def creazione_redditi_per_provincia():

    redditi = pd.read_csv(os.path.join(cleaned_datapath, "Redditi_per_comune_2020.csv"))
    redditi.loc[redditi["Sigla Provincia"] == "0.0", "Sigla Provincia"] = 'NA' #correzione per NA mancante &datacleaning&

    cxp = pd.read_csv(os.path.join(cleaned_datapath, "comune_per_provincia_2022.csv")).rename(columns= {'Denominazione in italiano':'comune', "Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)":'provincia', 'Sigla automobilistica':'sigla'})
    provincie = cxp.drop(columns=['comune', 'Unnamed: 0']).drop_duplicates() #selezione di solo la colonna provincia e sigla automobilistica &dataselection&
    provincie[provincie.isna()] = 'NA' #correzione per NA letto come nan &datacleaning&



    sigla_prov=[]
    provincia=[]
    regione=[]
    numero_comuni=[]
    numero_contribuenti=[]
    reddito_lavoro_frequenza=[]
    reddito_lavoro_ammontare=[]
    reddito_meno_zero_frequenza=[]
    reddito_meno_zero_ammontare=[]
    reddito_0_10000_frequenza=[]
    reddito_0_10000_ammontare=[]
    reddito_10000_15000_frequenza = []
    reddito_10000_15000_ammontare = []
    reddito_15000_26000_frequenza = []
    reddito_15000_26000_ammontare = []
    reddito_26000_55000_frequenza = []
    reddito_26000_55000_ammontare = []
    reddito_55000_75000_frequenza = []
    reddito_55000_75000_ammontare = []
    reddito_75000_120000_frequenza = []
    reddito_75000_120000_ammontare = []
    reddito_oltre_120000_frequenza = []
    reddito_oltre_120000_ammontare = []



    for index, prov in provincie.iterrows():
        sigla_prov.append(prov.sigla)
        provincia.append(prov.provincia)
        is_regione_inserted = False

        contatore_contribuenti = 0
        contatore_lavoro = 0
        sommatoria_lavoro = 0
        contatore_r_meno_0 = 0
        sommatoria_r_meno_0 = 0
        contatore_r_0_10 = 0
        sommatoria_r_0_10 = 0
        contatore_r_10_15 = 0
        sommatoria_r_10_15 = 0
        contatore_r_15_26 = 0
        sommatoria_r_15_26 = 0
        contatore_r_26_55 = 0
        sommatoria_r_26_55 = 0
        contatore_r_55_75 = 0
        sommatoria_r_55_75 = 0
        contatore_r_75_120 = 0
        sommatoria_r_75_120 = 0
        contatore_r_120 = 0
        sommatoria_r_120 = 0


        #slicing for provincia
        redditi_provinciali = redditi.loc[(redditi["Sigla Provincia"] == prov.sigla)]
        numero_comuni.append(len(redditi_provinciali))
        print(len(redditi_provinciali))

        for indexx, comune in redditi_provinciali.iterrows():

            if not is_regione_inserted:
                regione.append(comune["Regione"])
                is_regione_inserted = True

            contatore_contribuenti += comune["Numero contribuenti"]
            contatore_lavoro += comune["Reddito da lavoro autonomo (comprensivo dei valori nulli) - Frequenza"]
            sommatoria_lavoro += comune["Reddito da lavoro autonomo (comprensivo dei valori nulli) - Ammontare in euro"]
            contatore_r_meno_0 += comune["Reddito complessivo minore o uguale a zero euro - Frequenza"]
            sommatoria_r_meno_0 += comune["Reddito complessivo minore o uguale a zero euro - Ammontare in euro"]
            contatore_r_0_10 += comune["Reddito complessivo da 0 a 10000 euro - Frequenza"]
            sommatoria_r_0_10 += comune["Reddito complessivo da 0 a 10000 euro - Ammontare in euro"]
            contatore_r_10_15 += comune["Reddito complessivo da 10000 a 15000 euro - Frequenza"]
            sommatoria_r_10_15 += comune["Reddito complessivo da 10000 a 15000 euro - Ammontare in euro"]
            contatore_r_15_26 += comune["Reddito complessivo da 15000 a 26000 euro - Frequenza"]
            sommatoria_r_15_26 += comune["Reddito complessivo da 15000 a 26000 euro - Ammontare in euro"]
            contatore_r_26_55 += comune["Reddito complessivo da 26000 a 55000 euro - Frequenza"]
            sommatoria_r_26_55 += comune["Reddito complessivo da 26000 a 55000 euro - Ammontare in euro"]
            contatore_r_55_75 += comune["Reddito complessivo da 55000 a 75000 euro - Frequenza"]
            sommatoria_r_55_75 += comune["Reddito complessivo da 55000 a 75000 euro - Ammontare in euro"]
            contatore_r_75_120 += comune["Reddito complessivo da 75000 a 120000 euro - Frequenza"]
            sommatoria_r_75_120 += comune["Reddito complessivo da 75000 a 120000 euro - Ammontare in euro"]
            contatore_r_120 += comune["Reddito complessivo oltre 120000 euro - Frequenza"]
            sommatoria_r_120 += comune["Reddito complessivo oltre 120000 euro - Ammontare in euro"]

        numero_contribuenti.append(contatore_contribuenti)
        reddito_lavoro_frequenza.append(contatore_lavoro)
        reddito_lavoro_ammontare.append(sommatoria_lavoro)
        reddito_meno_zero_frequenza.append(contatore_r_meno_0)
        reddito_meno_zero_ammontare.append(sommatoria_r_meno_0)
        reddito_0_10000_frequenza.append(contatore_r_0_10)
        reddito_0_10000_ammontare.append(sommatoria_r_0_10)
        reddito_10000_15000_frequenza.append(contatore_r_10_15)
        reddito_10000_15000_ammontare.append(sommatoria_r_10_15)
        reddito_15000_26000_frequenza.append(contatore_r_15_26)
        reddito_15000_26000_ammontare.append(sommatoria_r_15_26)
        reddito_26000_55000_frequenza.append(contatore_r_26_55)
        reddito_26000_55000_ammontare.append(sommatoria_r_26_55)
        reddito_55000_75000_frequenza.append(contatore_r_55_75)
        reddito_55000_75000_ammontare.append(sommatoria_r_55_75)
        reddito_75000_120000_frequenza.append(contatore_r_75_120)
        reddito_75000_120000_ammontare.append(sommatoria_r_75_120)
        reddito_oltre_120000_frequenza.append(contatore_r_120)
        reddito_oltre_120000_ammontare.append(sommatoria_r_120)


    redditi_per_provincia = {'Sigla provincia':sigla_prov,
                             'Provincia':provincia,
                             'Regione':regione,
                             'Numero comuni':numero_comuni,
                             "Numero contribuenti":numero_contribuenti,
                             "Reddito lavoro - Frequenza": reddito_lavoro_frequenza,
                             "Reddito lavoro - Ammontare in euro": reddito_lavoro_ammontare,
                             "Reddito complessivo minore o uguale a zero euro - Frequenza":reddito_meno_zero_frequenza,
                             "Reddito complessivo minore o uguale a zero euro - Ammontare in euro":reddito_meno_zero_ammontare,
                             "Reddito complessivo da 0 a 10000 euro - Frequenza":reddito_0_10000_frequenza,
                             "Reddito complessivo da 0 a 10000 euro - Ammontare in euro":reddito_0_10000_ammontare,
                             "Reddito complessivo da 10000 a 15000 euro - Frequenza":reddito_10000_15000_frequenza,
                             "Reddito complessivo da 10000 a 15000 euro - Ammontare in euro":reddito_10000_15000_ammontare,
                             "Reddito complessivo da 15000 a 26000 euro - Frequenza":reddito_15000_26000_frequenza,
                             "Reddito complessivo da 15000 a 26000 euro - Ammontare in euro":reddito_15000_26000_ammontare,
                             "Reddito complessivo da 26000 a 55000 euro - Frequenza":reddito_26000_55000_frequenza,
                             "Reddito complessivo da 26000 a 55000 euro - Ammontare in euro":reddito_26000_55000_ammontare,
                             "Reddito complessivo da 55000 a 75000 euro - Frequenza":reddito_55000_75000_frequenza,
                             "Reddito complessivo da 55000 a 75000 euro - Ammontare in euro":reddito_55000_75000_ammontare,
                             "Reddito complessivo da 75000 a 120000 euro - Frequenza":reddito_75000_120000_frequenza,
                             "Reddito complessivo da 75000 a 120000 euro - Ammontare in euro":reddito_75000_120000_ammontare,
                             "Reddito complessivo oltre 120000 euro - Frequenza":reddito_oltre_120000_frequenza,
                             "Reddito complessivo oltre 120000 euro - Ammontare in euro":reddito_oltre_120000_ammontare }


    if not os.path.exists(integrated_datapath):
        os.mkdir(integrated_datapath)

    pd.DataFrame.from_dict(redditi_per_provincia).to_csv(os.path.join(integrated_datapath, "Redditi_per_provincia_2020.csv"))

# join between redditi per provincia e indicatori demografici per provincia &dataintegration&
def creazione_redditi_provincia_indicatori():

    redditi = pd.read_csv(os.path.join(integrated_datapath, "Redditi_per_provincia_2020.csv"))
    redditi.loc[redditi["Sigla provincia"].isna(), "Sigla provincia"] = 'NA'  # correzione per NA mancante &datacleaning&

    indicatori = pd.read_csv(os.path.join(cleaned_datapath, "indicatori_demografici_x_provincia_2020.csv")).rename(
        columns={'Territorio': 'Provincia',
                 "TIPO_DATO15": 'Indicatore',
                 "Tipo indicatore":'Spiegazione',
                 "TIME":'Anno',
                 'Value': 'Valore'})
    indicatori.drop(columns=['Spiegazione', 'Anno'], inplace=True)# selezione delle colonne spiegazione e anno &dataselection&

    Birthrate=[]
    Deathrate=[]
    Marrate=[]
    Nmigratein=[]
    Nmigrateab=[]
    Nmigrateor=[]
    Tmigrate=[]
    Growthraten=[]
    Growthratet=[]
    Tfr=[]
    Meanagech=[]
    Lifeexp0M=[]
    Lifeexp65M=[]
    Lifeexp0F=[]
    Lifeexp65F=[]
    Pop014=[]
    Pop1564=[]
    Pop65over=[]
    Dependrate=[]
    Oldagedepr=[]
    Ageindex=[]
    Meanagep=[]
    Lifeexp0T=[]
    Lifeexp65T=[]

    for index, provincia in redditi.iterrows():
        # slicing for provincia
        prov = ""
        # &datareconciliation& valle d'aosta e bolzano (spazio prima e dopo lo /) reggio calabria ha il di
        if '/' in provincia.Provincia:
            prov = provincia.Provincia.split('/')[0] + " / " + provincia.Provincia.split('/')[1]
        elif provincia.Provincia == "Reggio Calabria":
            prov = "Reggio di Calabria"
        else:
            prov = provincia.Provincia

        indicatori_provinciali = indicatori.loc[(indicatori["Provincia"] == prov)]

        Birthrate.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "BIRTHRATE", 'Valore'].iloc[0])
        Deathrate.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "DEATHRATE", 'Valore'].iloc[0])
        Marrate.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "MARRATE", 'Valore'].iloc[0])
        Nmigratein.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "NMIGRATEIN", 'Valore'].iloc[0])
        Nmigrateab.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "NMIGRATEAB", 'Valore'].iloc[0])
        Nmigrateor.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "NMIGRATEOR", 'Valore'].iloc[0])
        Tmigrate.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "TMIGRATE", 'Valore'].iloc[0])
        Growthraten.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "GROWTHRATEN", 'Valore'].iloc[0])
        Growthratet.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "GROWTHRATET", 'Valore'].iloc[0])
        Tfr.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "TFR", 'Valore'].iloc[0])
        Meanagech.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "MEANAGECH", 'Valore'].iloc[0])
        Lifeexp0M.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP0M", 'Valore'].iloc[0])
        Lifeexp65M.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP65M", 'Valore'].iloc[0])
        Lifeexp0F.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP0F", 'Valore'].iloc[0])
        Lifeexp65F.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP65F", 'Valore'].iloc[0])
        Pop014.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "POP014", 'Valore'].iloc[0])
        Pop1564.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "POP1564", 'Valore'].iloc[0])
        Pop65over.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "POP65OVER", 'Valore'].iloc[0])
        Dependrate.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "DEPENDRATE", 'Valore'].iloc[0])
        Oldagedepr.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "OLDAGEDEPR", 'Valore'].iloc[0])
        Ageindex.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "AGEINDEX", 'Valore'].iloc[0])
        Meanagep.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "MEANAGEP", 'Valore'].iloc[0])
        Lifeexp0T.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP0T", 'Valore'].iloc[0])
        Lifeexp65T.append(indicatori_provinciali.loc[indicatori_provinciali['Indicatore'] == "LIFEEXP65T", 'Valore'].iloc[0])


    redditi['BIRTHRATE'] = Birthrate
    redditi['DEATHRATE'] = Deathrate
    redditi['MARRATE'] = Marrate
    redditi['NMIGRATEIN'] = Nmigratein
    redditi['NMIGRATEAB'] = Nmigrateab
    redditi['NMIGRATEOR'] = Nmigrateor
    redditi['TMIGRATE'] = Tmigrate
    redditi['GROWTHRATEN'] = Growthraten
    redditi['GROWTHRATET'] = Growthratet
    redditi['TFR'] = Tfr
    redditi['MEANAGECH'] = Meanagech
    redditi['LIFEEXP0M'] = Lifeexp0M
    redditi['LIFEEXP65M'] = Lifeexp65M
    redditi['LIFEEXP0F'] = Lifeexp0F
    redditi['LIFEEXP65F'] = Lifeexp65F
    redditi['POP014'] = Pop014
    redditi['POP1564'] = Pop1564
    redditi['POP65OVER'] = Pop65over
    redditi['DEPENDRATE'] = Dependrate
    redditi['OLDAGEDEPR'] = Oldagedepr
    redditi['AGEINDEX'] = Ageindex
    redditi['MEANAGEP'] = Meanagep
    redditi['LIFEEXP0T'] = Lifeexp0T
    redditi['LIFEEXP65T'] = Lifeexp65T


    if not os.path.exists(integrated_datapath):
        os.mkdir(integrated_datapath)

    redditi.to_csv(os.path.join(integrated_datapath, "Redditi_e_indicatori_per_provincia_2020.csv"), index=False)

def creazione_redditi_soddisfazione_per_regione():

    redditi = pd.read_csv(os.path.join(integrated_datapath, "Redditi_per_provincia_2020.csv"))
    redditi.loc[redditi["Sigla provincia"].isna(), "Sigla provincia"] = 'NA'  # correzione per NA mancante &datacleaning&

    regioni = redditi.drop(columns=['Unnamed: 0','Reddito lavoro - Frequenza','Reddito lavoro - Ammontare in euro','Sigla provincia','Provincia','Numero comuni','Numero contribuenti','Reddito complessivo minore o uguale a zero euro - Frequenza','Reddito complessivo minore o uguale a zero euro - Ammontare in euro','Reddito complessivo da 0 a 10000 euro - Frequenza','Reddito complessivo da 0 a 10000 euro - Ammontare in euro','Reddito complessivo da 10000 a 15000 euro - Frequenza','Reddito complessivo da 10000 a 15000 euro - Ammontare in euro','Reddito complessivo da 15000 a 26000 euro - Frequenza','Reddito complessivo da 15000 a 26000 euro - Ammontare in euro','Reddito complessivo da 26000 a 55000 euro - Frequenza','Reddito complessivo da 26000 a 55000 euro - Ammontare in euro','Reddito complessivo da 55000 a 75000 euro - Frequenza','Reddito complessivo da 55000 a 75000 euro - Ammontare in euro','Reddito complessivo da 75000 a 120000 euro - Frequenza','Reddito complessivo da 75000 a 120000 euro - Ammontare in euro','Reddito complessivo oltre 120000 euro - Frequenza','Reddito complessivo oltre 120000 euro - Ammontare in euro']).drop_duplicates()  # selezione di solo la colonna provincia e sigla automobilistica &dataselection&

    soddisfazione = pd.read_csv(os.path.join(cleaned_datapath, "soddisfazione_per_regione_2020.csv"))

    regione = []
    numero_comuni = []
    numero_contribuenti = []
    e_molto = []
    e_abbastanza = []
    e_poco = []
    e_niente = []
    s_molto = []
    s_abbastanza = []
    s_poco = []
    s_niente = []
    f_molto = []
    f_abbastanza = []
    f_poco = []
    f_niente = []
    a_molto = []
    a_abbastanza = []
    a_poco = []
    a_niente = []
    t_molto = []
    t_abbastanza = []
    t_poco = []
    t_niente = []
    reddito_lavoro_frequenza = []
    reddito_lavoro_ammontare = []
    reddito_meno_zero_frequenza = []
    reddito_meno_zero_ammontare = []
    reddito_0_10000_frequenza = []
    reddito_0_10000_ammontare = []
    reddito_10000_15000_frequenza = []
    reddito_10000_15000_ammontare = []
    reddito_15000_26000_frequenza = []
    reddito_15000_26000_ammontare = []
    reddito_26000_55000_frequenza = []
    reddito_26000_55000_ammontare = []
    reddito_55000_75000_frequenza = []
    reddito_55000_75000_ammontare = []
    reddito_75000_120000_frequenza = []
    reddito_75000_120000_ammontare = []
    reddito_oltre_120000_frequenza = []
    reddito_oltre_120000_ammontare = []

    for index, reg in regioni.iterrows():
        regione.append(reg.Regione)

        soddisfazione_regionale = soddisfazione.loc[(soddisfazione["Regione"] == reg.Regione)]

        e_molto.append(soddisfazione_regionale["Eco_molto"].values[0])
        e_abbastanza.append(soddisfazione_regionale["Eco_abbastanza"].values[0])
        e_poco.append(soddisfazione_regionale["Eco_poco"].values[0])
        e_niente.append(soddisfazione_regionale["Eco_niente"].values[0])
        s_molto.append(soddisfazione_regionale["Salute_molto"].values[0])
        s_abbastanza.append(soddisfazione_regionale["Salute_abbastanza"].values[0])
        s_poco.append(soddisfazione_regionale["Salute_poco"].values[0])
        s_niente.append(soddisfazione_regionale["Salute_niente"].values[0])
        f_molto.append(soddisfazione_regionale["Famiglia_molto"].values[0])
        f_abbastanza.append(soddisfazione_regionale["Famiglia_abbastanza"].values[0])
        f_poco.append(soddisfazione_regionale["Famiglia_poco"].values[0])
        f_niente.append(soddisfazione_regionale["Famiglia_niente"].values[0])
        a_molto.append(soddisfazione_regionale["Amici_molto"].values[0])
        a_abbastanza.append(soddisfazione_regionale["Amici_abbastanza"].values[0])
        a_poco.append(soddisfazione_regionale["Amici_poco"].values[0])
        a_niente.append(soddisfazione_regionale["Amici_niente"].values[0])
        t_molto.append(soddisfazione_regionale["Tempo_molto"].values[0])
        t_abbastanza.append(soddisfazione_regionale["Tempo_abbastanza"].values[0])
        t_poco.append(soddisfazione_regionale["Tempo_poco"].values[0])
        t_niente.append(soddisfazione_regionale["Tempo_niente"].values[0])

        contatore_comuni = 0
        contatore_contribuenti = 0
        contatore_lavoro = 0
        sommatoria_lavoro = 0
        contatore_r_meno_0 = 0
        sommatoria_r_meno_0 = 0
        contatore_r_0_10 = 0
        sommatoria_r_0_10 = 0
        contatore_r_10_15 = 0
        sommatoria_r_10_15 = 0
        contatore_r_15_26 = 0
        sommatoria_r_15_26 = 0
        contatore_r_26_55 = 0
        sommatoria_r_26_55 = 0
        contatore_r_55_75 = 0
        sommatoria_r_55_75 = 0
        contatore_r_75_120 = 0
        sommatoria_r_75_120 = 0
        contatore_r_120 = 0
        sommatoria_r_120 = 0

        # slicing for regione
        redditi_regionali = redditi.loc[(redditi["Regione"] == reg.Regione)]

        for indexx, provincia in redditi_regionali.iterrows():

            contatore_contribuenti += provincia["Numero contribuenti"]
            contatore_comuni += provincia["Numero comuni"]
            contatore_lavoro += provincia["Reddito lavoro - Frequenza"]
            sommatoria_lavoro += provincia["Reddito lavoro - Ammontare in euro"]
            contatore_r_meno_0 += provincia["Reddito complessivo minore o uguale a zero euro - Frequenza"]
            sommatoria_r_meno_0 += provincia["Reddito complessivo minore o uguale a zero euro - Ammontare in euro"]
            contatore_r_0_10 += provincia["Reddito complessivo da 0 a 10000 euro - Frequenza"]
            sommatoria_r_0_10 += provincia["Reddito complessivo da 0 a 10000 euro - Ammontare in euro"]
            contatore_r_10_15 += provincia["Reddito complessivo da 10000 a 15000 euro - Frequenza"]
            sommatoria_r_10_15 += provincia["Reddito complessivo da 10000 a 15000 euro - Ammontare in euro"]
            contatore_r_15_26 += provincia["Reddito complessivo da 15000 a 26000 euro - Frequenza"]
            sommatoria_r_15_26 += provincia["Reddito complessivo da 15000 a 26000 euro - Ammontare in euro"]
            contatore_r_26_55 += provincia["Reddito complessivo da 26000 a 55000 euro - Frequenza"]
            sommatoria_r_26_55 += provincia["Reddito complessivo da 26000 a 55000 euro - Ammontare in euro"]
            contatore_r_55_75 += provincia["Reddito complessivo da 55000 a 75000 euro - Frequenza"]
            sommatoria_r_55_75 += provincia["Reddito complessivo da 55000 a 75000 euro - Ammontare in euro"]
            contatore_r_75_120 += provincia["Reddito complessivo da 75000 a 120000 euro - Frequenza"]
            sommatoria_r_75_120 += provincia["Reddito complessivo da 75000 a 120000 euro - Ammontare in euro"]
            contatore_r_120 += provincia["Reddito complessivo oltre 120000 euro - Frequenza"]
            sommatoria_r_120 += provincia["Reddito complessivo oltre 120000 euro - Ammontare in euro"]

        numero_contribuenti.append(contatore_contribuenti)
        numero_comuni.append(contatore_comuni)
        reddito_lavoro_frequenza.append(contatore_lavoro)
        reddito_lavoro_ammontare.append(sommatoria_lavoro)
        reddito_meno_zero_frequenza.append(contatore_r_meno_0)
        reddito_meno_zero_ammontare.append(sommatoria_r_meno_0)
        reddito_0_10000_frequenza.append(contatore_r_0_10)
        reddito_0_10000_ammontare.append(sommatoria_r_0_10)
        reddito_10000_15000_frequenza.append(contatore_r_10_15)
        reddito_10000_15000_ammontare.append(sommatoria_r_10_15)
        reddito_15000_26000_frequenza.append(contatore_r_15_26)
        reddito_15000_26000_ammontare.append(sommatoria_r_15_26)
        reddito_26000_55000_frequenza.append(contatore_r_26_55)
        reddito_26000_55000_ammontare.append(sommatoria_r_26_55)
        reddito_55000_75000_frequenza.append(contatore_r_55_75)
        reddito_55000_75000_ammontare.append(sommatoria_r_55_75)
        reddito_75000_120000_frequenza.append(contatore_r_75_120)
        reddito_75000_120000_ammontare.append(sommatoria_r_75_120)
        reddito_oltre_120000_frequenza.append(contatore_r_120)
        reddito_oltre_120000_ammontare.append(sommatoria_r_120)

    redditi_e_soddisfazione_per_regione = {'Regione': regione,
                             'Numero comuni': numero_comuni,
                             "Numero contribuenti": numero_contribuenti,
                             "Eco_molto": e_molto,
                             "Eco_abbastanza": e_abbastanza,
                             "Eco_poco": e_poco,
                             "Eco_niente": e_niente,
                             "Salute_molto": s_molto,
                             "Salute_abbastanza": s_abbastanza,
                             "Salute_poco": s_poco,
                             "Salute_niente": s_niente,
                             "Famiglia_molto": f_molto,
                             "Famiglia_abbastanza": f_abbastanza,
                             "Famiglia_poco": f_poco,
                             "Famiglia_niente": f_niente,
                             "Amici_molto": a_molto,
                             "Amici_abbastanza": a_abbastanza,
                             "Amici_poco": a_poco,
                             "Amici_niente": a_niente,
                             "Tempo_molto": t_molto,
                             "Tempo_abbastanza": t_abbastanza,
                             "Tempo_poco": t_poco,
                             "Tempo_niente": t_niente,
                             "Reddito lavoro - Frequenza": reddito_lavoro_frequenza,
                             "Reddito lavoro - Ammontare in euro": reddito_lavoro_ammontare,
                             "Reddito complessivo minore o uguale a zero euro - Frequenza": reddito_meno_zero_frequenza,
                             "Reddito complessivo minore o uguale a zero euro - Ammontare in euro": reddito_meno_zero_ammontare,
                             "Reddito complessivo da 0 a 10000 euro - Frequenza": reddito_0_10000_frequenza,
                             "Reddito complessivo da 0 a 10000 euro - Ammontare in euro": reddito_0_10000_ammontare,
                             "Reddito complessivo da 10000 a 15000 euro - Frequenza": reddito_10000_15000_frequenza,
                             "Reddito complessivo da 10000 a 15000 euro - Ammontare in euro": reddito_10000_15000_ammontare,
                             "Reddito complessivo da 15000 a 26000 euro - Frequenza": reddito_15000_26000_frequenza,
                             "Reddito complessivo da 15000 a 26000 euro - Ammontare in euro": reddito_15000_26000_ammontare,
                             "Reddito complessivo da 26000 a 55000 euro - Frequenza": reddito_26000_55000_frequenza,
                             "Reddito complessivo da 26000 a 55000 euro - Ammontare in euro": reddito_26000_55000_ammontare,
                             "Reddito complessivo da 55000 a 75000 euro - Frequenza": reddito_55000_75000_frequenza,
                             "Reddito complessivo da 55000 a 75000 euro - Ammontare in euro": reddito_55000_75000_ammontare,
                             "Reddito complessivo da 75000 a 120000 euro - Frequenza": reddito_75000_120000_frequenza,
                             "Reddito complessivo da 75000 a 120000 euro - Ammontare in euro": reddito_75000_120000_ammontare,
                             "Reddito complessivo oltre 120000 euro - Frequenza": reddito_oltre_120000_frequenza,
                             "Reddito complessivo oltre 120000 euro - Ammontare in euro": reddito_oltre_120000_ammontare}

    if not os.path.exists(integrated_datapath):
        os.mkdir(integrated_datapath)

    luca = pd.DataFrame.from_dict(redditi_e_soddisfazione_per_regione)
    luca.to_csv(os.path.join(integrated_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"), index=False)


creazione_redditi_per_provincia()
creazione_redditi_provincia_indicatori()
creazione_redditi_soddisfazione_per_regione()