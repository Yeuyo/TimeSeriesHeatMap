import seaborn  as sns
import matplotlib.pyplot as plt
import pandas as pd
import glob

data = pd.read_excel("C:/Users/yeww/TFs heatmap/BRD4 Time Series/final.xls", header = None)
exlList = glob.glob("C:/Users/yeww/TFs heatmap/BRD4_RFP/*.xls")
exlFiles = [None] * len(exlList)
for n in range(len(exlList)):
    exlFiles[int(exlList[n].split('Cell')[1].split('_')[0]) - 1] = exlList[n]
cbmax = 7 #data.loc[:, 5].max()
palette = sns.color_palette("cubehelix",n_colors = cbmax) # "YlGnBu"
palette.reverse()
# palette = sns.color_palette("crest",n_colors = cbmax)
fig, axs = plt.subplots(data.loc[:, 1].max(), 13)
# fig, axs = plt.subplots(3, 13)
axcb = fig.add_axes([.91, .3, .03, .4])

# for i in range(3): #range(data.loc[:, 1].max()):
for i in range(data.loc[:, 1].max()):
    rfpData = pd.read_excel(exlFiles[i])
    smtFrames = list(range(0, len(rfpData), 3))
    tGap = 11
    cellData = data.loc[data.loc[:, 1] == i + 1,]
    for n in range(12):
        sliceData = cellData.loc[cellData.loc[:, 2] == n + 1,]
        sliceData = sliceData.pivot(index = 4, columns = 3, values = 5)
        sns.heatmap(sliceData, vmin = 0, vmax = cbmax, cmap = palette, cbar = False, ax = axs[i, n])
        axs[i, n].axis('off')
        axs[i, n].set_aspect('equal')
        if rfpData.iloc[smtFrames[((n * tGap) + 1): ((n+1) * tGap)], 1].sum() > 0:
            axs[i, n].plot([0, 10], [0, 0], color='red', lw=2,clip_on=False)
    sns.heatmap(sliceData, vmin = 0, vmax = cbmax, cmap = palette, cbar_ax = axcb, ax = axs[i, n + 1])
    axs[i, n + 1].axis('off')
    axs[i, n + 1].set_aspect('equal')
    if rfpData.iloc[smtFrames[(((n+1) * tGap) + 1): ((n+2) * tGap)], 1].sum() > 0:
        axs[i, n + 1].plot([0, 10], [0, 0], color='red', lw=2,clip_on=False)
# plt.show()
fig.tight_layout(rect = (0, 0, 0.91, 1), h_pad = 0, w_pad = 0)
fig.savefig('C:/Users/yeww/time series heat map2.svg', format='svg')
fig.show()