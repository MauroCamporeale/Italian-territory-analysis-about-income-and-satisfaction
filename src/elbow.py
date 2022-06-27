import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")
integrated_datapath = os.path.join(datapath, "integrated")
constructed_datapath = os.path.join(datapath, "constructed")

elbow_datapath = "../results/elbow"

sf_path = "../maps/source/gadm40_ITA_1.shx"

if not os.path.exists(elbow_datapath):
    os.mkdir(elbow_datapath)

redditi_soddisfazione = pd.read_csv(os.path.join(constructed_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"))
regioni = pd.read_csv("../maps/source/nomi_regioni.csv")
soddisfazioni = ["Soddisfazione economica","Soddisfazione salute","Soddisfazione famiglia","Soddisfazione amici","Soddisfazione tempo","Soddisfazione media"]
sf = gpd.read_file(sf_path)

for soddisfazione in soddisfazioni:

    rapporto = []
    rapporti_reg = []

    for index, row in redditi_soddisfazione.iterrows():
        rapporto.append(row[soddisfazione] / (row["Reddito medio"] / 1000))

    redditi_soddisfazione["Rapporto"] = rapporto

    redditi_soddisfazione.sort_values(by=["Rapporto"], ascending=False, inplace=True)

    x = np.arange(1,22)
    y = redditi_soddisfazione[["Rapporto"]].to_numpy()

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.5)
    my_xticks = redditi_soddisfazione[["Regione"]].to_numpy()
    plt.xticks(x, my_xticks, rotation=90)
    ax.plot(x, y)
    # ax.plot(x, intercept + slope * x, label=line)
    plt.savefig(os.path.join(elbow_datapath, 'reddito_soddisfazione_elbow_'+soddisfazione+'_.png'))



    redditi_soddisfazione['Regione'] = redditi_soddisfazione['Regione'].map(lambda s: s.split('(')[0])
    for index, row in regioni.iterrows():
        df = redditi_soddisfazione[redditi_soddisfazione['Regione'] == row["Regioni"]]

        sodd_avg = 0

        for indexx, roww in df.iterrows():
            sodd_avg += roww["Rapporto"]

        rapporti_reg.append(sodd_avg / len(df))

    sf["Rapporto"] = rapporti_reg

    sf.plot(column='Rapporto', cmap='magma_r', k=20, legend=True)
    plt.savefig(os.path.join(elbow_datapath, 'reddito_soddisfazione_mappa_'+soddisfazione+'_.png'))


