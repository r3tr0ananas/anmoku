from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import List, Optional, Literal

from dataclasses import dataclass, field

__all__ = ("Title",)

class TitleData(TypedDict):
    type: Literal["Default", "Synonym", "Japanese", "English", "German", "Spanish", "French"]
    title: str

@dataclass(repr = False)
class Title():
    """A jikan title object."""
    data: List[TitleData] = field(repr = False)

    default: str = field(init = False)
    """The default title."""
    english: Optional[str] = field(init = False)
    """The english title."""
    japanese: Optional[str] = field(init = False)
    """The japanese title."""
    synonyms: List[str] = field(init = False)
    """A list of synonym titles."""

    def __post_init__(self):
        self.synonyms = []

        for title in self.data:

            if title["type"] == "Default":
                self.default = title["title"]
            elif title["type"] == "English":
                self.english = title["title"]
            elif title["type"] == "Japanese":
                self.japanese = title["title"]
            elif title["type"] == "Synonym":
                self.synonyms.append(title["title"])

    def __str__(self) -> str:
        return [title["title"] for title in self.data if title["type"] == "Default"][0]