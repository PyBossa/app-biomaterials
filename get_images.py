# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

from PIL import Image
import math
import os


def cut_photo(photo, slice_size=300, outdir="/tmp/"):
    # See http://stackoverflow.com/a/14252471
    out_name = "chunk"
    img = Image.open(photo)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(width / slice_size))
    count = 1
    for x in range(0, width, slice_size):
        for y in range(0, height, slice_size):
            bbox = (y, x, y + slice_size, x + slice_size)
            working_slice = img.crop(bbox)
            #save the slice
            working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(count) + ".tif"))
            count += 1
