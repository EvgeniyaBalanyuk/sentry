import sentry_sdk

sentry_sdk.init(
    dsn = "https://756f1d8568da3f99afbc21cc89d14e1f@o4508455814758400.ingest.de.sentry.io/4508455986790480",
    environment = "development",
    release = "1.0"
)

if __name__ == "__main__":
    division_zero = 1 / 0
