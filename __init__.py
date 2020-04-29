# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Rectanglify
                                 A QGIS plugin
 Add a digitizing tool which "rectanglifies" selected features of a polygon vector layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-04-28
        copyright            : (C) 2020 by Yoann Quenach de Quivillic
        email                : yoann.quenach@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Rectanglify class from file Rectanglify.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .rectanglify import Rectanglify
    return Rectanglify(iface)
