import plotly.offline
import plotly.graph_objs as go

fig = go.Figure(
    data=[
        go.Cone(
            x=[0],
            y=[0],
            z=[0],
            u=[0],
            v=[0],
            w=[1],
            sizeref=1,
            hoverinfo="skip",
            colorscale=[[0, "gold"], [0.5, "magenta"], [1, "magenta"]],
            showscale=False,
            lighting_ambient=0.7,
            lighting=dict(specular=1)
        ),
        go.Scatter3d(
            x=[0],
            y=[0],
            z=[1],
            hoverinfo="skip",
            opacity=0
        )
    ],
    layout=go.Layout(xaxis={"showgrid": False}, yaxis={"showgrid": False}),
)

R = 0.80
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
