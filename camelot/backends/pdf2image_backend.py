# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
from pdf2image import convert_from_path

class PDF2ImageBackend(object):
    def convert(self, pdf_path, png_path):

        try:
            output_folder = os.path.dirname(png_path)
            output_file = os.path.splitext(os.path.basename(png_path))[0]
            paths = convert_from_path(pdf_path, output_folder=output_folder, output_file=output_file, dpi=300, fmt='png',
                          single_file=True, use_pdftocairo=True, paths_only=True)
        except subprocess.CalledProcessError as e:
            raise ValueError(e.output)
