import argparse
from email_adapter import EmailAdapter

def main():
    parser = argparse.ArgumentParser(description='Send email notifications from the command line.')
    parser.add_argument('--to', required=True, help='Recipient email address')
    parser.add_argument('--message', required=True, help='The message to send')
    parser.add_argument('--subject', help='Email subject (default: "Notification")')

    args = parser.parse_args()

    adapter = EmailAdapter()
    adapter.send(args.message, to_email=args.to, subject=args.subject or "Notification")

if __name__ == "__main__":
    main()
