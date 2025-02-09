from solid import *
from solid.utils import *

b = difference()(
    cube(10),
    sphere(15),
)

scad_render_to_file(b, 'stand.scad')
