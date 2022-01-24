from .view3d import view3d
from .chemspace import chemspace
from .landing import landing

pages = {
    "3DView Page" : (view3d, False),
    "Chemspace" : (chemspace, False),
    "Landing" : (landing, True)
}