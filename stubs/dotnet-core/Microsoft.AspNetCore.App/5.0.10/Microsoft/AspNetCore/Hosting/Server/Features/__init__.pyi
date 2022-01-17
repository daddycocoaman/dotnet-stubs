from typing import Tuple, Set, Iterable, List


class IServerAddressesFeature:
    @property
    def Addresses(self) -> ICollection: ...
    @property
    def PreferHostingUrls(self) -> bool: ...
    @PreferHostingUrls.setter
    def PreferHostingUrls(self, value: bool) -> None: ...
