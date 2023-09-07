# -*- coding: utf-8 -*-

import os

from ..utils import get_page_layout, get_text_objects


class BaseParser(object):
    """Defines a base parser."""

    def _generate_layout(self, filename, layout_kwargs, img_fmt='png'):
        self.filename = filename
        self.layout_kwargs = layout_kwargs
        self.layout = layout_kwargs['layout']
        self.dimensions = layout_kwargs['dim']
        self.images = get_text_objects(self.layout, ltype="image")
        self.horizontal_text = layout_kwargs['horizontal_text']
        self.vertical_text = layout_kwargs['vertical_text']
        self.pdf_width, self.pdf_height = self.dimensions
        self.rootname, __ = os.path.splitext(self.filename)
        self.imagename = "".join([self.rootname, "." + img_fmt])
