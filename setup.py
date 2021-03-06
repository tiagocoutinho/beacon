from distutils.core import setup

# dependencies:
#  - gevent
#  - redis
#  - yaml
#  - netifaces
#  - louie (or old pydispatch)
#  - nanomsg
# optional dependencies:
#  - ruamel (yaml preserving comments, style, key order)
#  - posix_ipc (use posix queues)

setup(name="beacon", version="0.1",
      description="BEAmline CONfiguration library",
      author="S. Petitdemange, M. Guijarro (ESRF)",
      package_dir={"beacon": "beacon"},
      packages=["beacon", "beacon.conductor",
                "beacon.plugins","beacon.redis"],
      package_data={'beacon.redis':['redis.conf']},
      scripts=["bin/beacon-server"])
