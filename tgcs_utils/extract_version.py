import json
import sys
from dataclasses import dataclass

from cappa import command

__all__ = ["TGCSExtractVersion"]


@command(name="extract-version")
@dataclass
class TGCSExtractVersion:
    def __call__(self):
        data = json.loads(sys.stdin.read())
        print(data["release"]["version"])
