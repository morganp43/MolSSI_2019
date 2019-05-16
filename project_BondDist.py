#!/usr/bin/python3.4m

import numpy
import os
import sys

#brings up details for the help section of our script
def calc_dist(atom1, atom2):
   """
   Calculate the distance between two atoms.

   Parameters
   ----------
   atom1: list
     A list of coordinates [x, y, z]
   atom2: list
     A list of coordinates [x, y, z]

   Returns
   -------
   bond_length: float
     The distance between atoms.

   Examples
   --------
   >>> calc_dist([0,0,0,], [0,0,1])
   1.0
   """
   dist = numpy.sqrt( (atom1[0]-atom2[0])**2 + (atom1[1]-atom2[1])**2 + (atom1[2]-atom2[2])**2)
   return dist

def bond_chk(bond_len, minm=0, maxm=1.5): # the '=num' sets defaults for the values given, in case the user does not enter any
    """
    Check if atoms are actually bonded.

    Parameters
    ----------
    bond_len: float
       The distance between atoms.
    minm: float
       The minimum distance to define a bond. Default is 0.0 ang.
    maxm: float
       The maximum distanct to define a bond. Default is 1.5 ang.

    Returns
    ------
    1 if bond.
    0 if not a bond.
    """

# check that bond_len is a float. Modifying the error message
    if not isinstance(bond_len, float):
        raise TypeError(F'bond_len must be type float. {bond_len}')

    if (bond_len > minm and bond_len < maxm):
        return 1
    else:
        return 0

def open_xyz(filename):
  xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
  atoms = xyz_file[:,0]
  coords = xyz_file[:,1:].astype(numpy.float)
  return atoms, coords


if __name__ == "__main__":

#changes the error message when no file name is given in the arguments
  if len(sys.argv) < 2:
    raise IndexError('No file name given. Script requires an xyz file to be listed as an argument.')

  xyz_filename = sys.argv[1]
	#allows the user to give the file location in the command line argument
	#after 'python' in CL, all arguments are numbered starting from 0
	#argv[0] is the program
  atoms, coords = open_xyz(xyz_filename)

#  data = numpy.genfromtxt(fname=xyz_filename, dtype='unicode', skip_header=2)

#  atoms = data[:,0]
#  coords = data[:,1:].astype(numpy.float)

  print('Atom' + '\t' + 'Bond Distance (Ang)')
  for numA, atomA in enumerate(coords):
    for numB, atomB in enumerate(coords):
      if (numA < numB):
        dist_AB = calc_dist(atomA, atomB)
        if (bond_chk(dist_AB, 0, 1.5) == 1):
               # print(F'{atoms[numA]}-{atoms[numB]}: \t {dist_AB:.3f}')
           print(str(atoms[numA]) + '-' + str(atoms[numB]) + '\t' + str(dist_AB) )
