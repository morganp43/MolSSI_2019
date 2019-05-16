"""
This is a test for project_BondDist.py .
"""

import project_BondDist as bd
import pytest

def test_calcdist():
   coord1 = [0,0,1]
   coord2 = [0,0,0]

   observed = bd.calc_dist(coord1,coord2)

   assert observed == 1

def test_bondchk_false():
       """a test fo the bond_check function."""
       bond_len = 3.0
       observed = bd.bond_chk(bond_len)
       assert observed == 0

def test_bondchk_true():
    bond_len = 1.4
    observed = bd.bond_chk(bond_len)
    assert observed == 1

def test_bondlen_error():
    bond_len = 'a'

    with pytest.raises(TypeError):
        observed = bd.bond_chk(bond_len)
