import pytest
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph.config import Config
from pycallgraph.globbing_filter import GlobbingFilter


@pytest.fixture(autouse=True)
def record_call_graph(request):
    import time
    current_millis = int(round(time.time() * 1000))
    # import pdb
    # pdb.set_trace()
    with PyCallGraph(output=GraphvizOutput(output_file='dynCG.png', dot_file='./dotFiles/%s.dot' %
                                                                             (
                                                                              current_millis)),
                     config=Config(debug=True,
                                   trace_filter=GlobbingFilter(
                                       exclude=['pycallgraph.*', 'test*.*', '*.tests.*', '*test.*'],
                                       include=['thefuck.*'],
                                   )
                                   )):
        yield
