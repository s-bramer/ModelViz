import pyvista as pv


# Generate the 3D model with PyVista
plotter = pv.Plotter(off_screen=True)
sphere = pv.Sphere()
plotter.add_mesh(sphere, color="blue", opacity=0.7)
# plotter.export_vtksz('3d_model.vtksz')  # Export as .vtksz
# Specify the output HTML file path
html_file = "3d_model.html"

# Export the 3D scene to an HTML file
plotter.export_html(html_file)
