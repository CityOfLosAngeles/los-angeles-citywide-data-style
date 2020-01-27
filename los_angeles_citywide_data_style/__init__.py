import os

import matplotlib.cm
import matplotlib.style

from .cmap import cmaps
from ._version import __version__

# Register custom color maps.
for cmap in cmaps:
    matplotlib.cm.register_cmap(cmap=cmap)

# Use the style sheet distributed with the package.
matplotlib.style.use(os.path.join(os.path.dirname(__file__), "citywide.mplstyle"))

__all__ = ["__version__", "cmaps"]
