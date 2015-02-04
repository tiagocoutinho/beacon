"""Beacon test module
"""
import os
import unittest
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..")))

from beacon.conductor import client
from beacon.conductor import connection
from beacon import static

class TestBeaconHost(unittest.TestCase):
    def setUp(self):
        pass

    def testGetConfig(self):
        self.assertEquals(client._default_connection, None)
        cfg = static.get_config()
        self.assertEquals(client._default_connection._host, None)
        print cfg.names_list
        self.assertTrue(cfg)

    def testGetConfigWHost(self):
        os.environ["BEACON_HOST"]="localhost"
        c = connection.Connection()
        # replace default connection with this one
        client._default_connection = c
        self.assertEquals(client._default_connection._host, "localhost")
        cfg = static.get_config()
        # reload, to use new connection 
        cfg.reload()
        print cfg.names_list
        self.assertTrue(cfg)

if __name__ == '__main__':
    unittest.main()
