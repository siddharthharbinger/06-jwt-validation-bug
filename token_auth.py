from dataclasses import dataclass
from datetime import datetime


class TokenExpiredError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


@dataclass
class AuthToken:
    token_id: str
    user_id: str
    expires_at: datetime

    def verify(self, current_time: datetime) -> bool:
        """Verify token is valid and not expired."""
        # Bug: comparison is inverted; rejects valid unexpired tokens when current_time < expires_at
        if current_time < self.expires_at:
            raise TokenExpiredError("Token has expired")
        return True
