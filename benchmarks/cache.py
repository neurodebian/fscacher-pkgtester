from hashlib import sha256
import os
from pathlib import Path
import random
from time import time
from uuid import uuid4
from morecontext import envset
from fscacher import PersistentCache


class TimeFile:
    FILE_SIZE = 1024
    param_names = ["n", "control"]
    params = ([10, 100, 10000], ["", "ignore"])

    def setup_cache(self):
        with open("foo.dat", "wb") as fp:
            fp.write(bytes(random.choices(range(256), k=self.FILE_SIZE)))

    def setup(self, n, control):
        with envset("FSCACHER_CACHE", control):
            self.cache = PersistentCache(name=str(uuid4()))

    def time_file(self, n, control):
        @self.cache.memoize_path
        def hashfile(path):
            with open(path, "rb") as fp:
                return sha256(fp.read()).hexdigest()

        for _ in range(n):
            hashfile("foo.dat")

    def teardown(self, n, control):
        self.cache.clear()


class TimeDirectoryFlat:
    FILES = 100
    param_names = ["n", "control"]
    params = ([10, 100, 1000], ["", "ignore"])

    def setup_cache(self):
        base_time = time()
        for x in range(self.FILES):
            f = Path(f"f{x}")
            f.write_bytes(b"\0" * random.randint(1, 1024))
            t = base_time - x
            os.utime(f, (t, t))

    def setup(self, n, control):
        with envset("FSCACHER_CACHE", control):
            self.cache = PersistentCache(name=str(uuid4()))

    def time_directory(self, n, control):
        @self.cache.memoize_path
        def dirsize(path):
            total_size = 0
            with os.scandir(path) as entries:
                for e in entries:
                    if e.is_dir():
                        total_size += dirsize(e.path)
                    else:
                        total_size += e.stat().st_size
            return total_size

        for _ in range(n):
            dirsize(os.curdir)

    def teardown(self, n, control):
        self.cache.clear()


class TimeDirectoryDeep(TimeDirectoryFlat):
    def setup_cache(self):
        base_time = time()
        layout = (3, 3, 3, 3)
        dirs = [Path()]
        for i, width in enumerate(layout):
            if i < len(layout) - 1:
                dirs2 = []
                for d in dirs:
                    for x in range(width):
                        d2 = d / f"d{x}"
                        d2.mkdir()
                        dirs2.append(d2)
                dirs = dirs2
            else:
                for j, d in enumerate(dirs):
                    for x in range(width):
                        f = d / f"f{x}.dat"
                        f.write_bytes(b"\0" * random.randint(1, 1024))
                        t = base_time - x - j * width
                        os.utime(f, (t, t))
