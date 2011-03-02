# 
# __init__.py
# 
# Copyright (C) 2010 Antoine Mercadal <antoine.mercadal@inframonde.eu>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import snapshoting


def make_archipel_plugin(configuration, entity, group, excluded_plugins):
    return [{"info": snapshoting.TNSnapshoting.plugin_info(),
            "plugin": snapshoting.TNSnapshoting(configuration, entity, group)}]


def version():
    import pkg_resources
    return (__name__, pkg_resources.get_distribution("archipel-agent-virtualmachine-snapshoting").version)
