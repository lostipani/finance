from authenticator import AuthenticatorToken
from alphavantage import AlphaVantage


def main():
    auth = AuthenticatorToken()
    session = AlphaVantage(authenticator=auth)
    return session.get_daily("IBM")


if __name__ == "__main__":
    print(main())
