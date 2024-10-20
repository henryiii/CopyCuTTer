from __future__ import annotations

import copycutter as m
from copycutter._compat.typing import Protocol, runtime_checkable


def test_version():
    assert m.__version__


@runtime_checkable
class HasQuack(Protocol):
    def quack(self) -> str:
        ...


class Duck:
    def quack(self) -> str:
        return "quack"


def test_has_typing():
    assert isinstance(Duck(), HasQuack)
