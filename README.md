# mapArt
mapArt


## Dev Notes:
* uses https://github.com/marceloprates/prettymaps
* Install with:
```
pip install git+https://github.com/abey79/vsketch#egg=vsketch
pip install git+https://github.com/marceloprates/prettymaps.git
```

## Errors:

1.
```
Traceback (most recent call last):
  File "/Users/nicholas/Desktop/mapArt/basicMap.py", line 8, in <module>
    from prettymaps import plot
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/prettymaps/__init__.py", line 1, in <module>
    from .draw import plot
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/prettymaps/draw.py", line 22, in <module>
    import osmnx as ox
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/osmnx/__init__.py", line 3, in <module>
    from ._api import *
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/osmnx/_api.py", line 4, in <module>
    from .distance import get_nearest_edge
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/osmnx/distance.py", line 11, in <module>
    from . import utils_geo
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/osmnx/utils_geo.py", line 14, in <module>
    from . import projection
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/osmnx/projection.py", line 5, in <module>
    import geopandas as gpd
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/geopandas/__init__.py", line 1, in <module>
    from geopandas._config import options  # noqa
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/geopandas/_config.py", line 109, in <module>
    default_value=_default_use_pygeos(),
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/geopandas/_config.py", line 95, in _default_use_pygeos
    import geopandas._compat as compat
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/geopandas/_compat.py", line 217, in <module>
    import rtree  # noqa
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/rtree/__init__.py", line 9, in <module>
    from .index import Rtree, Index  # noqa
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/rtree/index.py", line 6, in <module>
    from . import core
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/rtree/core.py", line 77, in <module>
    rt.Error_GetLastErrorNum.restype = ctypes.c_int
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 387, in __getattr__
    func = self.__getitem__(name)
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 392, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: dlsym(RTLD_DEFAULT, Error_GetLastErrorNum): symbol not found
```
Fixed with `brew install spatialindex`

2. 
```

 "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/matplotlib/pyplot.py", line 2500, in <module>
    switch_backend(rcParams["backend"])
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/matplotlib/pyplot.py", line 277, in switch_backend
    class backend_mod(matplotlib.backend_bases._Backend):
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/matplotlib/pyplot.py", line 278, in backend_mod
    locals().update(vars(importlib.import_module(backend_name)))
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/matplotlib/backends/backend_tkagg.py", line 1, in <module>
    from . import _backend_tk
  File "/Users/nicholas/Desktop/mapArt/env/lib/python3.9/site-packages/matplotlib/backends/_backend_tk.py", line 7, in <module>
    import tkinter as tk
  File "/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
```

Fixed with `brew install python-tk`

