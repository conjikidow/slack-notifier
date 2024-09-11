"""Module providing a SlackNotifier class for sending notifications to Slack."""

import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackNotifier:
    """Class for sending notifications to Slack."""

    def __init__(self, token: str, channel: str, username: str | None = None) -> None:
        """Initialize the SlackNotifier object.

        Args:
            token (str): The Slack API token.
            channel (str): The Slack channel to send notifications to.
            username (str, optional): The username to use for sending notifications. Defaults to None.

        """
        self.__logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] [SlackNotifier] %(message)s",
        )

        try:
            self.__client = WebClient(token=token)
            self.__client.auth_test()
        except SlackApiError as e:
            log_message = f"Failed to initialize Slack client: {e.response['error']}"
            self.__logger.exception(log_message)
            self.__client = None

        self.__channel = channel
        self.__username = username

    def send_message(self, message: str) -> None:
        """Send a message to Slack.

        Args:
            message (str): The message to send.

        Returns:
            None

        """
        if self.__client is None:
            self.__logger.warning("Slack client is not initialized correctly. Cannot send notification.")
            return

        kwargs = {"channel": self.__channel, "text": message}
        if self.__username:
            kwargs["username"] = self.__username

        try:
            self.__client.chat_postMessage(**kwargs)
            log_message = f"Notification sent to Slack channel {self.__channel}"
            self.__logger.info(log_message)
        except SlackApiError as e:
            log_message = f"Failed to send notification: {e.response['error']}"
            self.__logger.exception(log_message)
