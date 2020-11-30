from abc import abstractmethod

"""
    Interface class for all the repositories search integrations
"""


class ISearchRepo:
    @abstractmethod
    def get_repositories_by_keyword(self, keyword: str = ""):
        raise NotImplementedError(
            "The calling context should instantiate a child class of IRepoSearch"
        )
