from flask import Flask, render_template
import folium
import plotly.express as px
import plotly.utils as pu
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Folium map centered at a specific location
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # London coordinates
    
    # Save the map as an HTML string
    folium_map = m._repr_html_()

    # Create a Plotly time-series plot
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="gdpPercap", title='GDP per Capita over Time')
    
    # Convert Plotly figure to JSON for rendering
    plotly_json = json.dumps(fig, cls=pu.PlotlyJSONEncoder)
    
    return render_template('index.html', folium_map=folium_map, plotly_json=plotly_json, title="Dashyboard")

if __name__ == '__main__':
    app.run(debug=True)
