from src import quotes


def test_quote_should_be_none_for_empty_cache():
    cache = {'quotes': {}}
    quote = quotes.get_random(cache)
    assert quote is None


def test_quote_should_be_in_cache():
    cache = {'quotes': {0: 'test1', 1: 'test2'}}
    quote = quotes.get_random(cache)
    assert quote in list(cache['quotes'].values())
