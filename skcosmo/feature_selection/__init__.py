"""
The :mod:`sklearn.feature_selection` module includes FPS and CUR selection, each
with the optional PCov-flavor
"""

from ..selection.FPS import FeatureFPS
from ..selection.CUR import FeatureCUR
from .simple_fps import FPS
from .simple_cur import CUR
from .meta_selectors import BlockSelector, RollingSelector


__all__ = ["FeatureFPS", "FeatureCUR", "FPS", "CUR", "BlockSelector", "RollingSelector"]
