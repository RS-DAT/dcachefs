__version__ = "0.2.0"
__author__ = "Francesco Nattino"
__email__ = "f.nattino@esciencecenter.nl"
__all__ = ["dCacheFileSystem"]

import logging

import fsspec

from .dcachefs import dCacheFileSystem

logging.getLogger(__name__).addHandler(logging.NullHandler())

fsspec.register_implementation("dcache", "dcachefs.dCacheFileSystem", clobber=True)
