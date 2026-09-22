from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget
import plotly.express as px
import pandas as pd
import sys

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.cluster import KMeans

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
kmeans = KMeans(n_clusters = 2)
kmeans.fit(multAxisData['Percentage of Time'].values.reshape(-1, 1))
kmeans2 = KMeans(n_clusters = 2)
kmeans2.fit(multAxisData['Visiting Frequency'].values.reshape(-1, 1))

g1P = multAxisData.loc[kmeans.labels_ == 0, 'Percentage of Time']
g2P = multAxisData.loc[kmeans.labels_ == 1, 'Percentage of Time']
g1V = multAxisData.loc[kmeans2.labels_ == 0, 'Visiting Frequency']
g2V = multAxisData.loc[kmeans2.labels_ == 1, 'Visiting Frequency']

multAxisData.loc[kmeans.labels_ == 0, "Group"] = "Cluster 1"
multAxisData.loc[kmeans.labels_ == 1, "Group"] = "Cluster 2"
# fig = px.scatter(multAxisData, x = 'Group', y = 'Percentage of Time')
fig = px.strip(multAxisData, x = 'Group', y = 'Percentage of Time')
fig.update_traces(marker = dict(size = 12, color = 'magenta'))

multAxisData.loc[kmeans2.labels_ == 0, "Group"] = "Cluster 1 "
multAxisData.loc[kmeans2.labels_ == 1, "Group"] = "Cluster 2 "
fig2 = px.scatter(multAxisData, x = 'Group', y = 'Visiting Frequency')
fig2 = px.strip(multAxisData, x = 'Group', y = 'Visiting Frequency')
fig2.update_traces(yaxis = 'y2', marker = dict(size = 12, color='green'))

multAxisFig = make_subplots(specs=[[{"secondary_y": True}]])
multAxisFig.add_traces(fig.data + fig2.data)
multAxisFig.update_layout(title_text = "???", title_font = dict(size = 22))

multAxisFig.update_xaxes(title_text = "Cluster", title_font = dict(size = 22, family = 'Times New Roman', color = 'black'), categoryorder = 'array', categoryarray = ['Cluster 1', 'Cluster 1 ', 'Cluster 2', 'Cluster 2'])
multAxisFig.update_yaxes(title_text = "Percentage of Time", secondary_y = False, title_font = dict(size = 22, family = 'Times New Roman', color = 'magenta'))
multAxisFig.update_yaxes(title_text = "Visiting Frequency", secondary_y = True, title_font = dict(size = 22, family = 'Times New Roman', color = 'green'))

# Background remove
# multAxisFig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
# multAxisFig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
# multAxisFig.update_xaxes(title_text = "Cluster", showline = True, linecolor = 'black', mirror = True, title_font = dict(size = 22, family = 'Times New Roman', color = 'black'), categoryorder = 'array', categoryarray = ['Cluster 1', 'Cluster 1 ', 'Cluster 2', 'Cluster 2'])
# multAxisFig.update_yaxes(title_text = "Percentage of Time", secondary_y = False, showline = True, linecolor = 'black', title_font = dict(size = 22, family = 'Times New Roman', color = 'magenta'))
# multAxisFig.update_yaxes(title_text = "Visiting Frequency", secondary_y = True, showline = True, linecolor = 'black', title_font = dict(size = 22, family = 'Times New Roman', color = 'green'))

multAxisFig.show()
1