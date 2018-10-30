import telegram
from src import randomvideo
import re

regex = 'bm[\.\?\!]?'


def response_random_video(update):
    """
    response_random_video(request, bot) - sends random video to telegram chat

    :param update: web request from telegram bot
    :return: link to YouTube Video
    """

    user = update.message.chat.username
    message = update.message.text

    print('Received message %s from %s' % (message, user))

    if re.match(regex, message):

        video_link = randomvideo.random_video()

        # repeat the same message back (echo)
        print('Sending link %s to %s' % (video_link, user))
        return video_link
    return None
