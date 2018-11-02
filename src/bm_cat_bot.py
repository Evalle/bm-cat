import telegram
from telegram import Bot
from src import random_video_request_handler, quotes
from telegram import InlineQueryResultArticle, InputTextMessageContent


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

        result_message = self.__get_video_link_message(update)
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

    def __get_video_link_message(self, update):
        """
        create string with random quote and random video from YT

        :param update: bot update structure
        :return: string
        """
        video_link = random_video_request_handler.response_random_video(update)
        if not video_link:
            return None
        random_quote = quotes.random_quote(self.data_provider['quotes'])
        return '%s\n\r%s' % (random_quote, video_link)
