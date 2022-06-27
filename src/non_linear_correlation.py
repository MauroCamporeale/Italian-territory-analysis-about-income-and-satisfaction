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

def non_linear_correlation_indicatori(lavoro = False):

    indicatori = ["BIRTHRATE","DEATHRATE","MARRATE","NMIGRATEIN", "NMIGRATEAB", "NMIGRATEOR", "TMIGRATE","GROWTHRATEN", "GROWTHRATET", "TFR","MEANAGECH", "POP014", "POP1564", "POP65OVER", "AGEINDEX", "MEANAGEP","LIFEEXP0M", "LIFEEXP65M", "LIFEEXP0F", "LIFEEXP65F", "LIFEEXP0T", "LIFEEXP65T","DEPENDRATE", "OLDAGEDEPR"]
    linear_r2 = []
    curve_r2 = []

    if lavoro:
        x = redditi_indicatori[["Reddito medio lavoro"]].to_numpy()
    else:
        x = redditi_indicatori[["Reddito medio"]].to_numpy()

    for indicatore in indicatori:

        y = redditi_indicatori[[indicatore]].to_numpy()

        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly_features = poly.fit_transform(x)

        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, y)

        xx = x.flatten()
        yy = y.flatten()

        coeff = np.polyfit(xx, yy, 1)
        if lavoro:
            poliy = np.polyval(coeff, np.linspace(10000, 75000, 4000))
            linex = np.linspace(10000, 75000, 4000).reshape(-1, 1)
        else:
            poliy = np.polyval(coeff, np.linspace(13000, 29000, 1000))
            linex = np.linspace(13000, 29000, 1000).reshape(-1, 1)
        liney = poly_reg_model.predict(poly.fit_transform(linex.reshape(-1, 1)))

        error = r2_score(y, poly_reg_model.predict(poly_features)).round(decimals=2)
        error2 = r2_score(y, np.polyval(coeff, x)).round(decimals=2)

        curve_r2.append(error)
        linear_r2.append(error2)


        # slope, intercept, r, p, stderr, stderr2 = st.linregress(x, y)
        # line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')
        ax.plot(linex, liney, color='green')
        ax.plot(linex, poliy, color='red')
        title = "R2 curve = " + str(error) + " | R2 line = " + str(error2)
        fig.suptitle(title)
        # ax.plot(x, intercept + slope * x, label=line)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend(facecolor='white')
        if lavoro:
            plt.savefig(os.path.join(correlations_datapath, 'reddito_lavoro_indicatori_'+indicatore+'.png'))
        else:
            plt.savefig(os.path.join(correlations_datapath, 'reddito_indicatori_'+indicatore+'.png'))



    correlations_indicatori = {'Indicatori':indicatori, 'Curve_r2':curve_r2, 'Line_r2':linear_r2}
    df = pd.DataFrame.from_dict(correlations_indicatori)
    df.sort_values(by=['Curve_r2'], ascending=False, inplace=True)
    if lavoro:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_lavoro_indicatori_curve.csv'))
    else:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_indicatori_curve.csv'))

    df.sort_values(by=['Line_r2'], ascending=False, inplace=True)
    if lavoro:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_lavoro_indicatori_line.csv'))
    else:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_indicatori_line.csv'))


def non_linear_correlation_soddisfazione(lavoro = False):

    soddisfazioni = ["Soddisfazione economica","Soddisfazione salute","Soddisfazione famiglia","Soddisfazione amici","Soddisfazione tempo","Soddisfazione media"]
    linear_r2 = []
    curve_r2 = []

    if lavoro:
        x = redditi_soddisfazione[["Reddito medio lavoro"]].to_numpy()
    else:
        x = redditi_soddisfazione[["Reddito medio"]].to_numpy()

    for soddisfazione in soddisfazioni:

        y = redditi_soddisfazione[[soddisfazione]].to_numpy()

        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly_features = poly.fit_transform(x)

        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, y)

        xx = x.flatten()
        yy = y.flatten()

        coeff = np.polyfit(xx, yy, 1)
        if lavoro:
            poliy = np.polyval(coeff, np.linspace(10000, 75000, 4000))
            linex = np.linspace(10000, 75000, 4000).reshape(-1, 1)
        else:
            poliy = np.polyval(coeff, np.linspace(13000, 29000, 1000))
            linex = np.linspace(13000, 29000, 1000).reshape(-1, 1)

        liney = poly_reg_model.predict(poly.fit_transform(linex.reshape(-1, 1)))

        error = r2_score(y, poly_reg_model.predict(poly_features)).round(decimals=2)
        error2 = r2_score(y, np.polyval(coeff, x)).round(decimals=2)

        curve_r2.append(error)
        linear_r2.append(error2)


        # slope, intercept, r, p, stderr, stderr2 = st.linregress(x, y)
        # line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')
        ax.plot(linex, liney, color='green')
        ax.plot(linex, poliy, color='red')
        title = "R2 curve = " + str(error) + " | R2 line = " + str(error2)
        fig.suptitle(title)
        # ax.plot(x, intercept + slope * x, label=line)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend(facecolor='white')
        if lavoro:
            plt.savefig(os.path.join(correlations_datapath, 'reddito_lavoro_soddisfazioni_'+soddisfazione+'.png'))
        else:
            plt.savefig(os.path.join(correlations_datapath, 'reddito_soddisfazioni_'+soddisfazione+'.png'))



    correlations_indicatori = {'Indicatori':soddisfazioni, 'Curve_r2':curve_r2, 'Line_r2':linear_r2}
    df = pd.DataFrame.from_dict(correlations_indicatori)
    df.sort_values(by=['Curve_r2'], ascending=False, inplace=True)
    if lavoro:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_lavoro_soddisfazioni_curve.csv'))
    else:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_soddisfazioni_curve.csv'))
    df.sort_values(by=['Line_r2'], ascending=False, inplace=True)
    if lavoro:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_lavoro_soddisfazioni_line.csv'))
    else:
        df.to_csv(os.path.join(correlations_datapath, 'correlazione_soddisfazioni_line.csv'))


non_linear_correlation_indicatori()
non_linear_correlation_soddisfazione()
non_linear_correlation_indicatori(lavoro=True)
non_linear_correlation_soddisfazione(lavoro=True)