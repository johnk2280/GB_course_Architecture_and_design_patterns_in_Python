from dataclasses import dataclass
from project.framework.views import View


@dataclass
class Url:
    path: str
    view: View
