"""Example script to demonstrate the usage of the SlackNotifier class."""

import logging

from slack_notifier import SlackNotifier


def main() -> None:
    """Demonstrate usage of the SlackNotifier class."""
    channel = "#slack-channel"  # Specify the Slack channel name (with #) or ID
    username = "slack-username"  # Optional: Provide the username for sending the message
    token_env_var = "SLACK_API_TOKEN"  # Optional: Defaults to "SLACK_TOKEN", or specify your own environment variable name

    # Initialize SlackNotifier with the channel, optional username, and optional token environment variable name
    notifier = SlackNotifier(channel, username=username, token_env_var=token_env_var)

    message = "Hello from your Slack notifier!"  # The message to send
    notifier.send_message(message)  # Send the message to Slack


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
