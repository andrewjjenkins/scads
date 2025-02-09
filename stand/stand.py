from solid import *
from solid.utils import *

b = difference()(
    cube(10),
    sphere(15),
)

if __name__ == '__main__':
    file_out = scad_render_to_file(b, 'out/stand.scad', include_orig_code=True)
    print(f"{__file__}: SCAD file written to: \n{file_out}")
