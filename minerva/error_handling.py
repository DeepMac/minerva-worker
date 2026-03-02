from random import random

import httpx

from minerva.constants import RETRIABLE_STATUS_CODES


def _retryable_status(code: int) -> bool:
    return code in RETRIABLE_STATUS_CODES


def _retry_sleep(attempt: int, cap: float = 25.0) -> float:
    return min(cap, (0.85 * attempt) + random() * 1.25)


def _raise_if_upgrade_required(resp: httpx.Response) -> None:
    if resp.status_code == 426:
        try:
            detail = resp.json().get("detail")
        except Exception:
            detail = resp.text.strip() or "Worker update required"
        raise RuntimeError(detail)


__all__ = ["_retryable_status", "_retry_sleep", "_raise_if_upgrade_required"]
