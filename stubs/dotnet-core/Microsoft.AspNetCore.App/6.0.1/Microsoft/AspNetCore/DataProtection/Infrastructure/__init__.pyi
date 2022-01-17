from typing import Tuple, Set, Iterable, List


class IApplicationDiscriminator:
    @property
    def Discriminator(self) -> str: ...
