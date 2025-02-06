import os

import pytest
from slack_sdk.errors import SlackApiError

from slack_notifier import SlackNotifier

# Ensure a valid Slack API token is available
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = "C08BUGZ66VB"  # Specify your Slack channel ID


@pytest.mark.skipif(SLACK_TOKEN is None, reason="SLACK_TOKEN is not set")
def test_send_message_with_default_username() -> None:
    """Test sending a message to Slack with the default username."""
    # Initialize SlackNotifier
    notifier = SlackNotifier(channel=SLACK_CHANNEL)

    message = "Test message from SlackNotifier! (default username)"
    success = notifier.send_message(message)

    if not success:
        pytest.fail("Message sending failed.")


@pytest.mark.skipif(SLACK_TOKEN is None, reason="SLACK_TOKEN is not set")
def test_send_message_with_custom_username() -> None:
    """Test sending a message to Slack with a custom username."""
    # Initialize SlackNotifier with a custom username
    username = "custom-username"
    notifier = SlackNotifier(channel=SLACK_CHANNEL, username=username)

    message = "Test message from SlackNotifier! (custom username)"
    success = notifier.send_message(message)

    if not success:
        pytest.fail("Message sending failed.")


@pytest.mark.skipif(os.getenv("SLACK_TOKEN") is None, reason="SLACK_TOKEN is not set")
def test_channel_not_found() -> None:
    """Test sending a message to a non-existent channel (this should fail)."""
    # Initialize SlackNotifier with a non-existent channel
    notifier = SlackNotifier(channel="non-existent-channel")

    message = "Test message from SlackNotifier! (non-existent channel)"
    success = notifier.send_message(message)

    if success:
        pytest.fail("Expected message sending failure, but the message was sent.")


@pytest.mark.skipif(os.getenv("SLACK_TOKEN") is None, reason="SLACK_TOKEN is not set")
def test_invalid_token() -> None:
    """Test sending a message with an invalid token (this should raise an error)."""
    os.environ["SLACK_TOKEN"] = "invalid_token"  # noqa: S105

    with pytest.raises(SlackApiError) as excinfo:
        # Initialize SlackNotifier with an invalid token
        _notifier = SlackNotifier(channel=SLACK_CHANNEL)

    if excinfo.value.response["error"] != "invalid_auth":
        pytest.fail(f"Expected 'invalid_auth' error, but got '{excinfo.value.response['error']}'.")


@pytest.mark.skipif(os.getenv("SLACK_TOKEN") is None, reason="SLACK_TOKEN is not set")
def test_no_token() -> None:
    """Test if no token is provided (this should raise an error)."""
    del os.environ["SLACK_TOKEN"]

    with pytest.raises(ValueError, match="SLACK_TOKEN is not set in environment variables or .env file."):
        # Initialize SlackNotifier without a token
        _notifier = SlackNotifier(channel=SLACK_CHANNEL)
