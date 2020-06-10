"""
gbApi - qeaml's wrapper for GameBanana's API

Usage:

	from gbApi import *
	gb = gbApi()
	m = gb.get_map(123)
	print(m.name)
"""

__author__ = "qeaml <qeaml@wp.pl>"
__version__ = "0.1.0"
version_info = (0, 1, 0, "beta", 1)

from .client import gbApi as Client

__all__ = ["Client"]