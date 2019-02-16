#
# Tests for the standard parameters
#
import pybamm

import unittest


class TestStandardParameters(unittest.TestCase):
    def test_geometric_parameters(self):
        Ln = pybamm.standard_parameters.Ln
        Ls = pybamm.standard_parameters.Ls
        Lp = pybamm.standard_parameters.Lp
        Lx = pybamm.standard_parameters.Lx
        ln = pybamm.standard_parameters.ln
        ls = pybamm.standard_parameters.ls
        lp = pybamm.standard_parameters.lp

        parameter_values = pybamm.ParameterValues(
            base_parameters={"Ln": 0.05, "Ls": 0.02, "Lp": 0.21}
        )
        Ln_eval = parameter_values.process_symbol(Ln)
        Ls_eval = parameter_values.process_symbol(Ls)
        Lp_eval = parameter_values.process_symbol(Lp)
        Lx_eval = parameter_values.process_symbol(Lx)
        self.assertEqual((Ln_eval + Ls_eval + Lp_eval).evaluate(), Lx_eval.evaluate())
        self.assertEqual((Ln_eval + Ls_eval + Lp_eval).id, Lx_eval.id)
        ln_eval = parameter_values.process_symbol(ln)
        ls_eval = parameter_values.process_symbol(ls)
        lp_eval = parameter_values.process_symbol(lp)
        self.assertAlmostEqual((ln_eval + ls_eval + lp_eval).evaluate(), 1)

    def test_functions(self):
        # create current functions
        current_function = pybamm.standard_current_functions.constant_current
        t = pybamm.t
        current = pybamm.standard_parameters.dimensional_current(2, current_function, t)
        dimensionless_current = pybamm.standard_parameters.dimensionless_current(
            current_function, t
        )

        # process
        parameter_values = pybamm.ParameterValues()
        current_eval = parameter_values.process_symbol(current)
        dimensionless_current_eval = parameter_values.process_symbol(
            dimensionless_current
        )
        self.assertEqual(current_eval.evaluate(t=3), 2)
        self.assertEqual(dimensionless_current_eval.evaluate(t=3), 1)


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
