import pytest
import py_call_graph


if __name__ == '__main__':
    pytest.main(['-x', './tests/'], plugins=[py_call_graph])
