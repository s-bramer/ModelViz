import pyvista as pv
from trame.app import get_server
from trame.widgets import vtk as vtk_widgets
from trame.ui import SinglePage

# PyVista Plotting
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(pv.Sphere())

# Trame server setup
server = get_server()

# Define the layout for the Trame application
def setup_ui(server):
    with SinglePage(server) as layout:
        layout.title.set("Interactive 3D Model with PyVista and Trame")
        with layout.content:
            vtk_widgets.VtkRemoteView(plotter.ren_win)

# Setup the Trame UI
setup_ui(server)

def start_trame_server():
    server.start()
