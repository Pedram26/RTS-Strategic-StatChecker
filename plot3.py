import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='pedrampd', api_key='hqjn455dw8')
import csv

player = []
total =[]
region = []
role = []
x1 = ['','','','','']
x2 = x1[:]


with open('player_dict3.csv', 'rU') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        player.append(row[1])
        total.append(row[9])
        region.append(row[3])
        role.append(row[2])



        if row[0] == 'TSM':
            if row[2] == 'TOP':
                if not x1[0]:
                    x1[0] = {row[1]: row[9]}
                else:
                    x1[0] = {row[1]: int(row[9]) + int(x1[0][row[1]])}
            if row[2] == 'JNG':
                if not x1[1]:
                    x1[1] = {row[1]: row[9]}
                else:
                    x1[1] = {row[1]: int(row[9]) + int(x1[1][row[1]])}
            if row[2] == 'MID':
                if not x1[2]:
                    x1[2] = {row[1]: row[9]}
                else:
                    x1[2] = {row[1]: int(row[9]) + int(x1[2][row[1]])}
            if row[2] == 'ADC':
                if not x1[3]:
                    x1[3] = {row[1]: row[9]}
                else:
                    x1[3] = {row[1]: int(row[9]) + int(x1[3][row[1]])}
            if row[2] == 'SUP':
                if not x1[4]:
                    x1[4] = {row[1]: row[9]}
                else:
                    x1[4] = {row[1]: int(row[9]) + int(x1[4][row[1]])}
        elif row[0] == 'C9':
            if row[2] == 'TOP':
                if not x2[0]:
                    x2[0] = {row[1]: row[9]}
                else:
                    x2[0] = {row[1]: int(row[9]) + int(x2[0][row[1]])}
            if row[2] == 'JNG':
                if not x2[1]:
                    x2[1] = {row[1]: row[9]}
                else:
                    x2[1] = {row[1]: int(row[9]) + int(x2[1][row[1]])}
            if row[2] == 'MID':
                if not x2[2]:
                    x2[2] = {row[1]: row[9]}
                else:
                    x2[2] = {row[1]: int(row[9]) + int(x2[2][row[1]])}
            if row[2] == 'ADC':
                if not x2[3]:
                    x2[3] = {row[1]: row[9]}
                else:
                    x2[3] = {row[1]: int(row[9]) + int(x2[3][row[1]])}
            if row[2] == 'SUP':
                if not x2[4]:
                    x2[4] = {row[1]: row[9]}
                else:
                    x2[4] = {row[1]: int(row[9]) + int(x2[4][row[1]])}


trace1 = go.Bar(
    x = ["Top", 'Jungle', 'Mid', 'ADC', 'Support'],
    y=[list(x1[i].values()) for i in range(len(x1))],
    text=[list(x1[i].keys()) for i in range(len(x1))],
    marker=dict(
        color='rgb(169,169,169)',
        line=dict(
            color='rgb(169,169,169)',
            width=1.5,
        )
    ),
    name='TSM'
)
trace2 = go.Bar(
    x = ["Top", 'Jungle', 'Mid', 'ADC', 'Support'],
    y=[list(x2[i].values()) for i in range(len(x2))],
    text=[list(x2[i].keys()) for i in range(len(x2))],
    marker=dict(
        color='rgb(29,173,234)',
        line=dict(
            color='rgb(29,173,234)',
            width=1.5,
        )
    ),
    name='C9'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='grouped-bar')
