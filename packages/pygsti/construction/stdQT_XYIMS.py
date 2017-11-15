from __future__ import division, print_function, absolute_import, unicode_literals
#*****************************************************************
#    pyGSTi 0.9:  Copyright 2015 Sandia Corporation
#    This Software is released under the GPL license detailed
#    in the file "license.txt" in the top-level pyGSTi directory
#*****************************************************************
"""
Variables for working with the a qutrit gate set containing Idle, X(pi/2) and Y(pi/2) and Molmer-Sorenson gates.
"""

from . import gatestringconstruction as _strc
from . import gatesetconstruction as _setc
from . import qutrit as _qutrit
from collections import OrderedDict as _OrderedDict
from numpy import pi as _pi

description = "Idle, symmetric X(pi/2), symmetric Y(pi/2), and Molmer-Sorenson gates"

gates = ['Gi','Gx','Gy','Gm']
prepStrs = _strc.gatestring_list([
    (), ('Gx',), ('Gy',), ('Gm',),
    ('Gx','Gx'), ('Gm','Gx'), ('Gm','Gy'),
    ('Gy','Gy','Gy'),('Gx','Gx','Gx') ])

effectStrs = _strc.gatestring_list([
    (),('Gy',),('Gx',), ('Gm',),
    ('Gx','Gx'),('Gy','Gm'),('Gx','Gm') ])

germs = _strc.gatestring_list([
    ('Gi',),
    ('Gx',),
    ('Gy',),
    ('Gm',),
    ('Gx', 'Gy'),
    ('Gx', 'Gm'),
    ('Gx', 'Gy', 'Gi'),
    ('Gx', 'Gi', 'Gy'),
    ('Gx', 'Gi', 'Gi'),
    ('Gy', 'Gi', 'Gi'),
    ('Gx', 'Gy', 'Gm'),
    ('Gx', 'Gm', 'Gy'),
    ('Gi', 'Gx', 'Gm'),
    ('Gy', 'Gm', 'Gm'),
    ('Gx', 'Gy', 'Gy'),
    ('Gi', 'Gm', 'Gx'),
    ('Gx', 'Gx', 'Gi', 'Gy'),
    ('Gx', 'Gy', 'Gy', 'Gi'),
    ('Gy', 'Gm', 'Gm', 'Gm'),
    ('Gy', 'Gy', 'Gm', 'Gm'),
    ('Gx', 'Gm', 'Gy', 'Gx'),
    ('Gx', 'Gm', 'Gm', 'Gm'),
    ('Gx', 'Gi', 'Gy', 'Gy'),
    ('Gy', 'Gx', 'Gy', 'Gi'),
    ('Gx', 'Gy', 'Gm', 'Gy'),
    ('Gm', 'Gm', 'Gi', 'Gi'),
    ('Gy', 'Gx', 'Gy', 'Gm'),
    ('Gi', 'Gx', 'Gm', 'Gx'),
    ('Gx', 'Gx', 'Gy', 'Gx'),
    ('Gx', 'Gi', 'Gm', 'Gi'),
    ('Gm', 'Gy', 'Gm', 'Gx'),
    ('Gx', 'Gx', 'Gy', 'Gy'),
    ('Gm', 'Gy', 'Gm', 'Gi'),
    ('Gi', 'Gx', 'Gy', 'Gm'),
    ('Gm', 'Gi', 'Gx', 'Gi'),
    ('Gy', 'Gy', 'Gy', 'Gy'),
    ('Gi', 'Gy', 'Gy', 'Gm'),
    ('Gy', 'Gy', 'Gx', 'Gx', 'Gy'),
    ('Gm', 'Gi', 'Gm', 'Gy', 'Gi'),
    ('Gy', 'Gi', 'Gi', 'Gy', 'Gx'),
    ('Gx', 'Gy', 'Gm', 'Gy', 'Gy'),
    ('Gx', 'Gi', 'Gm', 'Gi', 'Gy'),
    ('Gy', 'Gm', 'Gx', 'Gy', 'Gy'),
    ('Gx', 'Gy', 'Gy', 'Gy', 'Gy'),
    ('Gm', 'Gy', 'Gm', 'Gm', 'Gy'),
    ('Gx', 'Gy', 'Gm', 'Gx', 'Gi'),
    ('Gx', 'Gx', 'Gy', 'Gm', 'Gy'),
    ('Gm', 'Gx', 'Gi', 'Gx', 'Gx'),
    ('Gy', 'Gi', 'Gm', 'Gx', 'Gi'),
    ('Gy', 'Gy', 'Gx', 'Gm', 'Gx'),
    ('Gm', 'Gx', 'Gi', 'Gy', 'Gx'),
    ('Gx', 'Gx', 'Gy', 'Gx', 'Gy', 'Gy'),
    ('Gx', 'Gi', 'Gi', 'Gy', 'Gy', 'Gy'),
    ('Gm', 'Gm', 'Gi', 'Gi', 'Gy', 'Gi'),
    ('Gy', 'Gx', 'Gx', 'Gy', 'Gx', 'Gm'),
    ('Gi', 'Gm', 'Gx', 'Gy', 'Gm', 'Gy'),
    ('Gm', 'Gy', 'Gi', 'Gx', 'Gy', 'Gi'),
    ('Gi', 'Gx', 'Gx', 'Gi', 'Gy', 'Gy'),
    ('Gy', 'Gi', 'Gx', 'Gx', 'Gy', 'Gm'),
    ('Gm', 'Gx', 'Gy', 'Gx', 'Gx', 'Gx'),
    ('Gi', 'Gy', 'Gx', 'Gx', 'Gy', 'Gy'),
    ('Gm', 'Gy', 'Gx', 'Gm', 'Gm', 'Gy') ])


germs_lite = _strc.gatestring_list([
    ('Gi',),
    ('Gy',),
    ('Gx',),
    ('Gm',),
    ('Gi', 'Gy'),
    ('Gi', 'Gx'),
    ('Gi', 'Gm'),
    ('Gy', 'Gx'),
    ('Gy', 'Gm'),
    ('Gx', 'Gm'),
    ('Gi', 'Gi', 'Gy'),
    ('Gi', 'Gi', 'Gx'),
    ('Gi', 'Gi', 'Gm'),
    ('Gi', 'Gy', 'Gy'),
    ('Gi', 'Gy', 'Gx'),
    ('Gi', 'Gy', 'Gm'),
    ('Gi', 'Gx', 'Gy'),
    ('Gi', 'Gx', 'Gx'),
    ('Gi', 'Gx', 'Gm'),
    ('Gi', 'Gm', 'Gy'),
    ('Gi', 'Gm', 'Gx'),
    ('Gi', 'Gm', 'Gm'),
    ('Gy', 'Gy', 'Gx'),
    ('Gy', 'Gy', 'Gm'),
    ('Gy', 'Gx', 'Gx'),
    ('Gy', 'Gx', 'Gm'),
    ('Gy', 'Gm', 'Gx'),
    ('Gy', 'Gm', 'Gm'),
    ('Gx', 'Gx', 'Gm'),
    ('Gx', 'Gm', 'Gm') ])


#Construct a target gateset: Identity, sym X(pi/2), sym Y(pi/2), Molmer-Sorenson
gs_target = _qutrit.make_qutrit_gateset(errorScale=0, Xangle=_pi/2, Yangle=_pi/2,
                                       MSglobal=_pi/2, MSlocal=0, basis="qt")

legacy_gs_target = _qutrit.make_qutrit_gateset(errorScale=0, Xangle=-_pi/2, Yangle=_pi/2,
                                       MSglobal=-_pi/2, MSlocal=0, basis="qt")
  #Note: negative signs from weird/incorrect conventions

global_fidPairs =  [
    (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (6, 0), (7, 5), (7, 6), 
    (8, 4)]

pergerm_fidPairsDict = {
  ('Gx',): [
        (1, 4), (2, 0), (2, 1), (2, 2), (2, 6), (5, 3), (5, 5), 
        (5, 6), (6, 0), (6, 5), (8, 2), (8, 3)],
  ('Gm',): [
        (0, 2), (1, 2), (2, 5), (3, 1), (7, 1), (8, 0), (8, 3), 
        (8, 6)],
  ('Gi',): [
        (0, 0), (0, 5), (0, 6), (1, 0), (2, 1), (2, 3), (3, 1), 
        (3, 3), (3, 4), (4, 0), (4, 1), (5, 6), (6, 2), (6, 5), 
        (7, 4), (8, 2), (8, 5)],
  ('Gy',): [
        (0, 0), (3, 1), (3, 3), (3, 6), (4, 0), (5, 1), (5, 5), 
        (5, 6), (7, 4), (8, 2)],
  ('Gx', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gm'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gi', 'Gx', 'Gm'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gy', 'Gm'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gx', 'Gy', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gm', 'Gm'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gi', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gi', 'Gm', 'Gx'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gi', 'Gi'): [
        (1, 4), (2, 0), (2, 1), (2, 2), (2, 6), (5, 3), (5, 5), 
        (5, 6), (6, 0), (6, 5), (8, 2), (8, 3)],
  ('Gx', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gi', 'Gi'): [
        (0, 0), (3, 1), (3, 3), (3, 6), (4, 0), (5, 1), (5, 5), 
        (5, 6), (7, 4), (8, 2)],
  ('Gx', 'Gm', 'Gy'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gy', 'Gx', 'Gy', 'Gm'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gx', 'Gx', 'Gi', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gm', 'Gm', 'Gm'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gy', 'Gm', 'Gm'): [
        (0, 1), (1, 1), (2, 0), (2, 6), (5, 0), (5, 1), (6, 5), 
        (6, 6)],
  ('Gm', 'Gy', 'Gm', 'Gx'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gx', 'Gy', 'Gy'): [
        (0, 1), (1, 1), (2, 0), (2, 6), (5, 0), (5, 1), (6, 5), 
        (6, 6)],
  ('Gx', 'Gi', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gi', 'Gx', 'Gy', 'Gm'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gx', 'Gi', 'Gm', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gm', 'Gy', 'Gm', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gm', 'Gy', 'Gx'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gy', 'Gx', 'Gy', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gy', 'Gy', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gi', 'Gx', 'Gm', 'Gx'): [
        (0, 0), (0, 3), (1, 0), (1, 4), (3, 5), (4, 1), (4, 2), 
        (8, 0)],
  ('Gy', 'Gm', 'Gm', 'Gm'): [
        (1, 0), (2, 4), (2, 6), (4, 3), (4, 4), (5, 0), (5, 2), 
        (5, 3), (7, 1), (7, 3)],
  ('Gy', 'Gy', 'Gy', 'Gy'): [
        (0, 2), (1, 1), (1, 2), (2, 2), (2, 4), (6, 3), (6, 6), 
        (8, 3)],
  ('Gi', 'Gy', 'Gy', 'Gm'): [
        (0, 1), (0, 3), (0, 5), (1, 2), (1, 6), (2, 1), (2, 2), 
        (2, 5), (6, 1), (6, 5), (8, 0), (8, 5)],
  ('Gx', 'Gy', 'Gm', 'Gy'): [
        (0, 3), (1, 5), (3, 2), (4, 0), (4, 6), (5, 4), (6, 1), 
        (6, 3), (7, 2), (8, 0)],
  ('Gm', 'Gm', 'Gi', 'Gi'): [
        (0, 4), (1, 4), (2, 1), (2, 5), (3, 1), (3, 3), (8, 2), 
        (8, 4)],
  ('Gx', 'Gx', 'Gy', 'Gx'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gm', 'Gi', 'Gx', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gy', 'Gy', 'Gy', 'Gy'): [
        (1, 4), (2, 0), (2, 1), (2, 2), (2, 6), (5, 3), (5, 5), 
        (5, 6), (6, 0), (6, 5), (8, 2), (8, 3)],
  ('Gy', 'Gi', 'Gm', 'Gx', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gy', 'Gx', 'Gm', 'Gx'): [
        (0, 1), (0, 3), (0, 5), (1, 2), (1, 6), (2, 1), (2, 2), 
        (2, 5), (6, 1), (6, 5), (8, 0), (8, 5)],
  ('Gm', 'Gx', 'Gi', 'Gy', 'Gx'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gx', 'Gx', 'Gy', 'Gm', 'Gy'): [
        (0, 3), (2, 6), (3, 2), (3, 3), (5, 2), (5, 6), (6, 4), 
        (7, 1)],
  ('Gm', 'Gi', 'Gm', 'Gy', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gi', 'Gm', 'Gi', 'Gy'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gm', 'Gx', 'Gi', 'Gx', 'Gx'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gm', 'Gx', 'Gy', 'Gy'): [
        (0, 0), (0, 1), (0, 4), (1, 5), (3, 6), (4, 5), (5, 3), 
        (5, 6), (6, 0), (7, 5), (7, 6), (8, 4)],
  ('Gx', 'Gy', 'Gm', 'Gx', 'Gi'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gy', 'Gi', 'Gi', 'Gy', 'Gx'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gy', 'Gm', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gy', 'Gy', 'Gx', 'Gx', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gm', 'Gy', 'Gm', 'Gm', 'Gy'): [
        (0, 0), (0, 3), (1, 0), (1, 4), (3, 5), (4, 1), (4, 2), 
        (8, 0)],
  ('Gy', 'Gx', 'Gx', 'Gy', 'Gx', 'Gm'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gi', 'Gx', 'Gx', 'Gi', 'Gy', 'Gy'): [
        (0, 1), (1, 1), (2, 0), (2, 6), (5, 0), (5, 1), (6, 5), 
        (6, 6)],
  ('Gi', 'Gm', 'Gx', 'Gy', 'Gm', 'Gy'): [
        (0, 3), (1, 5), (3, 2), (4, 0), (4, 6), (5, 4), (6, 1), 
        (6, 3), (7, 2), (8, 0)],
  ('Gm', 'Gy', 'Gi', 'Gx', 'Gy', 'Gi'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gy', 'Gi', 'Gx', 'Gx', 'Gy', 'Gm'): [
        (0, 0), (0, 3), (1, 0), (1, 4), (3, 5), (4, 1), (4, 2), 
        (8, 0)],
  ('Gx', 'Gi', 'Gi', 'Gy', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gm', 'Gy', 'Gx', 'Gm', 'Gm', 'Gy'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gm', 'Gx', 'Gy', 'Gx', 'Gx', 'Gx'): [
        (1, 5), (2, 6), (3, 3), (4, 0), (4, 1), (5, 2), (6, 0), 
        (6, 5), (6, 6), (7, 4)],
  ('Gi', 'Gy', 'Gx', 'Gx', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gx', 'Gx', 'Gy', 'Gx', 'Gy', 'Gy'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
  ('Gm', 'Gm', 'Gi', 'Gi', 'Gy', 'Gi'): [
        (0, 0), (0, 4), (3, 6), (4, 5), (5, 3), (7, 5), (7, 6), 
        (8, 4)],
}
