import pandas as pd
import os
import re
import numpy as np

datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")

# cleaning of redditi x comune

df = pd.read_csv(os.path.join(datapath, "Redditi_per_comune_2020.csv"), sep=';', index_col=False)

# print(list(df.columns))

df.drop(columns=['Anno di imposta', 'Codice catastale', 'Codice Istat Comune', 'Codice Istat Regione',
                 'Reddito da fabbricati - Frequenza', 'Reddito da fabbricati - Ammontare in euro',
                 'Reddito da lavoro dipendente e assimilati - Frequenza',
                 'Reddito da lavoro dipendente e assimilati - Ammontare in euro', 'Reddito da pensione - Frequenza',
                 'Reddito da pensione - Ammontare in euro',
                 # 'Reddito da lavoro autonomo (comprensivo dei valori nulli) - Frequenza',
                 # 'Reddito da lavoro autonomo (comprensivo dei valori nulli) - Ammontare in euro',
                 "Reddito di spettanza dell'imprenditore in contabilita' ordinaria  (comprensivo dei valori nulli) - Frequenza",
                 "Reddito di spettanza dell'imprenditore in contabilita' ordinaria  (comprensivo dei valori nulli) - Ammontare in euro",
                 "Reddito di spettanza dell'imprenditore in contabilita' semplificata (comprensivo dei valori nulli) - Frequenza",
                 "Reddito di spettanza dell'imprenditore in contabilita' semplificata (comprensivo dei valori nulli) - Ammontare in euro",
                 'Reddito da partecipazione  (comprensivo dei valori nulli) - Frequenza',
                 'Reddito da partecipazione  (comprensivo dei valori nulli) - Ammontare in euro',
                 'Reddito imponibile - Frequenza', 'Reddito imponibile - Ammontare in euro',
                 'Imposta netta - Frequenza', 'Imposta netta - Ammontare in euro', 'Bonus spettante - Frequenza',
                 'Bonus spettante - Ammontare in euro', 'Reddito imponibile addizionale - Frequenza',
                 'Reddito imponibile addizionale - Ammontare in euro', 'Addizionale regionale dovuta - Frequenza',
                 'Addizionale regionale dovuta - Ammontare in euro', 'Addizionale comunale dovuta - Frequenza',
                 'Addizionale comunale dovuta - Ammontare in euro'], inplace=True)

df.fillna(float(0), inplace=True)  # sostituzione di 0 a nan &datacleaning&

if not os.path.exists(cleaned_datapath):
    os.mkdir(cleaned_datapath)

df.to_csv(os.path.join(cleaned_datapath, "Redditi_per_comune_2020.csv"))

# cleaning of popolazione x comune

df = pd.read_csv(os.path.join(datapath, "Popolazione_x_comune_2022.csv"))

# print(list(df.columns))
# print(df.head())

df.drop(columns=['ITTER107', 'TIPO_DATO15', 'Tipo di indicatore demografico', 'SEXISTAT1', 'ETA1', 'STATCIV2',
                 'Stato civile', 'TIME', 'Seleziona periodo', 'Flag Codes', 'Flags'], inplace=True)
df['Età'] = df['Età'].map(lambda s: s.split(' ')[0])

if not os.path.exists(cleaned_datapath):
    os.mkdir(cleaned_datapath)

df.to_csv(os.path.join(cleaned_datapath, "Popolazione_x_comune_2022.csv"))

# cleaning of popolazione x provincia

df = pd.read_csv(os.path.join(datapath, "Popolazione_x_provincia.csv"))

# print(list(df.columns))
# print(df.head())

df.drop(columns=['ITTER107', 'TIPO_DATO15', 'Tipo di indicatore demografico', 'SEXISTAT1', 'ETA1', 'STATCIV2',
                 'Stato civile', 'TIME', 'Seleziona periodo', 'Flag Codes', 'Flags'], inplace=True)
df['Età'] = df['Età'].map(lambda s: s.split(' ')[0])

if not os.path.exists(cleaned_datapath):
    os.mkdir(cleaned_datapath)

df.to_csv(os.path.join(cleaned_datapath, "Popolazione_x_provincia.csv"))

# cleaning of comune per provincia

df = pd.read_csv(os.path.join(datapath, "comune_per_provincia_2022.csv"), sep=';')

# print(list(df.columns))
# print(df.head())

df.drop(columns=['Codice Regione', "Codice dell'Unità territoriale sovracomunale \n(valida a fini statistici)",
                 'Codice Provincia (Storico)(1)', 'Progressivo del Comune (2)', 'Codice Comune formato alfanumerico',
                 'Denominazione (Italiana e straniera)', 'Denominazione altra lingua', 'Codice Ripartizione Geografica',
                 'Ripartizione geografica', 'Denominazione Regione', 'Tipologia di Unità territoriale sovracomunale ',
                 'Flag Comune capoluogo di provincia/città metropolitana/libero consorzio',
                 'Codice Comune formato numerico', 'Codice Comune numerico con 110 province (dal 2010 al 2016)',
                 'Codice Comune numerico con 107 province (dal 2006 al 2009)',
                 'Codice Comune numerico con 103 province (dal 1995 al 2005)', 'Codice Catastale del comune',
                 'Codice NUTS1 2010', 'Codice NUTS2 2010 (3) ', 'Codice NUTS3 2010', 'Codice NUTS1 2021',
                 'Codice NUTS2 2021 (3) ', 'Codice NUTS3 2021'], inplace=True)

# correzione mancanza di sigla napoli &datacleaning&

sigla_napoli = 'NA'
df.loc[df[
           "Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)"] == 'Napoli', 'Sigla automobilistica'] = sigla_napoli

if not os.path.exists(cleaned_datapath):
    os.mkdir(cleaned_datapath)

df.to_csv(os.path.join(cleaned_datapath, "comune_per_provincia_2022.csv"))

# cleaning of indicatori demografici per provincia

df = pd.read_csv(os.path.join(datapath, "indicatori_demografici_x_provincia_2022.csv"))

# print(list(df.columns))
# print(df.head())

df.drop(columns=['ITTER107', 'Seleziona periodo', 'Flag Codes', 'Flags'], inplace=True)
df.drop(df[df.TIME != 2020].index, inplace=True)
df.drop_duplicates(inplace=True)  # &datacleaning& valle aosta sia regione che provincia

if not os.path.exists(cleaned_datapath):
    os.mkdir(cleaned_datapath)

df.to_csv(os.path.join(cleaned_datapath, "indicatori_demografici_x_provincia_2020.csv"))

# cleaning of soddisfazione_in_vari_ambiti_per_regione_2020

df = pd.read_csv(os.path.join(datapath, "soddisfazione_in_vari_ambiti_per_regione_2020.csv"))

territorio = []
eco_molto = []
eco_abbastanza = []
eco_poco = []
eco_niente = []
salute_molto = []
salute_abbastanza = []
salute_poco = []
salute_niente = []
famiglia_molto = []
famiglia_abbastanza = []
famiglia_poco = []
famiglia_niente = []
amici_molto = []
amici_abbastanza = []
amici_poco = []
amici_niente = []
tempo_molto = []
tempo_abbastanza = []
tempo_poco = []
tempo_niente = []

territorial_code_pattern = '([A-Z]+[0-9]+)'

df.drop(columns=['Misura', 'TIME', 'Seleziona periodo', 'Flag Codes', 'Flags'], inplace=True)
df.drop(df[df["MISURA_AVQ"] != 'HSC'].index, inplace=True)  # &datacleaning& keeping only values for 100 people
df["TIPO_DATO_AVQ"] = df["TIPO_DATO_AVQ"].apply(lambda x: x.split('_')[1])
df.loc[(df['Tipo dato'] == "abbastanza ", 'Tipo dato')] = "abbastanza" #&datacleaning& value abbastanza for friends have a space at the end

territori = df.drop(columns=["TIPO_DATO_AVQ", "Tipo dato", "MISURA_AVQ", "Value"])
territori.drop_duplicates(inplace=True)

for index, row in territori.iterrows():
    if re.match(territorial_code_pattern, row["ITTER107"]):
        # slicing for regione
        soddisfazione_regionale = df.loc[(df["ITTER107"] == row["ITTER107"])]

        #&data_recoinciliation& tra nomenclature di regione
        if "Valle d'Aosta" in row["Territorio"]:
            territorio.append("Valle d'Aosta")
        elif "Bolzano" in row["Territorio"]:
            territorio.append("Trentino Alto Adige(P.A.Bolzano)")
        elif "Trento" in row["Territorio"]:
            territorio.append("Trentino Alto Adige(P.A.Trento)")
        elif "Emilia-Romagna" in row["Territorio"]:
            territorio.append("Emilia Romagna")
        elif "Friuli-Venezia Giulia" in row["Territorio"]:
            territorio.append("Friuli Venezia Giulia")
        else:
            territorio.append(row["Territorio"])

        soddisfazione_eco = soddisfazione_regionale.loc[(soddisfazione_regionale["TIPO_DATO_AVQ"] == "ECON")]
        soddisfazione_salute = soddisfazione_regionale.loc[(soddisfazione_regionale["TIPO_DATO_AVQ"] == "HEALTH")]
        soddisfazione_famiglia = soddisfazione_regionale.loc[(soddisfazione_regionale["TIPO_DATO_AVQ"] == "FAMILY")]
        soddisfazione_amici = soddisfazione_regionale.loc[(soddisfazione_regionale["TIPO_DATO_AVQ"] == "FRIEND")]
        soddisfazione_tempo = soddisfazione_regionale.loc[(soddisfazione_regionale["TIPO_DATO_AVQ"] == "LEISURE")]

        for indexxx, innerrow in soddisfazione_eco.iterrows():
            if innerrow["Tipo dato"] == 'molto':
                eco_molto.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'abbastanza':
                eco_abbastanza.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'poco':
                eco_poco.append(innerrow["Value"])
            else:
                eco_niente.append(innerrow["Value"])

        for indexxx, innerrow in soddisfazione_salute.iterrows():
            if innerrow["Tipo dato"] == 'molto':
                salute_molto.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'abbastanza':
                salute_abbastanza.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'poco':
                salute_poco.append(innerrow["Value"])
            else:
                salute_niente.append(innerrow["Value"])

        for indexxx, innerrow in soddisfazione_famiglia.iterrows():
            if innerrow["Tipo dato"] == 'molto':
                famiglia_molto.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'abbastanza':
                famiglia_abbastanza.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'poco':
                famiglia_poco.append(innerrow["Value"])
            else:
                famiglia_niente.append(innerrow["Value"])

        for indexxx, innerrow in soddisfazione_amici.iterrows():
            if innerrow["Tipo dato"] == 'molto':
                amici_molto.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'abbastanza':
                amici_abbastanza.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'poco':
                amici_poco.append(innerrow["Value"])
            else:
                amici_niente.append(innerrow["Value"])

        for indexxx, innerrow in soddisfazione_tempo.iterrows():
            if innerrow["Tipo dato"] == 'molto':
                tempo_molto.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'abbastanza':
                tempo_abbastanza.append(innerrow["Value"])
            elif innerrow["Tipo dato"] == 'poco':
                tempo_poco.append(innerrow["Value"])
            else:
                tempo_niente.append(innerrow["Value"])

clean_df = {'Regione': territorio,
            'Eco_molto': eco_molto,
            'Eco_abbastanza': eco_abbastanza,
            'Eco_poco': eco_poco,
            'Eco_niente': eco_niente,
            'Salute_molto': salute_molto,
            'Salute_abbastanza': salute_abbastanza,
            'Salute_poco': salute_poco,
            'Salute_niente': salute_niente,
            'Famiglia_molto': famiglia_molto,
            'Famiglia_abbastanza': famiglia_abbastanza,
            'Famiglia_poco': famiglia_poco,
            'Famiglia_niente': famiglia_niente,
            'Amici_molto': amici_molto,
            'Amici_abbastanza': amici_abbastanza,
            'Amici_poco': amici_poco,
            'Amici_niente': amici_niente,
            'Tempo_molto': tempo_molto,
            'Tempo_abbastanza': tempo_abbastanza,
            'Tempo_poco': tempo_poco,
            'Tempo_niente': tempo_niente,
            }

pd.DataFrame.from_dict(clean_df).to_csv(os.path.join(cleaned_datapath, "soddisfazione_per_regione_2020.csv"))
