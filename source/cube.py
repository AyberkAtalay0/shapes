import plotly.offline
import plotly.graph_objs as go
import numpy as np

fig = go.Figure(data=[
        go.Mesh3d(
            x=[0, 0, 1, 1, 0, 0, 1, 1],
            y=[0, 1, 1, 0, 0, 1, 1, 0],
            z=[0, 0, 0, 0, 1, 1, 1, 1],
            colorscale=[[0, "magenta"], [1, "fuchsia"]],
            intensity = np.linspace(0, 1, 8, endpoint=True),
            intensitymode="cell",
            showscale=False,
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            hoverinfo="skip",
            lighting_ambient=1,
        ),
        go.Scatter3d(
            x=[0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            y=[0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            z=[0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            mode="lines",
            line=dict(color="black", width=3),
            hoverinfo="skip",
        ),
    ],
)

R = 1.5
fig.update_layout(scene=dict(domain_x=[0, 0], camera_eye=dict(x=-0.76*R, y=1.8*R, z=0.92*R)), showlegend=False, margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor="#EBF2F7", paper_bgcolor="#EBF2F7")
fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)

plotly.offline.plot(fig, config={"displayModeBar": False, "responsive": True})

with open("temp-plot.html", "r", encoding="utf-8") as fr: readed = fr.read()
with open("temp-plot.html", "w", encoding="utf-8") as fw: 
    raw = readed.split('class="plotly-graph-div" style="')
    raw[0] = raw[0].replace('<body>', '<body style="background-color: #EBF2F7;">')
    raw[1] = raw[1].split('"', maxsplit=1)
    raw[1][0] = "margin: auto; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); height: calc(min(100vh, 100vw) - 16px); width: calc(min(100vh, 100vw) - 16px);"
    fw.write(raw[0] + 'class="plotly-graph-div" style="' + raw[1][0] + '"' + raw[1][1])
