#
# Tests for the Scipy Differential Evolution Optimiser class
#
import pbparam

import unittest

from tests.shared import DummyOptimisationProblem


class TestScipyDifferentialEvolution(unittest.TestCase):
    def test_scipy_differential_evolution_init(self):
        optimiser = pbparam.ScipyDifferentialEvolution()
        self.assertEqual(optimiser.name, "SciPy Differential Evolution optimiser")
        self.assertFalse(optimiser.single_variable)
        self.assertTrue(optimiser.global_optimiser)
        self.assertEqual(optimiser.extra_options, {})

    def test_optimiser(self):
        opt = DummyOptimisationProblem()
        opt.cost_function = lambda x: x[0] ** 2
        opt.x0 = 2
        opt.bounds = [[-10, 10]]

        optimiser = pbparam.ScipyDifferentialEvolution()
        result = optimiser.optimise(opt)
        self.assertAlmostEqual(result.x[0], 0, places=6)


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()