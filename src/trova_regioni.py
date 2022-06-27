import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


sf_path = "../maps/source/gadm40_ITA_1.shx"
sf = gpd.read_file(sf_path)
regioni = []

for index, row in sf.iterrows():
    p = gpd.GeoSeries(row['geometry'])
    p.plot()
    plt.show()

    value = input("che regione è ?")

    regioni.append(value)

df = {"Regioni":regioni}
pd.DataFrame.from_dict(df).to_csv("../maps/source/nomi_regioni.csv")

