
import json
import pyvista as pv
import pandas as pd
import numpy as np

model_vertices = pd.read_csv("apps/model_vertices.csv").values
with open('apps/model_dimensions.json', 'r') as file:
    dimensions = json.load(file)    
vertices = np.array(model_vertices)
print(vertices.shape)
# z_exaggeration = 20
# vertices[:, 2] *= z_exaggeration
# # Create a PyVista structured grid
# nx, ny, nz = 85, 117, 5

# structured_grid = pv.StructuredGrid()

# # Assign points and dimensions to the grid
# structured_grid.points = vertices.reshape((nx + 1, ny + 1, nz + 1, 3))  # +1 because grid points are at the corners
# structured_grid.dimensions = (nx + 1, ny + 1, nz + 1)  # Dimensions of the grid (points, not cells)

# ugrid = structured_grid.extract_surface().triangulate().extract_cells(range(structured_grid.n_cells))

# structured_grid.points = vertices
# structured_grid.dimensions = [nz, ny, nx]
    
# plotter = pv.Plotter()

# # Add cells to the plotter
# for i in range(nz):  # Loop through layers
#     layer_cells = ugrid.extract_cells(range(i * nx * ny, (i + 1) * nx * ny))
#     color = pv.get_cmap('viridis')(i / nz)
#     plotter.add_mesh(layer_cells, color=color, show_edges=False, opacity=0.5)
    
# # plotter.add_mesh(structured_grid, scalars='geology', cmap='viridis')
# plotter.add_mesh(structured_grid.outline(), color="black", line_width=1)
# plotter.show_axes()
# # plotter.camera_position = 'iso'
# # plotter.add_mesh_slice_spline(
# # structured_grid,
# # generate_triangles=False,
# # n_handles=5,
# # resolution=25,
# # widget_color=None,
# # show_ribbon=False,
# # ribbon_color='pink',
# # ribbon_opacity=0.5,
# # initial_points=None,
# # closed=False,
# # interaction_event=45)

# plotter.export_html("apps/static/assets/html/3d_model.html")
