# Aiogram Sea Helper Bots

Legacy Aiogram-based Telegram bots for maritime community support workflows.

The repository contains two bot entrypoints:

- `Mainbot3.py` - chat moderation, onboarding messages, rating handling, and ChatGPT-style replies.
- `Seahelper3.py` - menu-driven helper bot with company lookup, rules, admin contact flow, and FSM-based conversations.

This is a portfolio cleanup of an older private bot project. Secrets and experimental Dialogflow/test files were removed from the public tree.

## Features

- Aiogram 2.x Telegram bot handlers.
- Channel onboarding and leave-event logging.
- Inline and reply keyboard navigation.
- Admin-only flows and restricted handlers.
- OpenAI chat response helper.
- Maritime helper text and company lookup utilities.

## Requirements

- Python 3.10+
- Telegram bot token
- OpenAI API key if GPT replies are enabled

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Configuration

Copy the example config and fill it locally:

```bash
cp Keys/key.example.ini Keys/key.ini
```

`Keys/key.ini` is ignored by Git and must never be committed.

Required sections:

```ini
[Telegram]
token = replace-with-production-bot-token
token2 = replace-with-secondary-bot-token
token_test = replace-with-test-bot-token
admin_id = 123456789
channel_id = -1000000000000
test_channel_id = -1000000000000
dashboard_channel_id = -1000000000000
log_channel_id = -1000000000000

[OpenAI]
openai_key = replace-with-openai-api-key
```

## Run

Main bot:

```bash
python Mainbot3.py
```

Sea helper bot:

```bash
python Seahelper3.py
```

## Project Layout

```text
.
├── Mainbot3.py              # Main Telegram bot entrypoint
├── Seahelper3.py            # Sea helper bot entrypoint
├── Bothelper/               # Seahelper buttons, text, decorators, utilities
├── Mainbot/                 # Mainbot buttons, text, ratings, GPT helper
├── Keys/key.example.ini     # Safe config template
├── requirements.txt
└── screenshot.png
```

## Security Notes

Real bot tokens, OpenAI keys, Google service-account JSON, IDE state, and experimental test scripts are excluded from this public release. Rotate any credentials that were ever committed before this cleanup.

## License

MIT License. See [LICENSE](LICENSE).
