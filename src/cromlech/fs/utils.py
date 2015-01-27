# -*- coding: utf-8 -*-

import os
from . import FSError, ChRootError

RXW = (os.F_OK,
       os.R_OK,
       os.W_OK,
       os.X_OK)


def access_permissions(path, *perms):
    for perm in perms:
        if not os.access(path, os.W_OK):
            return False
    return True


def create_directory(path, chroot=None):
    """Returns True if the creation was complete or if
    the folder already exists and is writeable.
    """
    realpath = os.path.realpath(path)
    if chroot is not None:
        rooted = os.path.realpath(chroot)
        if not os.path.isdir(rooted):
            raise ChRootError('%r is not a valid directory.' % chroot)
        if not can_use_chroot(rooted):
            raise ChRootError('%r has the wrong permissions.' % chroot)
        if not realpath.startswith(rooted):
            raise ChRootError('%r is not contained in the root %r.' % 
                              (path, chroot))
        assert access_permissions(rooted, *RXW)

    if os.path.exists(realpath):
        if not os.path.isdir(realpath):
            raise FSError('%r exists and is not a folder' % path)
        else:
            assert access_permissions(realpath, *RXW)
    else:
        os.makedirs(realpath, 0755)

    return True
