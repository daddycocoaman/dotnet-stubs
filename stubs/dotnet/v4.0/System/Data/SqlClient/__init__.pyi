from typing import Tuple, Set, Iterable, List


class SqlProviderServices(DbProviderServices):
    @property
    def SingletonInstance() -> SqlProviderServices: ...
