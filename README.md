# Slack Notifier Module

This module provides a simple interface to send notifications to Slack using the Slack SDK for Python.

## Installation

Install the module using [Rye](https://rye.astral.sh) is recommended.
Run the following command to add the module to your project:

```bash
rye add --git github.com/rye/slack-notifier
rye sync
```

Then you can import the module in your Python code:

```python
from slack_notifier import SlackNotifier
```

## Usage

### Example Usage

Here is an example of how to use the `SlackNotifier` class to send a message to Slack:

```python
from slack_notifier import SlackNotifier

def main():
    token = "slack-token"
    channel = "slack-channel"
    username = "slack-username"  # Optional

    notifier = SlackNotifier(token, channel, username)

    message = "Hello from your Slack notifier!"
    notifier.send_message(message)

if __name__ == "__main__":
    main()
```

### Explanation

- Replace `"slack-token"`, `"slack-channel"`, and `"slack-username"` with your actual Slack API token, channel, and username (if applicable).
- The `SlackNotifier` class initializes a Slack client with the provided token and sends a message to the specified channel using the `send_message` method.
- If the username is provided, it will be used as the sender of the message; otherwise, the default sender will be used.
