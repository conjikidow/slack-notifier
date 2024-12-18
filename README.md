# Slack Notifier Package

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This package provides a simple interface to send notifications to Slack using the Slack SDK for Python.

## Installation

Install the package using [uv](https://github.com/astral-sh/uv) is recommended.
Run the following command to add the package to your project:

```console
uv add git+https://github.com/conjikidow/slack-notifier
```

Then you can import the package in your Python code:

```python
from slack_notifier import SlackNotifier
```

## Usage

### Example Usage

Here is an example of how to use the `SlackNotifier` class to send a message to Slack:

```python
import logging

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
    logging.basicConfig(level=logging.INFO)

    main()
```

### Explanation

- Replace `"slack-token"`, `"slack-channel"`, and `"slack-username"` with your actual Slack API token, channel, and username (if applicable).
- The `SlackNotifier` class initializes a Slack client with the provided token and sends a message to the specified channel using the `send_message` method.
- If the username is provided, it will be used as the sender of the message; otherwise, the default sender will be used.
