from abc import ABC
from abc import abstractmethod


class AbstractRequest(ABC):

    @abstractmethod
    def _get_headers(self, environ: dict) -> dict:
        pass

    @abstractmethod
    def _get_query_params(self, environ: dict) -> dict:
        pass
