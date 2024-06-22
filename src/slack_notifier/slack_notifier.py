import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackNotifier:
    def __init__(self, token, channel, username=None):
        self.__logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] [SlackNotifier] %(message)s",
        )

        try:
            self.__client = WebClient(token=token)
            self.__client.auth_test()
        except SlackApiError as e:
            self.__logger.error(f"Failed to initialize Slack client: {e.response['error']}")
            self.__client = None

        self.__channel = channel
        self.__username = username

    def send_message(self, message):
        if self.__client is None:
            self.__logger.warning("Slack client is not initialized correctly. Cannot send notification.")
            return

        kwargs = {"channel": self.__channel, "text": message}
        if self.__username:
            kwargs["username"] = self.__username

        try:
            self.__client.chat_postMessage(**kwargs)
            self.__logger.info(f"Notification sent to Slack channel {self.__channel}")
        except SlackApiError as e:
            error_message = f"Failed to send notification: {e.response['error']}"
            self.__logger.error(error_message)
