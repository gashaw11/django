import sys
import unittest

# Discover and run tests
loader = unittest.TestLoader()
suite = loader.discover('tests/shortcuts', pattern='test_*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
