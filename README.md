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
```

### Explanation

- Replace `"#slack-channel"` and `"slack-username"` with your actual Slack channel (name or ID) and username (if applicable).
- The `SlackNotifier` class will automatically try to load the Slack API token from the environment variable:
  - By default, it looks for the `SLACK_TOKEN` environment variable.
  - You can specify a different environment variable name using the `token_env_var` parameter.
  - If the token is not found in the environment variable, the class will attempt to load it from the `.env` file (if present).
  - If no token is found in either the environment variable or `.env` file, an error will be raised.
- The `SlackNotifier` class initializes a Slack client with the loaded token and sends a message to the specified channel using the `send_message` method.
- If the username is provided, it will be used as the sender of the message; otherwise, the default sender will be used.
