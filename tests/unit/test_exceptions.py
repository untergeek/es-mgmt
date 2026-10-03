"""Exception hierarchy tests."""

from __future__ import annotations

from es_mgmt.exceptions import ESMgmtActionError, ESMgmtException


def test_action_error_is_shared() -> None:
    """ESMgmtActionError is a shared list-action error."""
    assert issubclass(ESMgmtActionError, ESMgmtException)
