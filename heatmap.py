import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

path = "labels_pose_30Hz_20200602_1319_VGlut-cre C146 M0_2DLC_resnet50_EnclosedBehaviorMay27shuffle1_307000.csv"

data_df = pd.read_csv(path, skiprows = 3, names=['randomNos', 'B-SOiD label', 'frameNo', 'snoutX', 'snoutY', 'snoutLike',
                                                'LeftEarX', 'LeftEarY', 'LeftEarlikelihood', 'rightearx', 'righteary',
                                                'rightearlikelihood', 'leftforepawx', 'leftforepawy',
                                                'leftforewlikelihood', 'rightforepawx', 'rightforepawy',
                                                'rightforepawlikelihood', 'lefthindpawx', 'lefthindpawy',
                                                'lefthindpawlikelihood', 'righthindpawx', 'righthindpawy',
                                                'righthindpawlikelihood', 'tailbasex', 'tailbasey', 'taillikelihood'])

importantThings = pd.DataFrame(data=data_df[['frameNo', 'B-SOiD label']])
importantThings['5s'] = 5

# importantFrame = importantThings['frameNo'].to_numpy()
# importantLabel = importantThings['B-SOiD label'].to_numpy()

label = pd.Series(importantThings['B-SOiD label'])
frame = pd.Series(importantThings['frameNo'])
fives = pd.Series(importantThings['5s'])
# # fig = go.Figure(data=go.Heatmap(z=importantFrame, x=importantLabel, y=["idk"], colorscale='Viridis', hoverongaps=False))
# fig = go.Figure(data=go.Heatmap(z=[1, 40, 13, 2]))
#
# fig.update_layout(title='Frequency of Behavior')
#
#
# fig.show()
anotherArr = label[9000:10000]
framArr = frame[1:1000]
fivesArr = fives[9000:10000]



fig = px.imshow([anotherArr])

fig.show()
# print(importantThings)