import sys
import unittest

# Discover and run tests
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_*.py')  # Look for files starting with 'test_'
runner = unittest.TextTestRunner()
runner.run(suite)
