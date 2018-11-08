from src import videos


def test_video_should_be_none_for_empty_cache():
    cache = {'videos': {}}
    video = videos.get_random(cache)
    assert video is None


def test_video_should_be_be_in_array():
    cache = {'videos': {'test1': {'id_1': 'test_1', 'id_2': 'test_2'}, 'test2': {'id_3': 'test_3', 'id_4': 'test_4'}}}
    video_urls = ['https://youtu.be/' + x for x in list(cache['videos'].keys())]
    video = videos.get_random(cache)
    assert video in video_urls
