import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge",
    gauge = {'shape': "bullet",
             'bar': {'thickness': 0.1}},
    value = 220,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed (Kts)"})
)

fig.show()
