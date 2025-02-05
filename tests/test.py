"""Script to test the SlackNotifier class."""

import logging

from slack_notifier import SlackNotifier


def main() -> None:
    """Test the SlackNotifier class."""
    channel = "#slack-channel"  # Either the channel name (with #) or ID
    username = "slack-username"  # Optional
    token_env_var = "SLACK_API_TOKEN"  # Optional, defaults to "SLACK_TOKEN"

    # Initialize SlackNotifier with the channel, username, and optional token environment variable name
    notifier = SlackNotifier(channel, username, token_env_var=token_env_var)

    message = "Hello from your Slack notifier!"
    notifier.send_message(message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main()
