from typing import Tuple, Set, Iterable, List


class X509Certificate2UI(Object):
    @overload
    def DisplayCertificate(certificate: X509Certificate2) -> None: ...
    @overload
    def DisplayCertificate(certificate: X509Certificate2, hwndParent: IntPtr) -> None: ...
    @overload
    def SelectFromCollection(certificates: X509Certificate2Collection, title: str, message: str, selectionFlag: X509SelectionFlag) -> X509Certificate2Collection: ...
    @overload
    def SelectFromCollection(certificates: X509Certificate2Collection, title: str, message: str, selectionFlag: X509SelectionFlag, hwndParent: IntPtr) -> X509Certificate2Collection: ...


class X509SelectionFlag:
    SingleSelection = 0
    MultiSelection = 1
