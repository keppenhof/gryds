#! /usr/bin/env python
#
# Transformation base class


from __future__ import division, print_function, absolute_import

from .grid import Grid
from ..config import DTYPE


class Interpolator(object):
    """Base class for interpolators, that implements the minimum requirements
    for sampling on grid in new images.

    Attributes:
        self.image (np.ndarray): The wrapped ND image.
        self.grid (Grid): The image's default sampling grid.
    """

    def __init__(self, image):
        """
        Args:
            image (np.ndarray): An ND image array.
        """
        self.image = image
        self.grid = Grid(shape=self.image.shape)

    @property
    def shape(self):
        return self.image.shape

    def sample(self, points, **kwargs):
        raise NotImplementedError()

    def resample(self, points, **kwargs):
        raise NotImplementedError()

    def transform(self, *transforms, **kwargs):
        transformed_grid = self.grid.transform(*transforms)
        new_image = self.resample(transformed_grid, **kwargs)
        return new_image.astype(DTYPE)
