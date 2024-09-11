"""Script to test the SlackNotifier class."""

from slack_notifier import SlackNotifier


def main() -> None:
    """Test the SlackNotifier class."""
    token = "slack-token"
    channel = "slack-channel"
    username = "slack-username"  # Optional

    notifier = SlackNotifier(token, channel, username)

    message = "Hello from your Slack notifier!"
    notifier.send_message(message)


if __name__ == "__main__":
    main()
