from dataclasses import dataclass
from framework.views import View


@dataclass
class Url:
    path: str
    view: View
