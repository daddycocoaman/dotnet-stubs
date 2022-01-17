__all__ = ['Automation','Collections']
from typing import Tuple, Set, Iterable, List


class IContract:
    def AcquireLifetimeToken(self) -> int: ...
    def GetRemoteHashCode(self) -> int: ...
    def QueryContract(self, contractIdentifier: str) -> IContract: ...
    def RemoteEquals(self, contract: IContract) -> bool: ...
    def RemoteToString(self) -> str: ...
    def RevokeLifetimeToken(self, token: int) -> None: ...




class IExecutorExtensionContract:
    def AssemblyLoaded(self, assemblyName: str) -> None: ...
    def AssemblyLoadedFrom(self, assemblyFile: str) -> None: ...
    def AssemblyLoading(self, assemblyName: str) -> None: ...
    def AssemblyLoadingFrom(self, assemblyFile: str) -> None: ...
    def EntryPointStarted(self, entryPoint: IContract) -> None: ...
    def EntryPointStarting(self, assemblyName: str, startupClass: str, initArgs: IRemoteArgumentArrayContract) -> None: ...
    def ExecutorCreated(self) -> None: ...




class INativeHandleContract:
    def GetHandle(self) -> IntPtr: ...


class IProfferServiceContract:
    def ProfferService(self, serviceIdentifier: str, service: IServiceProviderContract) -> None: ...
    def RevokeService(self, serviceIdentifier: str) -> None: ...


class ISerializableObjectContract:
    def GetCanonicalName(self) -> str: ...
    def GetSerializableObjectData(self) -> SerializableObjectData: ...


class IServiceProviderContract:
    def QueryService(self, serviceIdentifier: str, serviceContractIdentifier: str) -> IContract: ...


class RemoteArgument(ValueType):
    @overload
    def __init__(self, value: IContract): ...
    @overload
    def __init__(self, value: UInt64): ...
    @overload
    def __init__(self, value: UInt32): ...
    @overload
    def __init__(self, value: UInt16): ...
    @overload
    def __init__(self, value: SByte): ...
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, value: Single): ...
    @overload
    def __init__(self, value: Int64): ...
    @overload
    def __init__(self, value: int): ...
    @overload
    def __init__(self, array: Array): ...
    @overload
    def __init__(self, value: float): ...
    @overload
    def __init__(self, value: Decimal): ...
    @overload
    def __init__(self, value: Int16): ...
    @overload
    def __init__(self, value: DateTime): ...
    @overload
    def __init__(self, value: Char): ...
    @overload
    def __init__(self, value: bool): ...
    @overload
    def __init__(self, value: Byte): ...
    @overload
    def __init__(self, value: DBNull): ...
    @overload
    def __init__(self, value: DBNull, isByRef: bool): ...
    @overload
    def __init__(self, value: UInt64, isByRef: bool): ...
    @overload
    def __init__(self, value: IContract, isByRef: bool): ...
    @overload
    def __init__(self, value: UInt32, isByRef: bool): ...
    @overload
    def __init__(self, remoteArgKind: RemoteArgumentKind, typeCode: TypeCode): ...
    @overload
    def __init__(self, value: UInt16, isByRef: bool): ...
    @overload
    def __init__(self, value: SByte, isByRef: bool): ...
    @overload
    def __init__(self, value: str, isByRef: bool): ...
    @overload
    def __init__(self, value: Single, isByRef: bool): ...
    @overload
    def __init__(self, value: Int64, isByRef: bool): ...
    @overload
    def __init__(self, value: Byte, isByRef: bool): ...
    @overload
    def __init__(self, value: int, isByRef: bool): ...
    @overload
    def __init__(self, value: Int16, isByRef: bool): ...
    @overload
    def __init__(self, value: Char, isByRef: bool): ...
    @overload
    def __init__(self, value: float, isByRef: bool): ...
    @overload
    def __init__(self, value: Decimal, isByRef: bool): ...
    @overload
    def __init__(self, value: DateTime, isByRef: bool): ...
    @overload
    def __init__(self, value: bool, isByRef: bool): ...
    @overload
    def __init__(self, array: Array, isByRef: bool): ...
    @overload
    def __init__(self, remoteArgKind: RemoteArgumentKind, typeCode: TypeCode, isByRef: bool): ...
    @overload
    def CreateRemoteArgument(value: Object) -> RemoteArgument: ...
    @overload
    def CreateRemoteArgument(value: Object, isByRef: bool) -> RemoteArgument: ...
    @overload
    def CreateRemoteArgument(value: Object, isByRef: bool, typeCodeToUse: TypeCode) -> RemoteArgument: ...
    @property
    def ArrayValue(self) -> Array: ...
    @property
    def BooleanValue(self) -> bool: ...
    @property
    def ByteValue(self) -> Byte: ...
    @property
    def CharValue(self) -> Char: ...
    @property
    def ContractValue(self) -> IContract: ...
    @property
    def DateTimeValue(self) -> DateTime: ...
    @property
    def DBNullValue(self) -> DBNull: ...
    @property
    def DecimalValue(self) -> Decimal: ...
    @property
    def DoubleValue(self) -> float: ...
    @property
    def Int16Value(self) -> Int16: ...
    @property
    def Int32Value(self) -> int: ...
    @property
    def Int64Value(self) -> Int64: ...
    @property
    def IsByRef(self) -> bool: ...
    @property
    def MissingValue(self) -> Missing: ...
    @property
    def RemoteArgumentKind(self) -> RemoteArgumentKind: ...
    @property
    def SByteValue(self) -> SByte: ...
    @property
    def SingleValue(self) -> Single: ...
    @property
    def StringValue(self) -> str: ...
    @property
    def TypeCode(self) -> TypeCode: ...
    @property
    def UInt16Value(self) -> UInt16: ...
    @property
    def UInt32Value(self) -> UInt32: ...
    @property
    def UInt64Value(self) -> UInt64: ...
    @ArrayValue.setter
    def ArrayValue(self, value: Array) -> None: ...
    @BooleanValue.setter
    def BooleanValue(self, value: bool) -> None: ...
    @ByteValue.setter
    def ByteValue(self, value: Byte) -> None: ...
    @CharValue.setter
    def CharValue(self, value: Char) -> None: ...
    @ContractValue.setter
    def ContractValue(self, value: IContract) -> None: ...
    @DateTimeValue.setter
    def DateTimeValue(self, value: DateTime) -> None: ...
    @DBNullValue.setter
    def DBNullValue(self, value: DBNull) -> None: ...
    @DecimalValue.setter
    def DecimalValue(self, value: Decimal) -> None: ...
    @DoubleValue.setter
    def DoubleValue(self, value: float) -> None: ...
    @Int16Value.setter
    def Int16Value(self, value: Int16) -> None: ...
    @Int32Value.setter
    def Int32Value(self, value: int) -> None: ...
    @Int64Value.setter
    def Int64Value(self, value: Int64) -> None: ...
    @IsByRef.setter
    def IsByRef(self, value: bool) -> None: ...
    @SByteValue.setter
    def SByteValue(self, value: SByte) -> None: ...
    @SingleValue.setter
    def SingleValue(self, value: Single) -> None: ...
    @StringValue.setter
    def StringValue(self, value: str) -> None: ...
    @UInt16Value.setter
    def UInt16Value(self, value: UInt16) -> None: ...
    @UInt32Value.setter
    def UInt32Value(self, value: UInt32) -> None: ...
    @UInt64Value.setter
    def UInt64Value(self, value: UInt64) -> None: ...


class RemoteArgumentKind:
    Missing = 0
    Intrinsic = 1
    IntrinsicArray = 2
    Contract = 3


class SerializableObjectData(ValueType):
    pass
