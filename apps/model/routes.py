import json
import pyvista as pv
import pandas as pd
from flask import render_template
from . import model_bp

@model_bp.route('/model')
def model():
    # vertices = pd.read_csv("apps/model/input/model_vertices.csv").values
    # with open('apps/model/input/model_dimensions.json', 'r') as file:
    #     dimensions = json.load(file)
    # # Create a PyVista structured grid
    # nx, ny, nz = 85, 117, 5
    # structured_grid = pv.StructuredGrid()
    # structured_grid.points = vertices
    # structured_grid.dimensions = [nz, ny, nx]
        
    # plotter = pv.Plotter(off_screen=True)
    # # plotter.add_mesh(structured_grid, scalars='geology', cmap='viridis')
    # plotter.add_mesh(structured_grid, cmap='viridis')
    # plotter.add_axes()
    # plotter.export_html("static/3dmodel.html")
    
    return render_template('home/model.html')