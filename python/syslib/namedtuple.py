import new
import struct
from collections import namedtuple

Config = namedtuple("Config", "a b c d")
Config.pattern = "HHHH"
Config.pack = new.instancemethod(
            lambda self, *args:
                struct.pack(Config.pattern, *args),
            Config, None)
Config.unpack = new.instancemethod(
            lambda self, packed_cfg:
                Config(*struct.unpack(Config.pattern, packed_cfg)),
            Config, None)



'''
cfg = Config(1, 2, 3, 4)
packed_cfg = struct.pack(Config.pattern, *cfg)
newCfg = Config(*struct.unpack(Config.pattern, packed_cfg))
'''
packed_cfg = Config.pack(1, 2, 3, 4)
newCfg = Config.unpack(packed_cfg)
print newCfg.a, newCfg.b, newCfg.c, newCfg.d
