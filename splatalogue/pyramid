#-----------------------------------------------------------------------
#  Copyright (C) 2013
#  Associated Universities, Inc. Washington DC, USA.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 3 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, see
#  <http://www.gnu.org/licenses/>. 
#
#  Correspondence should be addressed as follows:
#         Email: aremijan@nrao.edu
#         Postal address: Tony Remijan
#                         National Radio Astronomy Observatory
#                         520 Edgemont Road
#                         Charlottesville, VA 22903-2475 USA
#-----------------------------------------------------------------------

from pyramid.paster import get_app, setup_logging
import os
import site  # PPM; SWW, please sanity check these two lines
site.addsitedir('/export/home/wdgweb-alpha/wdgweb-alpha.cv.nrao.edu/active/pyramid/code-box/lib/python2.7/site-packages')

ini_path = os.path.dirname(__file__) + '/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main') 