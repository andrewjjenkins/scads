from solid import *
from solid.utils import *

boxes = import_scad("mcad/boxes.scad")

base = color([1, 1, 0], 0.3)(boxes.roundedCube([90, 130, 15], 3, False, True))

rise = translate([-16.9, 0, 39])(
    rotate([0, -60, 0])(boxes.roundedCube([90, 130, 15], 3, False, True))
)

screen = translate([-25.5, 0, 48])(
    rotate([0, -60, 0])(
        color([0, 0, 1])(boxes.roundedCube([68, 108, 12], 2, True, True))
    )
)


rise_notched = rise - screen

stand = union()(
    base,
    rise_notched,
)

if __name__ == "__main__":
    file_out = scad_render_to_file(stand, "out/stand.scad", include_orig_code=True)
    print(f"{__file__}: SCAD file written to: \n{file_out}")
