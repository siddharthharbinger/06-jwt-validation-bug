# JWT Validation Bug

High-level bug: `AuthToken.verify` contains an inverted comparison check (`if current_time < self.expires_at:` raises `TokenExpiredError`), causing brand-new and unexpired tokens to be erroneously rejected as expired, while expired tokens incorrectly pass validation.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: Calling `token.verify(now)` on a token expiring 1 hour in the future should return `True`, but the buggy implementation raises `TokenExpiredError`.
