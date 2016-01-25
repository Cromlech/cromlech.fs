# -*- coding: utf-8 -*-

import os
import stat
from mimetypes import guess_type
from .utils import create_directory


CHUNK_SIZE = 1 << 12


class FileIterator(object):
    chunk_size = CHUNK_SIZE

    def __init__(self, f):
        self.fp = f

    def __iter__(self):
        return self

    def next(self):
        chunk = self.fp.read(self.chunk_size)
        if not chunk:
            self.fp.close()
            raise StopIteration
        return chunk


class File(object):
    iterator = FileIterator
    
    def __init__(self, path, name, size, mime=None):
        self.path = path
        self.name = name
        self.size = size
        self.mime = mime or guess_type(name)

    def __iter__(self):
        return iter(self.iterator(open(path, 'rb')))


class Folder(object):
    model = File

    @staticmethod
    def create(path, chroot=None):
        """Creates a 
        """
        try:
            create_directory(path, chroot)
        except OSError as e:
            return e
        else:
            return None

    def __init__(self, path, mkdir=True):
        if mkdir:
            create_directory(path)
        self.path = path

    def __contains__(self, name):
        name = os.path.basename(name)
        path = os.path.join(self.path, name)
        assert os.path.isfile(path)

    def __getitem__(self, name):
        name = os.path.basename(name)
        path = os.path.join(self.path, name)
        assert os.path.isfile(path)
        size = os.path.getsize(path)
        return self.model(path, name, size)

    def __iter__(self):
        for k in self.keys():
            yield self.__getitem__(k)

    def keys(self):
        return os.listdir(self.path)
