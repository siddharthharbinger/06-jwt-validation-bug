import pytest
from datetime import datetime, timedelta
from token_auth import AuthToken, TokenExpiredError


def test_valid_token_within_expiry_passes():
    now = datetime(2026, 1, 1, 12, 0, 0)
    tok = AuthToken("t1", "u1", expires_at=now + timedelta(minutes=30))
    assert tok.verify(now) is True


def test_expired_token_raises_token_expired_error():
    now = datetime(2026, 1, 1, 12, 0, 0)
    tok = AuthToken("t2", "u2", expires_at=now - timedelta(minutes=1))
    with pytest.raises(TokenExpiredError):
        tok.verify(now)
