import os

import searcher

def test_search_runner():

    result = searcher.search_runner(os.path.abspath('./fixtures/config.toml'), 'A test runner')

    assert result
