from typing import Tuple, Set, Iterable, List


class AppDomainData:
    pass


class AppDomainStoreData:
    pass


class AssemblyData:
    pass


class CcwData:
    pass


class ClrDataAddress:
    def __init__(self, value: Int64): ...
    @property
    def Value(self) -> Int64: ...
    @overload
    def op_Implicit(cda: ClrDataAddress) -> UInt64: ...
    @overload
    def op_Implicit(value: UInt64) -> ClrDataAddress: ...


class ClrDataMethod(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnk: IntPtr): ...
    def GetILToNativeMap(self) -> Set(ILToNativeMap): ...


class ClrDataModule(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnknown: IntPtr): ...
    def GetFileName(self) -> str: ...
    def GetModuleData(self) -> Tuple[HResult, ExtendedModuleData]: ...
    def GetName(self) -> str: ...


class ClrDataProcess(CallableCOMWrapper):
    @overload
    def __init__(self, library: DacLibrary, pUnknown: IntPtr): ...
    @overload
    def __init__(self, library: DacLibrary, toClone: CallableCOMWrapper): ...
    def CreateStackWalk(self, id: UInt32, flags: UInt32) -> ClrStackWalk: ...
    def EnumerateMethodInstancesByAddress(self, addr: ClrDataAddress) -> Iterable[ClrDataMethod]: ...
    def Flush(self) -> None: ...
    def GetSOSDacInterface(self) -> SOSDac: ...
    def GetSOSDacInterface6(self) -> SOSDac6: ...
    def GetSOSDacInterface8(self) -> SOSDac8: ...
    def Request(self, reqCode: UInt32, input: ReadOnlySpan, output: Span) -> HResult: ...


class ClrStackWalk(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnk: IntPtr): ...
    def GetContext(self, contextFlags: UInt32, contextBufSize: int, buffer: Set(Byte)) -> Tuple[HResult, int]: ...
    def GetFrameVtable(self) -> ClrDataAddress: ...
    def Next(self) -> HResult: ...


class CodeHeaderData:
    pass


class CodeHeapType:
    Loader = 0
    Host = 1
    Unknown = 2


class COMInterfacePointerData:
    pass


class CommonMethodTables:
    pass


class DomainLocalModuleData:
    pass


class ExtendedModuleData:
    pass


class FieldData:
    pass


class FieldInfo:
    pass


class GCInfo:
    pass


class GenerationData:
    pass


class HandleData:
    pass


class HeapDetails:
    @property
    def EphemeralAllocContextLimit(self) -> UInt64: ...
    @property
    def EphemeralAllocContextPtr(self) -> UInt64: ...
    @property
    def FQAllObjectsStart(self) -> UInt64: ...
    @property
    def FQAllObjectsStop(self) -> UInt64: ...
    @property
    def FQRootsStart(self) -> UInt64: ...
    @property
    def FQRootsStop(self) -> UInt64: ...


class JitCodeHeapInfo:
    pass


class JitManagerInfo:
    pass


class LoaderHeapTraverse:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, address: UInt64, size: IntPtr, isCurrent: int, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, address: UInt64, size: IntPtr, isCurrent: int) -> None: ...


class MetadataImport(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnknown: IntPtr): ...
    def EnumerateFields(self, token: int) -> Iterable[int]: ...
    def EnumerateGenericParams(self, token: int) -> Iterable[int]: ...
    def EnumerateInterfaceImpls(self, token: int) -> Iterable[int]: ...
    def GetCustomAttributeByName(self, token: int, name: str) -> Tuple[HResult, IntPtr, UInt32]: ...
    def GetFieldProps(self, token: int) -> Tuple[HResult, str, FieldAttributes, IntPtr, int, int, IntPtr]: ...
    def GetGenericParamProps(self, token: int) -> Tuple[bool, int, GenericParameterAttributes, str]: ...
    def GetInterfaceImplProps(self, token: int) -> Tuple[HResult, int, int]: ...
    def GetMethodAttributes(self, token: int) -> MethodAttributes: ...
    def GetNestedClassProperties(self, token: int) -> Tuple[HResult, int]: ...
    def GetRva(self, token: int) -> UInt32: ...
    def GetSigFromToken(self, token: int) -> SigParser: ...
    def GetTypeDefProperties(self, token: int) -> Tuple[HResult, str, TypeAttributes, int]: ...
    def GetTypeRefName(self, token: int) -> str: ...


class MethodDescData:
    pass


class MethodTableCollectibleData:
    pass


class MethodTableData:
    pass


class ModuleData:
    pass


class ModuleMapTraverse:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, index: int, methodTable: UInt64, token: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, index: int, methodTable: UInt64, token: IntPtr) -> None: ...


class ModuleMapTraverseKind:
    TypeDefToMethodTable = 0
    TypeRefToMethodTable = 1


class ObjectData:
    pass


class RcwData:
    pass


class RejitData:
    pass


class SegmentData:
    pass


class SOSDac(CallableCOMWrapper):
    @overload
    def __init__(self, library: DacLibrary, ptr: IntPtr): ...
    @overload
    def __init__(self, lib: DacLibrary, toClone: CallableCOMWrapper): ...
    @overload
    def EnumerateHandles(self) -> SOSHandleEnum: ...
    @overload
    def EnumerateHandles(self, types: Set(ClrHandleKind)) -> SOSHandleEnum: ...
    def EnumerateStackRefs(self, osThreadId: UInt32) -> SOSStackRefEnum: ...
    def GetAppBase(self, domain: UInt64) -> str: ...
    def GetAppDomainData(self, addr: UInt64) -> Tuple[HResult, AppDomainData]: ...
    def GetAppDomainList(self, count: int) -> Set(ClrDataAddress): ...
    def GetAppDomainName(self, appDomain: UInt64) -> str: ...
    def GetAppDomainStoreData(self) -> Tuple[HResult, AppDomainStoreData]: ...
    def GetAssemblyData(self, domain: UInt64, assembly: UInt64) -> Tuple[HResult, AssemblyData]: ...
    @overload
    def GetAssemblyList(self, appDomain: UInt64) -> Set(ClrDataAddress): ...
    @overload
    def GetAssemblyList(self, appDomain: UInt64, count: int) -> Set(ClrDataAddress): ...
    def GetAssemblyName(self, assembly: UInt64) -> str: ...
    def GetCCWData(self, ccw: UInt64) -> Tuple[HResult, CcwData]: ...
    def GetCCWInterfaces(self, ccw: UInt64, count: int) -> Set(COMInterfacePointerData): ...
    def GetClrDataModule(self, module: UInt64) -> ClrDataModule: ...
    def GetCodeHeaderData(self, ip: UInt64) -> Tuple[HResult, CodeHeaderData]: ...
    def GetCodeHeapList(self, jitManager: UInt64) -> Set(JitCodeHeapInfo): ...
    def GetCommonMethodTables(self) -> Tuple[HResult, CommonMethodTables]: ...
    def GetConfigFile(self, domain: UInt64) -> str: ...
    def GetDomainLocalModuleDataFromAppDomain(self, appDomain: UInt64, id: int) -> Tuple[HResult, DomainLocalModuleData]: ...
    def GetDomainLocalModuleDataFromModule(self, module: UInt64) -> Tuple[HResult, DomainLocalModuleData]: ...
    def GetFieldData(self, fieldDesc: UInt64) -> Tuple[HResult, FieldData]: ...
    def GetFieldInfo(self, mt: UInt64) -> Tuple[HResult, FieldInfo]: ...
    def GetFrameName(self, vtable: UInt64) -> str: ...
    def GetGCHeapData(self) -> Tuple[HResult, GCInfo]: ...
    def GetHeapList(self, heapCount: int) -> Set(ClrDataAddress): ...
    def GetILForModule(self, moduleAddr: UInt64, rva: UInt32) -> UInt64: ...
    def GetJitHelperFunctionName(self, addr: UInt64) -> str: ...
    def GetJitManagers(self) -> Set(JitManagerInfo): ...
    def GetMetadataImport(self, module: UInt64) -> MetadataImport: ...
    def GetMethodDescData(self, md: UInt64, ip: UInt64) -> Tuple[HResult, MethodDescData]: ...
    def GetMethodDescFromToken(self, module: UInt64, token: int) -> UInt64: ...
    def GetMethodDescName(self, md: UInt64) -> str: ...
    def GetMethodDescPtrFromFrame(self, frame: UInt64) -> ClrDataAddress: ...
    def GetMethodDescPtrFromIP(self, frame: UInt64) -> ClrDataAddress: ...
    def GetMethodTableByEEClass(self, eeclass: UInt64) -> ClrDataAddress: ...
    def GetMethodTableData(self, addr: UInt64) -> Tuple[HResult, MethodTableData]: ...
    def GetMethodTableName(self, mt: UInt64) -> str: ...
    def GetMethodTableSlot(self, mt: UInt64, slot: UInt32) -> UInt64: ...
    def GetModuleData(self, module: UInt64) -> Tuple[HResult, ModuleData]: ...
    @overload
    def GetModuleList(self, assembly: UInt64) -> Set(ClrDataAddress): ...
    @overload
    def GetModuleList(self, assembly: UInt64, count: int) -> Set(ClrDataAddress): ...
    def GetObjectData(self, obj: UInt64) -> Tuple[HResult, ObjectData]: ...
    def GetPEFileName(self, pefile: UInt64) -> str: ...
    def GetRCWData(self, rcw: UInt64) -> Tuple[HResult, RcwData]: ...
    def GetRCWInterfaces(self, ccw: UInt64, count: int) -> Set(COMInterfacePointerData): ...
    def GetRejitData(self, md: UInt64, ip: UInt64) -> Set(RejitData): ...
    def GetSegmentData(self, addr: UInt64) -> Tuple[HResult, SegmentData]: ...
    def GetServerHeapDetails(self, addr: UInt64) -> Tuple[HResult, HeapDetails]: ...
    def GetSyncBlockData(self, index: int) -> Tuple[HResult, SyncBlockData]: ...
    def GetThreadData(self, address: UInt64) -> Tuple[HResult, ThreadData]: ...
    def GetThreadFromThinlockId(self, id: UInt32) -> ClrDataAddress: ...
    def GetThreadLocalModuleData(self, thread: UInt64, index: UInt32) -> Tuple[HResult, ThreadLocalModuleData]: ...
    def GetThreadPoolData(self) -> Tuple[HResult, ThreadPoolData]: ...
    def GetThreadStoreData(self) -> Tuple[HResult, ThreadStoreData]: ...
    def GetTlsIndex(self) -> UInt32: ...
    def GetWksHeapDetails(self) -> Tuple[HResult, HeapDetails]: ...
    def GetWorkRequestData(self, request: UInt64) -> Tuple[HResult, WorkRequestData]: ...
    def TraverseLoaderHeap(self, heap: UInt64, callback: LoaderHeapTraverse) -> HResult: ...
    def TraverseModuleMap(self, mt: ModuleMapTraverseKind, module: UInt64, traverse: ModuleMapTraverse) -> HResult: ...
    def TraverseStubHeap(self, heap: UInt64, type: int, callback: LoaderHeapTraverse) -> HResult: ...


class SOSDac6(CallableCOMWrapper):
    @overload
    def __init__(self, toClone: CallableCOMWrapper): ...
    @overload
    def __init__(self, library: DacLibrary, ptr: IntPtr): ...
    def GetMethodTableCollectibleData(self, mt: UInt64) -> Tuple[HResult, MethodTableCollectibleData]: ...


class SOSDac8(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, ptr: IntPtr): ...
    @property
    def GenerationCount(self) -> int: ...
    def GetAssemblyLoadContext(self, methodTable: ClrDataAddress) -> Tuple[HResult, ClrDataAddress]: ...
    @overload
    def GetFinalizationFillPointers(self) -> Set(ClrDataAddress): ...
    @overload
    def GetFinalizationFillPointers(self, heap: UInt64) -> Set(ClrDataAddress): ...
    @overload
    def GetGenerationTable(self) -> Set(GenerationData): ...
    @overload
    def GetGenerationTable(self, heap: UInt64) -> Set(GenerationData): ...


class SOSHandleEnum(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnk: IntPtr): ...
    def ReadHandles(self, handles: Span) -> int: ...


class SOSStackRefEnum(CallableCOMWrapper):
    def __init__(self, library: DacLibrary, pUnk: IntPtr): ...
    def ReadStackReferences(self, stackRefs: Span) -> int: ...


class StackRefData:
    pass


class SyncBlockData:
    pass


class ThreadData:
    pass


class ThreadLocalModuleData:
    pass


class ThreadPoolData:
    pass


class ThreadStoreData:
    pass


class WorkRequestData:
    pass