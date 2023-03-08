"""
Written by Andrew Bond

Python Developer | Network Designer | Superyacht Builder (M/Y Eris)

# Copyright (c) 2023, ANDREW BOND. All rights reserved.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

LinkedIn: https://www.linkedin.com/in/ahbond/
SJSU: https://www.sjsu.edu/people/andrew.bond/
Email: abptlm@gmail.com
"""

import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=3, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
                                            [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
                                            [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])

gauge1 = go.Indicator(
    mode = "gauge+number",
    value = 18,
    title={
        'text': "Speed (Kts)",
        'font': {'size': 24}},
    gauge = {
        'axis': {'range': [None, 25]},
        'steps': [
            {'range': [0, 20], 'color': "lightblue"},
            {'range': [20, 25], 'color': "blue"}],
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
            {'range': [0, 240], 'color': "lightyellow"},
            {'range': [240, 480], 'color': "yellow"},
            {'range': [480, 720], 'color': "lightyellow"},
            {'range': [720, 960], 'color': "yellow"}],
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
            {'range': [0, 47], 'color': "lightyellow"},
            {'range': [47, 93], 'color': "yellow"},
            {'range': [93, 140], 'color': "lightyellow"},
            {'range': [140, 186], 'color': "yellow"}],
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
            {'range': [0, 240], 'color': "lightyellow"},
            {'range': [240, 480], 'color': "yellow"},
            {'range': [480, 720], 'color': "lightyellow"},
            {'range': [720, 960], 'color': "yellow"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 864}})

gauge5 = go.Indicator(
    mode = "gauge+number",
    value = 1250,
    title = {'text': "Port Main RPM"},
    gauge = {'axis': {'range': [None, 1800]},
             'bar': {'color': "green"},
             'steps' : [
                 {'range': [0, 1500], 'color': 'rgb(220, 220, 220)'},
                 {'range': [1500, 1650], 'color': 'rgb(255, 165, 0)'},
                 {'range': [1650, 1800], 'color': 'rgb(180, 10, 28)'}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1600}})


gauge6 = go.Indicator(
    mode = "gauge+number",
    value = 1250,
    title = {'text': "Starboard Main RPM"},
    gauge = {'axis': {'range': [None, 1800]},
             'bar': {'color': "green"},
             'steps' : [
                 {'range': [0, 1500], 'color': 'rgb(220, 220, 220)'},
                 {'range': [1500, 1650], 'color': 'rgb(255, 165, 0)'},
                 {'range': [1650, 1800], 'color': 'rgb(180, 10, 28)'}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1600}})

gauge7 = go.Indicator(
    mode = "gauge+number",
    value = 2330,
    title = {"text": "Generator 1 RPM"},
    gauge = {
        "axis": {"range": [0, 3000]},
        "bar": {"color": "green"},
        "steps": [
            {'range': [0, 2500], 'color': 'rgb(220, 220, 220)'},
            {'range': [2500, 2750], 'color': 'rgb(255, 165, 0)'},
            {'range': [2750, 3000], 'color': 'rgb(180, 10, 28)'}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 2700}}
)

gauge8 = go.Indicator(
    mode = "gauge+number",
    value = 2250,
    title = {"text": "Generator 2 RPM"},
    gauge = {
        "axis": {"range": [0, 3000]},
        "bar": {"color": "green"},
        'steps': [
            {'range': [0, 2500], 'color': 'rgb(220, 220, 220)'},
            {'range': [2500, 2750], 'color': 'rgb(255, 165, 0)'},
            {'range': [2750, 3000], 'color': 'rgb(180, 10, 28)'}],
        'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 2700}
    }
)

fig.add_trace(gauge1, row=1, col=2)
fig.add_trace(gauge2, row=2, col=1)
fig.add_trace(gauge3, row=2, col=2)
fig.add_trace(gauge4, row=2, col=3)
fig.add_trace(gauge5, row=1, col=1)
fig.add_trace(gauge6, row=1, col=3)
fig.add_trace(gauge7, row=3, col=1)
fig.add_trace(gauge8, row=3, col=3)

fig.update_layout(
    font=dict(family="Helvetica", size=12),
    title={
        'text': "M/Y Eris Dashboard",
        'font': {'size': 42},
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'middle'
    },
    width=600,
    height=600,
    grid=dict(rows=2, columns=3, pattern='independent'),
    margin=dict(l=50, r=50, t=100, b=50),
    paper_bgcolor='white',
    plot_bgcolor='white',
)

fig.show()
