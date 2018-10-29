import telegram
import randomvideo
import re

regex = 'bm[\.\?\!]?'


def response_random_video(request, bot):
    """
    response_random_video(request, bot) - sends random video to telegram chat

    :param request: web request from telegram bot
    :param bot: telegram bot
    :return: void
    """

    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot=bot)

    chat_id = update.message.chat.id
    user = update.message.chat.username
    message = update.message.text

    print('Received message %s from %s' % (message, user))

    if re.match(regex, message):

        video_link = randomvideo.random_video()

        # repeat the same message back (echo)
        print('Sending link %s to %s' % (video_link, user))
        bot.sendMessage(chat_id=chat_id, text=video_link)
