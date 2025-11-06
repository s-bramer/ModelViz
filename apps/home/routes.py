from flask import Blueprint, Flask, render_template, jsonify, request
from apps.home import home_bp
from apps.static.assets.py.plotly_layouts import standard_layout
# from . import home_bp
import folium
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly
import json

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

    # Create a Plotly figure
    # Line 1
    line1 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['1.Naturalised'], 
                       mode='lines', name='Naturalised', line=dict(color='green'))
    # Line 2
    line2 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['2.Recent Actual'],
                       mode='lines', name='Recent Actual', line=dict(color='blue'))
    # Line 3
    line3 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['3.Fully Licensed'],
                       mode='lines', name='Fully Licensed', line=dict(color='red'))
    
    # Update plot layput with dynamic title
    updated_layout = standard_layout.to_plotly_json()
    updated_layout['title'] = {'text': f"{DEFAULT_CATCHMENT} Plot"}
    
    # df_data = pd.DataFrame([line1, line2, line3])
    fig = go.Figure(data=[line1, line2, line3], layout=updated_layout)
    
    fdc_data = fdc_data.set_index('Percentile')
    df_table = fdc_data.T[[30,50,70,95]]
    df_table.columns = ['Q30', 'Q50', 'Q70', 'Q95']
    table_html = df_table.to_html(classes="table table-striped table-bordered", index=False)
    
    plot_json = fig.to_json()

    return render_template('home/index.html', plot=plot_json, table=table_html)

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
    # fdc_data = fdc_data.set_index('Percentile')

    # Create a Plotly figure
    # Line 1
    line1 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['1.Naturalised'], 
                       mode='lines', name='Naturalised', line=dict(color='green'))
    # Line 2
    line2 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['2.Recent Actual'],
                       mode='lines', name='Recent Actual', line=dict(color='blue'))
    # Line 3
    line3 = go.Scatter(x=fdc_data['Percentile'], y=fdc_data['3.Fully Licensed'],
                       mode='lines', name='Fully Licensed', line=dict(color='red'))

    # Update plot layput with dynamic title
    updated_layout = standard_layout.to_plotly_json()
    updated_layout['title'] = {'text': f"{catchment_name} Plot"}
    
    fig = go.Figure(data=[line1, line2, line3], layout=updated_layout)
    plot_json = fig.to_json()

    return jsonify(plot_json)

@home_bp.route('/get_geojson/<filename>')
def get_geojson(filename):
    print(f"trying to get json file: {filename}")
    # Load and return the GeoJSON file as JSON
    file_path = f'apps/static/assets/geojson/{filename}.json'
    with open(file_path) as f:
        geojson_data = f.read()
    
    return geojson_data

