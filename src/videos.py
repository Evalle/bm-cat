import random


def get_random(cache):
    try:
        video_id = random.choice(list(cache['videos'].keys()))
        if video_id:
            return 'https://youtu.be/' + video_id
    except IndexError:
        print('Videos dict is empty')
