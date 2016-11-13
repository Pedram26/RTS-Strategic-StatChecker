import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
tls.set_credentials_file(username='pedrampd', api_key='hqjn455dw8')
import csv

player =[]
profile2 = []
total = []
total2 =[]
region = []

with open('player_dict.csv', 'rU') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        player.append(row[1])
        total.append(row[8])
        region.append(row[2])

#Returns the indices of the duplicate items in the list
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

#Adds the duplicate item to profile2
s=set(player)
for x in player:
    if x in s:
        s.remove(x)
    else:
        profile2.append(x)

indices = list_duplicates_of(player, profile2[0])
total2 = min(int(total[indices[0]]), int(total[indices[1]]))
total2_index = total.index(str(total2))

trace1 = go.Bar(
    x=player,
    y=total,
    text = region,
    name='Profile 1'
)

trace2 = go.Bar(
    x= profile2,
    y= total2,
    text = region[total2_index],
    name='Profile 2'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')
