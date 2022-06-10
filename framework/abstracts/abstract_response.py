from abc import ABC
from abc import abstractmethod


class AbstractResponse(ABC):

    @abstractmethod
    def _get_headers(self, user_headers: dict) -> dict:
        pass
