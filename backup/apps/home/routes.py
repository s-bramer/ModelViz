from flask import Blueprint, Flask, render_template, jsonify, request
from apps.home import home_bp
# from . import home_bp
import folium
import pandas as pd
import plotly.express as px
import plotly
import json

# home_bp = Blueprint(
#     'home_blueprint',
#     __name__,
#     url_prefix='',
#     template_folder="../templates", 
#     static_folder="../static", 
#     static_url_path='/apps/static'
# )

# home_bp = Blueprint("home", __name__, template_folder="../templates", static_folder="../static", static_url_path='/apps/static')
# Load the CSV data

def load_data():
    df_outflow_points = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\WFD surface waterbody catchments list_outflow_XY.csv")
    fl_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\FL_flows_Qs.csv")
    ra_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\RA_flows_Qs.csv")
    nat_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Nat_flows_Qs.csv")
    abs_impacts = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Abstraction_Impacts.csv")
    scenario_results = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Scenario_results.csv")
    summary_table = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Summary_table.csv")
    return df_outflow_points, fl_Qs, ra_Qs, nat_Qs, abs_impacts, scenario_results, summary_table
data = load_data()

DEFAULT_CATCHMENT = "GB104026066630"
geojson_catchments = r"C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\Catchments_WGS84.json"

@home_bp.route("/")
def index():
    
    fdc_data = pd.DataFrame()
    fdc_data['Percentile'] = data[2]['Percentile']
    fdc_data['1.Naturalised'] = data[3][DEFAULT_CATCHMENT]
    fdc_data['2.Recent Actual'] = data[2][DEFAULT_CATCHMENT]
    fdc_data['3.Fully Licensed'] = data[1][DEFAULT_CATCHMENT]
    fdc_data = fdc_data.set_index('Percentile')

    # Generate a Plotly plot for the default catchment
    fig = px.line(fdc_data, title=f'Data for {DEFAULT_CATCHMENT}')
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('home/index.html', plot=graph_json)

@home_bp.route('/get_geojson')
def get_geojson():
    # Load your GeoJSON data (from file or other sources)
    with open(geojson_catchments) as f:
        geojson_data = f.read()
    return geojson_data


@home_bp.route('/plot', methods=['POST'])
def plot():
    
    # Extract the catchment name from the request
    catchment_name = request.json.get('catchment')
    # print(f"Plotting catchment: {catchment_name}")
    
    fdc_data = pd.DataFrame()
    fdc_data['Percentile'] = data[2]['Percentile']
    fdc_data['1.Naturalised'] = data[3][catchment_name]
    fdc_data['2.Recent Actual'] = data[2][catchment_name]
    fdc_data['3.Fully Licensed'] = data[1][catchment_name]
    fdc_data = fdc_data.set_index('Percentile')

    # Create a Plotly figure
    fig = px.line(fdc_data, title=f'Data for {catchment_name}')
    
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify(graph_json)