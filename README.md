# Slack Notifier Package

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/conjikidow/slack-notifier/actions/workflows/ci.yaml/badge.svg)](https://github.com/conjikidow/slack-notifier/actions/workflows/ci.yaml)

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
from pathlib import Path

from slack_notifier import SlackNotifier


def main() -> None:
    channel = "#slack-channel"  # Specify the Slack channel name (with #) or ID
    username = "slack-username"  # Optional: Provide the username for sending the message
    token_env_var = "SLACK_API_TOKEN"  # Optional: Defaults to "SLACK_TOKEN", or specify your own environment variable name

    # Initialize SlackNotifier with the channel, optional username, and optional token environment variable name
    notifier = SlackNotifier(channel, username=username, token_env_var=token_env_var)

    message = "Hello from your Slack notifier!"  # The message to send
    notifier.send_message(message)  # Send the message to Slack

    attachments = [
        Path("tests/data/test_file.txt"),
        Path("tests/data/test_file.png"),
    ]
    message = "Hello from your Slack notifier with file attachments!"
    notifier.send_message(message, attachments=attachments)  # Send the message with file attachments


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
- If file paths are provided in the `attachments` parameter, the files will be uploaded as attachments to the message.

### Obtaining Your Slack API Token

To use the Slack API, you need to create a Slack App and generate a bot token. Follow these steps:

1. **Create a Slack App**:
   - Go to [Slack API: Your Apps](https://api.slack.com/apps).
   - Click on the **Create New App** button.
   - Select either **From scratch** or **Using an app manifest** to create your app. Provide the necessary details, such as the name of your app and the workspace where you want it installed.

2. **Set Up Permissions**:
   - Once your app is created, navigate to the **OAuth & Permissions** section under the **Features** tab.
   - Here, you will define the **Bot Token Scopes** that your app requires. For sending messages, you need at least the following permissions:
     - `chat:write` - Send messages to channels.
     - `chat:write.customize` - Send messages with a custom username and avatar (optional, but required when specifying a custom username).
     - `files:write` - Upload files (optional, but required for sending file attachments).

     ![Image](https://github.com/user-attachments/assets/b80548d0-392d-4524-906c-d870bb53e02c)

3. **Install the App**:
   - Go to the **Install App** section in the left sidebar of your app's settings.
   - Click **Install to Workspace** to install the app to your Slack workspace.
   - You’ll be prompted to authorize the app. Once authorized, you’ll be given an **OAuth Access Token** (starts with `xoxb-`), which is the token you will use for API requests.

4. **Set the Token as an Environment Variable**:
   - You can set the obtained OAuth token as an environment variable called `SLACK_TOKEN`. Alternatively, you can specify a different environment variable name by passing it to the `SlackNotifier` class.

For more details, visit the [Slack API Authentication Documentation](https://api.slack.com/authentication).
