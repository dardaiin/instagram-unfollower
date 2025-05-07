# Instagram Unfollower

A simple Python script to check which Instagram users you follow but don't follow you back.

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

The script will:

1. Prompt you to enter your Instagram username and password securely (password input will be hidden)
2. If you have two-factor authentication enabled (this won't work with SMS or WhatsApp):
   - You'll be prompted to enter the 2FA code from your authenticator app
   - Enter the code when prompted
3. Log in to your Instagram account
4. Get your followers and following lists
5. Compare them to find who isn't following you back
6. Display the results in a numbered list

## Security Features

- Password input is hidden while typing
- Credentials are not stored anywhere on disk
- Credentials are only kept in memory during script execution
- No sensitive data is logged or saved
- Supports two-factor authentication for enhanced security

## Requirements

- Python 3.7 or higher
- Internet connection
- Instagram account
- If using 2FA: Access to your authenticator app

## Warning

Should be safe to use, you can review the code. Some users have reported using Instaloader to being locked out or banned.
