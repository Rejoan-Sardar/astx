"""ASTx Data Types module."""

from __future__ import annotations

from public import public
from typeguard import typechecked

from astx.types.base import AnyType


@public
@typechecked
class UTF8String(AnyType):
    """Class for UTF-8 encoded strings."""


@public
@typechecked
class UTF8Char(AnyType):
    """Class for UTF-8 encoded characters."""
