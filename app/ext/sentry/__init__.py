import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration


def init_sentry(app):
    sentry_sdk.init(
        dsn=app.config.get("SENTRY_DSN"),
        # Set tracesSampleRate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in productions
        traces_sample_rate=1.0,
        integrations=[FlaskIntegration()],
        send_default_pii=True,
        debug=True,
        environment="development",
        attach_stacktrace=True,
        _experiments={
            "profiles_sample_rate": 1.0, },
    )
    return sentry_sdk
