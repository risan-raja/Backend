export SENTRY_AUTH_TOKEN=4f059fd17a8e49c79844386af95e1795d83bbde45054447d90f515c96a126d85 # From internal integration: python-flask Release Integration
export SENTRY_ORG=risan-raja
export SENTRY_PROJECT=python-flask
VERSION='sentry-cli releases propose-version'
# Workflow to create releases
sentry-cli releases new "$VERSION"
sentry-cli releases set-commits "$VERSION" --auto
sentry-cli releases finalize "$VERSION"
