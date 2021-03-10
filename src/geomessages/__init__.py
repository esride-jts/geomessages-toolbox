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

import xml.etree.ElementTree as ElementTree

class geomessage:

    def __init__(self, id, coordinates, wkid, sic):
        self._id = id
        self._coordinates = coordinates
        self._wkid = wkid
        self._sic = sic



class geomessage_reader:

    def __init__(self):
        pass

    def read_messages(self, file_path):
        geomessages = []
        geomessages_root = ElementTree.parse(file_path).getroot()
        for geomessage_element in geomessages_root.findall('geomessage'):
            id = geomessage_element.find('_id').text
            control_points = geomessage_element.find('_control_points').text
            coordinates = [float(coordinate) for coordinate in control_points.split(',')]
            wkid = int(geomessage_element.find('_wkid').text)
            sic_element = geomessage_element.find('sic')
            if not None is sic_element:
                sic = sic_element.text
                new_geomessage = geomessage(id, coordinates, wkid, sic)
                geomessages.append(new_geomessage)

        return geomessages