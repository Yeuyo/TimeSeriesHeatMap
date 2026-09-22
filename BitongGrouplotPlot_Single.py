from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget
import plotly.express as px
import pandas as pd
import sys

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture

# class appWindow(QWidget):
#     def __init__(self, parent=None):
#         super(appWindow, self).__init__(parent)
#         mainLayout = QGridLayout()
#         # label = QLabel("Message.")
#         self.figure = QtWebEngineWidgets.QWebEngineView(self)
#         # mainLayout.addWidget(label, 1, 0)
#         mainLayout.addWidget(self.figure, 1, 0)
#         self.setLayout(mainLayout)

        # Plot
        # boxData = pd.read_excel("/Users/bitong/Desktop/Book3.xlsx")
        # # boxData = pd.DataFrame({"Cell": [1, 2, 3], "State": ["ON-on", "ON-off", "OFF"], "Visiting frequency to TS": [0.5, 0.5, 0.6]})
        # boxFigure = px.box(boxData, x = "State", y = "Visiting frequency", color = "Cell", points = "all", hover_name = "Cell")
        # boxFigure.show()
        # self.figure.setHtml(boxFigure.to_html(include_plotlyjs='cdn'))


# if __name__ == '__main__':
#     app = QApplication([])
#     appInterface = appWindow()
#     appInterface.show()
#     sys.exit(app.exec())

multAxisData = pd.read_excel("C:/Users/yeww/Documents/GIC-Dashboard/Grouping data.xlsx")
multAxisData.dropna(inplace = True)
# kmeans = KMeans(n_clusters = 3, tol = 0.01, algorithm = "elkan")
kmeans = DBSCAN(eps=0.005, min_samples=5)
# kmeans = GaussianMixture(n_components=3)
kmeans.fit(multAxisData['Visiting Frequency'].values.reshape(-1, 1))
# kmeans.labels_ = kmeans.predict(multAxisData['Visiting Frequency'].values.reshape(-1, 1))


g1P = multAxisData.loc[kmeans.labels_ == 0, 'Visiting Frequency']
g2P = multAxisData.loc[kmeans.labels_ == 1, 'Visiting Frequency']
g3P = multAxisData.loc[kmeans.labels_ == 2, 'Visiting Frequency']

multAxisData.loc[kmeans.labels_ == 0, "Group"] = "Cluster 1"
multAxisData.loc[kmeans.labels_ == 1, "Group"] = "Cluster 2"
multAxisData.loc[kmeans.labels_ == 2, "Group"] = "Cluster 3"
# fig = px.scatter(multAxisData, x = 'Group', y = 'Percentage of Time')
fig = px.strip(multAxisData, x = 'Group', y = 'Visiting Frequency', hover_name='Cell')
fig.update_traces(marker = dict(size = 12, color = 'magenta'))

# Background remove
# multAxisFig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
# multAxisFig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
# multAxisFig.update_xaxes(title_text = "Cluster", showline = True, linecolor = 'black', mirror = True, title_font = dict(size = 22, family = 'Times New Roman', color = 'black'), categoryorder = 'array', categoryarray = ['Cluster 1', 'Cluster 1 ', 'Cluster 2', 'Cluster 2'])
# multAxisFig.update_yaxes(title_text = "Percentage of Time", secondary_y = False, showline = True, linecolor = 'black', title_font = dict(size = 22, family = 'Times New Roman', color = 'magenta'))
# multAxisFig.update_yaxes(title_text = "Visiting Frequency", secondary_y = True, showline = True, linecolor = 'black', title_font = dict(size = 22, family = 'Times New Roman', color = 'green'))

fig.show()
1