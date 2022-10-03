from supabase import create_client
import uuid
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import math
import numpy as np
from numpy.linalg import norm
from fastapi.responses import FileResponse

import cloudinary

cloudinary.config(
    cloud_name="dxbi9m7sv",
    api_key="651348724447779",
    api_secret="Z5LP84k7pwSFv1yDPf604sjyVjE"
)

import cloudinary.uploader
import cloudinary.api

API_URL = 'https://dquglwcmtervdexzzyma.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRxdWdsd2NtdGVydmRleHp6eW1hIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1NjMwMjc0MCwiZXhwIjoxOTcxODc4NzQwfQ.HnD8TCzYHQLEu3WRs-2tCH-1etD0WdO8MKkRQU77MW4'
supabase = create_client(API_URL, API_KEY)
print(supabase)


def distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2), 2)


def segmentation():
    OrderData = supabase.table('orders').select('*').execute()
    InteractionData = supabase.table('Interactions').select('*').execute()

    print(OrderData)
    print()
    print()
    print(InteractionData)

    # for each item in OrderData:
    #     print(item)
    for item in OrderData.data:
        print(item)

    # for each item in InteractionData:
    #     print(item)
    for item in InteractionData.data:
        print(item)

    OrderData = pd.DataFrame(OrderData.data)
    InteractionData = pd.DataFrame(InteractionData.data)

    print(OrderData)
    print()
    print(InteractionData)

    print("Done")

    ## Summarization of the data
    # https://www.kaggle.com/roshansharma/customer-segmentation-using-rfm-analysis
    spend = OrderData.groupby('userid')['payment'].sum()
    spend = spend.reset_index()
    spend.columns = ['userID', 'payment']
    print(spend)

    interaction = InteractionData.groupby('user')['type'].sum()
    interaction = interaction.reset_index()
    interaction.columns = ['userID', 'interactionScore']
    print("interaction")
    print(interaction)

    # merge the two dataframes by userID
    data = pd.merge(spend, interaction, on='userID', how='outer')
    print(data)

    # fill the missing values with 0
    data = data.fillna(0)
    print(data)

    # insert raws to data
    data = data.append({'userID': '1', 'payment': 100, 'interactionScore': 100}, ignore_index=True)
    data = data.append({'userID': '2', 'payment': 50.0, 'interactionScore': 51}, ignore_index=True)
    data = data.append({'userID': '3', 'payment': 31.0, 'interactionScore': 12}, ignore_index=True)
    data = data.append({'userID': '4', 'payment': 45.50, 'interactionScore': 100}, ignore_index=True)
    data = data.append({'userID': '5', 'payment': 89.0, 'interactionScore': 105}, ignore_index=True)
    data = data.append({'userID': '6', 'payment': 99.0, 'interactionScore': 30}, ignore_index=True)
    data = data.append({'userID': '7', 'payment': 2000.5, 'interactionScore': 60}, ignore_index=True)
    data = data.append({'userID': '8', 'payment': 50.0, 'interactionScore': 51}, ignore_index=True)
    data = data.append({'userID': '9', 'payment': 31.0, 'interactionScore': 12}, ignore_index=True)
    data = data.append({'userID': '10', 'payment': 45.50, 'interactionScore': 100}, ignore_index=True)

    # Now these are ready for K-Means clustering
    X = data.iloc[:, 1:4].values
    print(X[0:5])

    ################################################## 3. Identifying the number of clusters using elbow graph

    # Computing WSS scored for k values 1-10
    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    distances = []
    for i in range(1, 11):
        p1 = (1, wcss[0])
        p1 = np.asarray(p1)
        p2 = (10, wcss[9])
        p2 = np.asarray(p2)
        p3 = (i, wcss[i - 1])
        p3 = np.asarray(p3)
        d = norm(np.cross(p2 - p1, p1 - p3)) / norm(p2 - p1)
        # Or we can use below code
        # abs((x2-x1)*(y1-y0) - (x1-x0)*(y2-y1)) / np.sqrt(np.square(x2-x1) + np.square(y2-y1))
        distances.append(d)

    # Find the largest value index in the list
    index = distances.index(max(distances)) + 1
    print("index")
    print(distances)
    print(index)

    # Elbow plot
    sns.set()
    plt.plot(range(1, 11), wcss)
    plt.title("Elbow Graph")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    # Elobow plot shows that the elbow is at k=5

    # WCSS
    # https://medium.com/@ODSC/unsupervised-learning-evaluating-clusters-bd47eed175ce
    """
    Elbow method is one of the most popular methods to select the optimum value of k for the model.

    It works by calculating the Within-Cluster-Sum of Squared Errors ( WSS ) for different values of k and choose the value of k for which the WSS diminishes the most.

    Lets breakdown WSS:

    The squared error for each point is the square of the distance between the point and the predicted cluster center.
    Any distance metric such as the Euclidean distance or Hamming distance can be used.
    The WSS score is the sum of these squared errors for all data points.
    The point where there is a significant drop in WSS score is selected to be the value of k.
    """

    ################################################## 4. Applying K-Means Clustering Algorithm (Training the model)

    kmeans = KMeans(n_clusters=index, init='k-means++', random_state=7)
    Y = kmeans.fit_predict(X)
    print(Y)

    ################################################## 5. Visualizing the clusters
    # Scatter plot to visualize the different cluster in the dataset

    plt.figure(figsize=(10, 10))

    colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']

    # Run 2 line from below code
    for i in range(0, index):
        plt.scatter(X[Y == i, 0], X[Y == i, 1], s=50, c=colors[i], label='Cluster ' + str(i + 1))

    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='black', label="Centroids")

    plt.title("Customer Segmentation")
    plt.xlabel("Spending Score")
    plt.ylabel("Interaction Score")
    plt.legend()

    # plot to image
    plt.savefig('plot.png')

    # OrderData = supabase.table('orders').select('*').execute()

    file = 'plot.png'

    config = cloudinary.config(secure=True)

    cloudinary.uploader.upload('plot.png', public_id='plot-customer', overwrite=True, invalidate=True)
    srcURL = cloudinary.CloudinaryImage("plot-customer").build_url()

    print(srcURL)
    print(srcURL)
    print(srcURL)

    return srcURL

#  uvicorn main:app --reload
