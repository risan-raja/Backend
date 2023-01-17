from dataclasses import dataclass
from zxcvbn import zxcvbn
from flask_security.utils import uia_email_mapper


@dataclass
class configSecurity(object):
    SECURITY_PASSWORD_SALT = (
        "65f639cff0ba3b459a800d6deaed666d56f7489697b275dded8ac5f83cf1e42d"
    )
    SECURITY_USERNAME_ENABLE = False
    SECURITY_FLASH_MESSAGES = False

    # Need to be able to route backend flask API calls. Use 'accounts'
    # to be the Flask-Security endpoints.
    SECURITY_URL_PREFIX = "/api/accounts"
    SECURITY_REDIRECT_HOST = "127.0.0.1"

    # Turn on all the great Flask-Security features
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
    SECURITY_REGISTERABLE = True
    SECURITY_UNIFIED_SIGNIN = False
    SECURITY_USER_IDENTITY_ATTRIBUTES = [
        {"email": {"mapper": uia_email_mapper, "case_insensitive": True}},
    ]
    # {"us_phone_number": {"mapper": uia_phone_mapper}},
    SECURITY_US_ENABLED_METHODS = ["password", "email"]
    SECURITY_DEFAULT_REMEMBER_ME = True
    SECURITY_PHONE_REGION_DEFAULT = "IN"
    SECURITY_PASSWORD_COMPLEXITY_CHECKER = zxcvbn
    SECURITY_PASSWORD_LENGTH_MIN = 8
    SECURITY_EMAIL_VALIDATOR_ARGS = {"check_deliverability": True}
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    """
    These need to be defined to handle redirects
    As defined in the API documentation - they will receive the relevant context
    """
    # done
    SECURITY_POST_LOGOUT_VIEW = "http://127.0.0.1/user-login"
    SECURITY_POST_CONFIRM_VIEW = "/confirmed"
    SECURITY_CONFIRM_ERROR_VIEW = "/confirm-error"
    SECURITY_RESET_VIEW = "/reset-password"
    SECURITY_RESET_ERROR_VIEW = "/reset-password"
    SECURITY_REDIRECT_BEHAVIOR = "spa"
    SECURITY_POST_LOGOUT_VIEW = "/logout"
    """
    CSRF protection is critical for all session-based browser UIs
    enforce CSRF protection for session / browser - but allow token-based
    API calls to go through
    """
    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True

    # Send Cookie with csrf-token. This is the default for Axios and Angular.
    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None
    SECURITY_TOTP_ISSUER = "None"
    SECURITY_TOTP_SECRETS = {1: "lSAG4uwH6Q9SQALv44bHgjKw4lp6RsGgVQaWIi1r4mh"}
