from typing import Tuple, Set, Iterable, List


class ADVF:
    ADVF_NODATA = 1
    ADVF_PRIMEFIRST = 2
    ADVF_ONLYONCE = 4
    ADVFCACHE_NOHANDLER = 8
    ADVFCACHE_FORCEBUILTIN = 16
    ADVFCACHE_ONSAVE = 32
    ADVF_DATAONSTOP = 64


class DATADIR:
    DATADIR_GET = 1
    DATADIR_SET = 2


class DVASPECT:
    DVASPECT_CONTENT = 1
    DVASPECT_THUMBNAIL = 2
    DVASPECT_ICON = 4
    DVASPECT_DOCPRINT = 8


class FORMATETC(ValueType):
    pass


class IAdviseSink:
    def OnClose(self) -> None: ...
    def OnDataChange(self, format: FORMATETC, stgmedium: STGMEDIUM) -> Tuple[FORMATETC, STGMEDIUM]: ...
    def OnRename(self, moniker: IMoniker) -> None: ...
    def OnSave(self) -> None: ...
    def OnViewChange(self, aspect: int, index: int) -> None: ...


class IDataObject:
    def DAdvise(self, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink) -> Tuple[int, FORMATETC, int]: ...
    def DUnadvise(self, connection: int) -> None: ...
    def EnumDAdvise(self) -> Tuple[int, IEnumSTATDATA]: ...
    def EnumFormatEtc(self, direction: DATADIR) -> IEnumFORMATETC: ...
    def GetCanonicalFormatEtc(self, formatIn: FORMATETC) -> Tuple[int, FORMATETC, FORMATETC]: ...
    def GetData(self, format: FORMATETC) -> Tuple[FORMATETC, STGMEDIUM]: ...
    def GetDataHere(self, format: FORMATETC, medium: STGMEDIUM) -> Tuple[FORMATETC, STGMEDIUM]: ...
    def QueryGetData(self, format: FORMATETC) -> Tuple[int, FORMATETC]: ...
    def SetData(self, formatIn: FORMATETC, medium: STGMEDIUM, release: bool) -> Tuple[FORMATETC, STGMEDIUM]: ...


class IEnumFORMATETC:
    def Clone(self) -> Tuple[IEnumFORMATETC]: ...
    def Next(self, celt: int) -> Tuple[int, Set(FORMATETC), Set(int)]: ...
    def Reset(self) -> int: ...
    def Skip(self, celt: int) -> int: ...


class IEnumSTATDATA:
    def Clone(self) -> Tuple[IEnumSTATDATA]: ...
    def Next(self, celt: int) -> Tuple[int, Set(STATDATA), Set(int)]: ...
    def Reset(self) -> int: ...
    def Skip(self, celt: int) -> int: ...


class STATDATA(ValueType):
    pass


class STGMEDIUM(ValueType):
    pass


class TYMED:
    TYMED_NULL = 0
    TYMED_HGLOBAL = 1
    TYMED_FILE = 2
    TYMED_ISTREAM = 4
    TYMED_ISTORAGE = 8
    TYMED_GDI = 16
    TYMED_MFPICT = 32
    TYMED_ENHMF = 64
