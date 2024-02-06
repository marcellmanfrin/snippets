# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>5.

from snippet.typehints.thing import Thing


def test_thing_creation() -> None:  
    assert Thing() is not None
    
def test_empty_thing() -> None:
    assert Thing.EMPTY_THING is not None
    
def test_new_thing_diffent_from_empty_thing() -> None:
    assert Thing() != Thing.EMPTY_THING
