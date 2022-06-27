import pandas as pd
import os
from sklearn.cluster import KMeans, SpectralClustering
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm
import numpy as np
import geopandas as gpd



datapath = "../datasources"
cleaned_datapath = os.path.join(datapath, "cleaned")
integrated_datapath = os.path.join(datapath, "integrated")
constructed_datapath = os.path.join(datapath, "constructed")

clustering_datapath = "../results/clustering"
sf_path = "../maps/source/gadm40_ITA_1.shx"

sf = gpd.read_file(sf_path)


if not os.path.exists(clustering_datapath):
    os.mkdir(clustering_datapath)

redditi_soddisfazione = pd.read_csv(os.path.join(constructed_datapath, "Redditi_e_soddisfazione_per_regione_2020.csv"))
redditi_indicatori = pd.read_csv(os.path.join(constructed_datapath, "Redditi_e_indicatori_per_provincia_2020.csv"))
regions = pd.read_csv("../maps/source/nomi_regioni.csv")


X = redditi_soddisfazione[["Reddito medio","Soddisfazione media"]].to_numpy()
scaler = MinMaxScaler((0,10))


regioni = redditi_soddisfazione[["Regione"]].to_numpy()
redditi_soddisfazione['Regione'] = redditi_soddisfazione['Regione'].map(lambda s: s.split('(')[0])



range_n_clusters = [2, 3, 4, 5]

for n_clusters in range_n_clusters:
    # Create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)


    ax1.set_xlim([-0.5, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    X = scaler.fit_transform(X)

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10, n_init=30)
    # clusterer = SpectralClustering(n_clusters=n_clusters, random_state=10, n_init=30)
    cluster_labels = clusterer.fit_predict(X)
    redditi_soddisfazione["cluster"] = clusterer.labels_

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(
        "For n_clusters =",
        n_clusters,
        "The average silhouette_score is :",
        silhouette_avg,
    )

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10

    X = scaler.inverse_transform(X)


    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax1.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    # The vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])




    # 2nd Plot showing the actual clusters formed
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )
    for i, txt in enumerate(regioni):
        ax2.annotate(txt, (X[i, 0], X[i, 1]))

    # Labeling the clusters
    centers = clusterer.cluster_centers_
    centers = scaler.inverse_transform(centers)
    # Draw white circles at cluster centers
    ax2.scatter(
        centers[:, 0],
        centers[:, 1],
        marker="o",
        c="white",
        alpha=1,
        s=200,
        edgecolor="k",
    )

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")

    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")

    plt.suptitle(
        "Silhouette analysis for KMeans clustering on sample data with n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

    plt.savefig(os.path.join(clustering_datapath, 'soddisfazione_' + str(n_clusters) + '.png'))

    #3rd plot


    clusters=[]

    for index, row in regions.iterrows():
        df = redditi_soddisfazione[redditi_soddisfazione['Regione'] == row["Regioni"]]
        df = df.drop_duplicates()
        clusters.append(df["cluster"].iloc[0])

    sf["cluster"] = clusters

    sf.plot(column='cluster', k=n_clusters)

    plt.savefig(os.path.join(clustering_datapath, 'mappa_soddisfazione_' + str(n_clusters) + '.png'))

