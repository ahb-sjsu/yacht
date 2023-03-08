import plotly.figure_factory as ff
import plotly.graph_objects as go

data = (
  {"label": "Port Main", "sublabel": "count", "range": [1400, 2000, 2500],
   "performance": [1000, 1650],"point": [1200]},
  {"label": "Starboard Main", "sublabel": "count", "range": [1400, 2000, 2500],
   "performance": [1000, 1650],"point": [1225]},
  {"label": "Generator 1", "sublabel": "count", "range": [1400, 2000, 2500],
   "performance": [1200, 3000],"point": [2000]},
  {"label": "Generator 2", "sublabel": "count", "range": [1400, 2000, 2500],
   "performance": [1200, 3000],"point": [1850]}
)

fig = ff.create_bullet(
    data, titles='label', subtitles='sublabel', markers='point',
    title='Engine RPM',
    measures='performance', ranges='range', orientation='v',
)
fig.show()

fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 335,
    mode = "gauge+number+delta",
    title = {'text': "Speed"},
    delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 500], 'tickvals': [0, 25, 50, 100, 200, 300, 400, 500]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
fig2.update_layout(
    font=dict(
        family="Courier",
        size=18,
        color="black"))
fig2.show()