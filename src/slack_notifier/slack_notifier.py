"""Module providing a SlackNotifier class for sending notifications to Slack."""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from rich.logging import RichHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackNotifier:

    """Class for sending notifications to Slack."""

    def __init__(self, channel: str, username: str | None = None, token_env_var: str = "SLACK_TOKEN") -> None:  # noqa: S107
        """Initialize the SlackNotifier object.

        Args:
            channel (str): The Slack channel name or ID to send notifications to.
            username (str, optional): The username to use for sending notifications. Defaults to None.
            token_env_var (str, optional): The environment variable name for the Slack API token. Defaults to "SLACK_TOKEN".

        """
        self.__logger = logging.getLogger(__name__)
        self.__logger.propagate = False
        if not self.__logger.handlers:
            rich_handler = RichHandler(markup=True, rich_tracebacks=True)
            formatter = logging.Formatter("[green][SlackNotifier][/green] %(message)s", datefmt="[%X]")
            rich_handler.setFormatter(formatter)
            self.__logger.addHandler(rich_handler)

        # Try to get the token from the environment variable
        token = os.getenv(token_env_var)

        # If the token is not found in the environment variable, try loading from .env file
        if not token:
            load_dotenv()  # Load .env file
            token = os.getenv(token_env_var)

        # If the token is still not found, raise an exception
        if not token:
            error_message = f"{token_env_var} is not set in environment variables or .env file."
            self.__logger.error(error_message)
            raise ValueError(error_message)

        try:
            self.__client = WebClient(token=token)
            self.__client.auth_test()
        except SlackApiError as e:
            log_message = f"Failed to initialize Slack client: {e.response['error']}"
            self.__logger.exception(log_message)
            raise

        self.__channel = channel
        self.__username = username

    def send_message(self, message: str, file_paths: list[Path] | None = None) -> bool:
        """Send a message to Slack, optionally with files.

        Args:
            message (str): The message to send.
            file_paths (list[Path], optional): List of file paths to attach. Defaults to None.

        Returns:
            bool: True if the message was sent successfully, False otherwise.

        """
        kwargs = {"channel": self.__channel}
        if self.__username:
            kwargs["username"] = self.__username

        if file_paths:
            for file_path in file_paths:
                if file_path.exists():
                    # Upload file to Slack
                    response = self.__client.files_upload_v2(
                        title=f"{file_path.name}",
                        file=str(file_path),
                    )
                    message += f"<{response['file']['permalink']}| >"
                else:
                    log_message = f"File {file_path} not found. Skipping this file."
                    self.__logger.warning(log_message)

        kwargs["text"] = message

        try:
            self.__client.chat_postMessage(**kwargs)
            log_message = f"Notification sent to Slack channel {self.__channel}"
            self.__logger.info(log_message)
        except SlackApiError as e:
            log_message = f"Failed to send notification: {e.response['error']}"
            self.__logger.exception(log_message)
            return False

        return True
