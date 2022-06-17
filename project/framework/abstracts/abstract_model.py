from abc import ABC
from typing import List


class Model(ABC):

    def get_all(self) -> List[str]:
        pass

    def save(self) -> None:
        pass

