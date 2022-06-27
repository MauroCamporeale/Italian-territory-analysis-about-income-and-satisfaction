import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")
integrated_datapath = os.path.join(datapath, "integrated")
constructed_datapath = os.path.join(datapath, "constructed")

correlations_datapath = "../results/correlations"

if not os.path.exists(correlations_datapath):
    os.mkdir(correlations_datapath)

redditi_soddisfazione = pd.read_csv(os.path.join(constructed_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"))
redditi_indicatori = pd.read_csv(os.path.join(constructed_datapath, "Redditi_e_indicatori_per_provincia_2020.csv"))


def correlation_redditi_soddisfazione():

    sliced_df = redditi_soddisfazione[["Reddito medio","Soddisfazione economica","Soddisfazione salute","Soddisfazione famiglia","Soddisfazione amici","Soddisfazione tempo","Soddisfazione media"]]
    sliced_df = sliced_df.to_numpy().transpose()

    corr_matrix = np.corrcoef(sliced_df).round(decimals=2)

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=('reddito', 'eco', 'sal', 'fam', 'ami', 'tem', 'avg'))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=('reddito', 'eco', 'sal', 'fam', 'ami', 'tem', 'avg'))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_soddisfazione.png'))

def correlation_reddito_lavoro_soddisfazione():

    sliced_df = redditi_soddisfazione[["Reddito medio lavoro","Soddisfazione economica","Soddisfazione salute","Soddisfazione famiglia","Soddisfazione amici","Soddisfazione tempo","Soddisfazione media"]]
    sliced_df = sliced_df.to_numpy().transpose()

    corr_matrix = np.corrcoef(sliced_df).round(decimals=2)

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=('reddito lavoro', 'eco', 'sal', 'fam', 'ami', 'tem', 'avg'))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=('reddito lavoro', 'eco', 'sal', 'fam', 'ami', 'tem', 'avg'))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_soddisfazione.png'))


def correlation_redditi_indicatori():

    sliced_df1 = redditi_indicatori[["Reddito medio","BIRTHRATE","DEATHRATE","MARRATE"]]
    sliced_df1 = sliced_df1.to_numpy().transpose()

    sliced_df2 = redditi_indicatori[["Reddito medio", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"]]
    sliced_df2 = sliced_df2.to_numpy().transpose()

    sliced_df3 = redditi_indicatori[["Reddito medio","GROWTHRATEN", "GROWTHRATET", "TFR"]]
    sliced_df3 = sliced_df3.to_numpy().transpose()

    sliced_df4 = redditi_indicatori[["Reddito medio","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"]]
    sliced_df4 = sliced_df4.to_numpy().transpose()

    sliced_df5 = redditi_indicatori[["Reddito medio","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"]]
    sliced_df5 = sliced_df5.to_numpy().transpose()

    sliced_df6 = redditi_indicatori[["Reddito medio", "DEPENDRATE", "OLDAGEDEPR"]]
    sliced_df6 = sliced_df6.to_numpy().transpose()

    corr_matrix1 = np.corrcoef(sliced_df1).round(decimals=2)
    corr_matrix2 = np.corrcoef(sliced_df2).round(decimals=2)
    corr_matrix3 = np.corrcoef(sliced_df3).round(decimals=2)
    corr_matrix4 = np.corrcoef(sliced_df4).round(decimals=2)
    corr_matrix5 = np.corrcoef(sliced_df5).round(decimals=2)
    corr_matrix6 = np.corrcoef(sliced_df6).round(decimals=2)

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix1)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito medio","BIRTHRATE","DEATHRATE","MARRATE"))
    ax.yaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito medio","BIRTHRATE","DEATHRATE","MARRATE"))
    ax.set_ylim(3.5, -0.5)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, corr_matrix1[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_rates.png'))


    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix2)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4), ticklabels=("Reddito medio", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4), ticklabels=("Reddito medio", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"))
    ax.set_ylim(4.5, -0.5)
    for i in range(5):
        for j in range(5):
            ax.text(j, i, corr_matrix2[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_migrate.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix3)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito medio","GROWTHRATEN", "GROWTHRATET", "TFR"))
    ax.yaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito medio","GROWTHRATEN", "GROWTHRATET", "TFR"))
    ax.set_ylim(3.5, -0.5)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, corr_matrix3[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_growth.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix4)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito medio","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito medio","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix4[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_age.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix5)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito medio","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito medio","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix5[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_lifeexp.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix6)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2), ticklabels=("Reddito medio", "DEPENDRATE", "OLDAGEDEPR"))
    ax.yaxis.set(ticks=(0, 1, 2), ticklabels=("Reddito medio", "DEPENDRATE", "OLDAGEDEPR"))
    ax.set_ylim(2.5, -0.5)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, corr_matrix6[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_indicatori_depend.png'))


def correlation_reddito_lavoro_indicatori():

    sliced_df1 = redditi_indicatori[["Reddito medio lavoro","BIRTHRATE","DEATHRATE","MARRATE"]]
    sliced_df1 = sliced_df1.to_numpy().transpose()

    sliced_df2 = redditi_indicatori[["Reddito medio lavoro", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"]]
    sliced_df2 = sliced_df2.to_numpy().transpose()

    sliced_df3 = redditi_indicatori[["Reddito medio lavoro","GROWTHRATEN", "GROWTHRATET", "TFR"]]
    sliced_df3 = sliced_df3.to_numpy().transpose()

    sliced_df4 = redditi_indicatori[["Reddito medio lavoro","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"]]
    sliced_df4 = sliced_df4.to_numpy().transpose()

    sliced_df5 = redditi_indicatori[["Reddito medio lavoro","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"]]
    sliced_df5 = sliced_df5.to_numpy().transpose()

    sliced_df6 = redditi_indicatori[["Reddito medio lavoro", "DEPENDRATE", "OLDAGEDEPR"]]
    sliced_df6 = sliced_df6.to_numpy().transpose()

    corr_matrix1 = np.corrcoef(sliced_df1).round(decimals=2)
    corr_matrix2 = np.corrcoef(sliced_df2).round(decimals=2)
    corr_matrix3 = np.corrcoef(sliced_df3).round(decimals=2)
    corr_matrix4 = np.corrcoef(sliced_df4).round(decimals=2)
    corr_matrix5 = np.corrcoef(sliced_df5).round(decimals=2)
    corr_matrix6 = np.corrcoef(sliced_df6).round(decimals=2)

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix1)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito lavoro","BIRTHRATE","DEATHRATE","MARRATE"))
    ax.yaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito lavoro","BIRTHRATE","DEATHRATE","MARRATE"))
    ax.set_ylim(3.5, -0.5)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, corr_matrix1[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_rates.png'))


    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix2)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4), ticklabels=("Reddito lavoro", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4), ticklabels=("Reddito lavoro", "NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE"))
    ax.set_ylim(4.5, -0.5)
    for i in range(5):
        for j in range(5):
            ax.text(j, i, corr_matrix2[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_migrate.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix3)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito lavoro","GROWTHRATEN", "GROWTHRATET", "TFR"))
    ax.yaxis.set(ticks=(0, 1, 2, 3), ticklabels=("Reddito lavoro","GROWTHRATEN", "GROWTHRATET", "TFR"))
    ax.set_ylim(3.5, -0.5)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, corr_matrix3[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_growth.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix4)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito lavoro","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito lavoro","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP"))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix4[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_age.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix5)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito lavoro","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"))
    ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6), ticklabels=("Reddito lavoro","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T"))
    ax.set_ylim(6.5, -0.5)
    for i in range(7):
        for j in range(7):
            ax.text(j, i, corr_matrix5[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_lifeexp.png'))

    fig, ax = plt.subplots()
    im = ax.imshow(corr_matrix6)
    im.set_clim(-1, 1)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1, 2), ticklabels=("Reddito lavoro", "DEPENDRATE", "OLDAGEDEPR"))
    ax.yaxis.set(ticks=(0, 1, 2), ticklabels=("Reddito lavoro", "DEPENDRATE", "OLDAGEDEPR"))
    ax.set_ylim(2.5, -0.5)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, corr_matrix6[i, j], ha='center', va='center',
                    color='r')
    cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
    plt.savefig(os.path.join(correlations_datapath, 'CM_reddito_lavoro_indicatori_depend.png'))

correlation_redditi_soddisfazione()
correlation_reddito_lavoro_soddisfazione()
correlation_redditi_indicatori()
correlation_reddito_lavoro_indicatori()