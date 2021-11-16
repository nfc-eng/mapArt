#
# # from prettymaps import *
# # from matplotlib import pyplot as plt
#
# import sys; sys.path.append('../')
#
# #import vsketch
# from prettymaps import plot
# import matplotlib.font_manager as fm
# from matplotlib import pyplot as plt
#
# # Init matplotlib figure
# fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)
#
# backup = plot(
#     # Address:
#     'Praça Ferreira do Amaral, Macau',
#     # Plot geometries in a circle of radius:
#     radius = 1100,
#     # Matplotlib axis
#     ax = ax,
#     # Which OpenStreetMap layers to plot and their parameters:
#     layers = {
#             # Perimeter (in this case, a circle)
#             'perimeter': {},
#             # Streets and their widths
#             'streets': {
#                 'width': {
#                     'motorway': 5,
#                     'trunk': 5,
#                     'primary': 4.5,
#                     'secondary': 4,
#                     'tertiary': 3.5,
#                     'residential': 3,
#                     'service': 2,
#                     'unclassified': 2,
#                     'pedestrian': 2,
#                     'footway': 1,
#                 }
#             },
#             # Other layers:
#             #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
#             'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
#             'water': {'tags': {'natural': ['water', 'bay']}},
#             'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
#             'forest': {'tags': {'landuse': 'forest'}},
#             'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
#         },
#         # drawing_kwargs:
#         #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
#         drawing_kwargs = {
#             'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
#             'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
#             'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
#             'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
#             'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
#             'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
#             'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
#             'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
#         }
# )
# backup.savefig('/prints/test.png')


import sys;

import random

sys.path.append('../')
# Prettymaps
from prettymaps import *
# Vsketch
import vsketch
# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
# Shapely
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

'''
Change everything below this to change the type of image.
'''

palette_one_turquoise = ['#15B7B9',
                         '#10DDC2',
                         '#F5F5F5'
                         ]
palette_two_brown_orange = ['#5c2626', '#ffd6b6', '#b74242']
palette_three_green = ['#018558', '#bde902', '#fef031']
palette_four_pinks = ['#fde4e3', '#f282b4', '#ef415e']
pallet_orig = ['#FFC857', '#E9724C', '#C5283D']

paletts = [pallet_orig, palette_one_turquoise, palette_two_brown_orange, palette_three_green, palette_four_pinks]

locations = [('Pripyat, Ukraine', 'pripyat_ukraine'), ('Tokyo, Japan', 'tokyo'), ('New York, Ny', 'ny'), ('Chicago, Illinois', 'chicago'),
             ('Rome, Italy', 'rome',), ('London, England', 'london')]

fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)

for index, palette in enumerate(paletts):
    for location in locations:
        layers = plot(
            location[0], radius=1500,
            ax=ax,
            layers={
                'perimeter': {},
                'streets': {
                    'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
                    'width': {
                        'motorway': 5,
                        'trunk': 5,
                        'primary': 4.5,
                        'secondary': 4,
                        'tertiary': 3.5,
                        'residential': 3,
                        'service': 2,
                        'unclassified': 2,
                        'pedestrian': 2,
                        'footway': 1,
                    }
                },
                'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
                'water': {'tags': {'natural': ['water', 'bay']}},
                'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
                'forest': {'tags': {'landuse': 'forest'}},
                'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}}
            },
            drawing_kwargs={
                'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
                'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...', 'zorder': 0},
                'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
                'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
                'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
                'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
                'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
                'building': {'palette': palette_four_pinks, 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
            },

            osm_credit={'color': '#2F3737'}
        )
        # Draw left text
        xmin, ymin, xmax, ymax = layers['perimeter'].bounds
        dx, dy = xmax - xmin, ymax - ymin
        ax.text(
            xmax - (.25 * dx), ymax - (.04 * dy),
            location[0],
            # color='#2F3737',
            alpha=1.0,
            rotation=0,
            fontsize=20,
            fontstyle='italic',
            fontweight='demibold'
            # fontproperties=fm.FontProperties(size=35),
        )
        print(f"Saving {palette} {location}")
        print(f"Location: prints/{location[1]}/{location[1]}_palette_{str(index)}.png")

        plt.savefig(f'prints/{location[1]}/{location[1]}_palette_{str(index)}.png')
