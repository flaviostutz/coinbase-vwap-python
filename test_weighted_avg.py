#!/usr/bin/env python3

import unittest
from decimal import *
from mathutils import weighted_avg

class TestWeightedAvg(unittest.TestCase):

    def test_Simple(self):        
        wa1 = weighted_avg.WeightedAvg(1)

        wa1.add(Decimal("1"), Decimal("1"))
        self.assertEqual("1", str(wa1.avg()))

        wa1.add(Decimal("2"), Decimal("2"))
        self.assertEqual("2", str(wa1.avg()))

        wa1.add(Decimal("3"), Decimal("3"))
        self.assertEqual("3", str(wa1.avg()))

    def test_Regular(self):
        wa = weighted_avg.WeightedAvg(3)

        wa.add(Decimal("1"), Decimal("1"))
        self.assertEqual("1", str(wa.avg()))

        wa.add(Decimal("3"), Decimal("1"))
        self.assertEqual("2", str(wa.avg()))

        wa.add(Decimal("2"), Decimal("1"))
        self.assertEqual("2", str(wa.avg()))

        wa.add(Decimal("7"), Decimal("1"))
        self.assertEqual("4", str(wa.avg()))

        wa.add(Decimal("15"), Decimal("1"))
        self.assertEqual("8", str(wa.avg()))

    def test_Advanced(self):
        wa = weighted_avg.WeightedAvg(4)

        wa.add(Decimal("1"), Decimal("2"))
        self.assertEqual("1", str(wa.avg()))

        wa.add(Decimal("1"), Decimal("4"))
        self.assertEqual("1", str(wa.avg()))

        wa.add(Decimal("3"), Decimal("2"))
        self.assertEqual("1.5", str(wa.avg()))

        #this should remove the first sample from calc
        wa.add(Decimal("2"), Decimal("6"))
        self.assertEqual("1.714285714", str(wa.avg())[:11])

        wa.add(Decimal("3"), Decimal("1"))
        self.assertEqual("1.923076923", str(wa.avg())[:11])
