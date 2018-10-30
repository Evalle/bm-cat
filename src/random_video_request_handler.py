import telegram
from src import randomvideo
import re


def response_random_video(update):
    """
    response_random_video(request, bot) - sends random video to telegram chat

    :param update: web request from telegram bot
    :return: link to YouTube Video
    """
    regex = 'bm[\.\?\!]?'

    if update.message is None:
        message = update.inline_query.query
    else:
        message = update.message.text
        user = update.message.chat.username
        print('Received message %s from %s' % (message, user))

    if re.match(regex, message, re.IGNORECASE):

        video_link = randomvideo.random_video()

        return video_link
    return None
