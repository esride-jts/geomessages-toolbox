#   This file is part of the GEOINT Python tools.
#   Copyright (C) 2021 Esri Deutschland GmbH
#   Contact: Jan Tschada (j.tschada@esri.de)
#   
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#   
#   You should have received a copy of the GNU Lesser General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import geomessages
import os
import unittest

class TestImportGeomessageFile(unittest.TestCase):

    def setUp(self):
        self._reader = geomessages.geomessage_reader()

    def test_import_large_file(self):
        file_path = os.environ['geomessages.filepath']
        geomessages = self._reader.read_messages(file_path)
        self.assertTrue(0 < len(geomessages), 'At least one geomessage should be read!')



if __name__ == '__main__':
    unittest.main()
