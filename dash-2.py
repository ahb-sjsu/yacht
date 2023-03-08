import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
                                            [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])


gauge1 = go.Indicator(
    mode = "gauge+number",
    value = 18,
    title={
        'text': "Speed (Kts)",
        'font': {'size': 32}},
    gauge = {
        'axis': {'range': [None, 25]},
        'steps': [
            {'range': [0, 20], 'color': "lightgray"},
            {'range': [20, 25], 'color': "gray"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 24}})

gauge2 = go.Indicator(
    mode = "gauge+number",
    value = 475,
    title = {'text': "Port Main Fuel"},
    gauge = {
        'axis': {'range': [None, 960]},
        'steps': [
            {'range': [0, 240], 'color': "lightgray"},
            {'range': [240, 480], 'color': "gray"},
            {'range': [480, 720], 'color': "lightgray"},
            {'range': [720, 960], 'color': "gray"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 864}})

gauge3 = go.Indicator(
    mode = "gauge+number",
    value = 123,
    title = {'text': "Day Tank Fuel"},
    gauge = {
        'axis': {'range': [None, 186]},
        'steps': [
            {'range': [0, 47], 'color': "lightgray"},
            {'range': [47, 93], 'color': "gray"},
            {'range': [93, 140], 'color': "lightgray"},
            {'range': [140, 186], 'color': "gray"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 168}})

gauge4 = go.Indicator(
    mode = "gauge+number",
    value = 440,
    title = {'text': "Starboard Main Fuel"},
    gauge = {
        'axis': {'range': [None, 960]},
        'steps': [
            {'range': [0, 240], 'color': "lightgray"},
            {'range': [240, 480], 'color': "gray"},
            {'range': [480, 720], 'color': "lightgray"},
            {'range': [720, 960], 'color': "gray"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 864}})

gauge5 = go.Indicator(
    mode = "gauge+number",
    value = 1250,
    title = {'text': "Port Main Engine RPM"},
    gauge = {'axis': {'range': [None, 1800]},
             'bar': {'color': "green"},
             'steps' : [
                 {'range': [0, 1500], 'color': 'rgb(220, 220, 220)'},
                 {'range': [1500, 1650], 'color': 'rgb(255, 165, 0)'},
                 {'range': [1650, 1800], 'color': 'rgb(180, 10, 28)'}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1250}})


gauge6 = go.Indicator(
    mode = "gauge+number",
    value = 1250,
    title = {'text': "Starboard Main Engine RPM"},
    gauge = {'axis': {'range': [None, 1800]},
             'bar': {'color': "green"},
             'steps' : [
                 {'range': [0, 1500], 'color': 'rgb(220, 220, 220)'},
                 {'range': [1500, 1650], 'color': 'rgb(255, 165, 0)'},
                 {'range': [1650, 1800], 'color': 'rgb(180, 10, 28)'}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1240}})



fig.add_trace(gauge1, row=1, col=2)
fig.add_trace(gauge2, row=2, col=1)
fig.add_trace(gauge3, row=2, col=2)
fig.add_trace(gauge4, row=2, col=3)
fig.add_trace(gauge5, row=1, col=1)
fig.add_trace(gauge6, row=1, col=3)
fig.update_layout(
    font=dict(family="Helvetica", size=18),
    title={
        'text': "M/Y Eris Dashboard",
        'font': {'size': 42},
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'middle'
    },
    width=1200,
    height=800,
    grid=dict(rows=2, columns=3, pattern='independent'),
    margin=dict(l=50, r=50, t=100, b=50),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

fig.show()
