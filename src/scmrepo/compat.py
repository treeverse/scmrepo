import sys
from typing import TYPE_CHECKING

if sys.version_info >= (3, 12) or TYPE_CHECKING:
    from functools import cached_property  # noqa: TID251
else:
    from funcy import cached_property  # noqa: TID251

__all__ = ["cached_property"]
