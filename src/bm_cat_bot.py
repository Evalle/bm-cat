import telegram
from telegram import Bot
from src import quotes, videos
from telegram import InlineQueryResultArticle, InputTextMessageContent
import re


class BMCatBot:
    """
    represents entire logic of bm cat bot
    """

    def __init__(self, api_key, data_provider):
        self.bot = None
        self.api_key = api_key
        self.data_provider = data_provider

    def send_random_video(self, update, bot=None):
        """
        sending random video from youtube with random black metal quote

        :param update: telegram update struct
        :param bot: telegram bot
        :return: void
        """
        if not bot:
            bot = self.bot
        else:
            if not bot:
                try:
                    bot = self.get_bot()
                except telegram.error.InvalidToken:
                    return

        result_message = self._get_result_message(update)
        if not result_message:
            return

        query = update.inline_query
        if query:
            results = list()
            results.append(
                InlineQueryResultArticle(
                    id=update.inline_query.query.upper(),
                    title='send link',
                    input_message_content=InputTextMessageContent(result_message)
                )
            )
            # 10 seconds cache
            bot.answer_inline_query(update.inline_query.id, results, cache_time=10)
        else:
            bot.send_message(chat_id=update.message.chat.id, text=result_message)

    def get_bot(self):
        """
        get underlying telegram bot

        :return: telegram.bot
        """
        try:
            self.bot = Bot(self.api_key)
        except telegram.error.InvalidToken:
            print('Cannot initialize telegram bot with given api_key')
            raise telegram.error.InvalidToken
        return self.bot

    def set_web_hook(self, web_hook_url, ssl_certificate_path, bot=None):
        if not bot:
            bot = self.get_bot()
        # delete webhook before new assigning
        bot.deleteWebhook()

        # set new webhook
        bot.setWebhook(web_hook_url, certificate=open(ssl_certificate_path, 'rb'))

    def _get_result_message(self, update):
        """
        create string with random quote and random video from YT

        :param update: bot update structure
        :return: string
        """
        regex = 'bm[\.\?\!]?'

        if update.message is None:
            message = update.inline_query.query
        else:
            message = update.message.text
            user = update.message.chat.username
            print('Received message %s from %s' % (message, user))

        if re.match(regex, message, re.IGNORECASE):
            return self._get_message_body

    def _get_message_body(self):
        video_link = videos.get_random(self.data_provider)
        random_quote = quotes.get_random(self.data_provider)
        if video_link and random_quote:
            return '%s\n\r%s' % (random_quote, video_link)
        return None
