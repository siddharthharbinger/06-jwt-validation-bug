from datetime import datetime, timedelta
from token_auth import AuthToken, TokenExpiredError

now = datetime(2026, 1, 1, 12, 0, 0)
future_expiry = now + timedelta(hours=1)
token = AuthToken(token_id="tok_abc", user_id="usr_99", expires_at=future_expiry)

try:
    token.verify(now)
    print("Token verified successfully.")
    raise SystemExit(0)
except TokenExpiredError as exc:
    print(f"BUG DETECTED: Valid unexpired token rejected with error: {exc}")
    raise SystemExit(1)
