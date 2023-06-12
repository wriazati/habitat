from abc import ABC, abstractmethod


class AbstractDownloader(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def download(self):
        raise NotImplementedError
