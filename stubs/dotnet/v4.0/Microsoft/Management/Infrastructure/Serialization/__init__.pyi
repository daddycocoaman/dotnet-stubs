from typing import Tuple, Set, Iterable, List


class CimDeserializer:
    @overload
    def Create() -> CimDeserializer: ...
    @overload
    def Create(format: str, flags: UInt32) -> CimDeserializer: ...
    @overload
    def DeserializeClass(self, serializedData: Set(Byte), offset: UInt32) -> Tuple[CimClass, UInt32]: ...
    @overload
    def DeserializeClass(self, serializedData: Set(Byte), offset: UInt32, parentClass: CimClass) -> Tuple[CimClass, UInt32]: ...
    @overload
    def DeserializeClass(self, serializedData: Set(Byte), offset: UInt32, parentClass: CimClass, computerName: str, namespaceName: str) -> Tuple[CimClass, UInt32]: ...
    @overload
    def DeserializeInstance(self, serializedData: Set(Byte), offset: UInt32) -> Tuple[CimInstance, UInt32]: ...
    @overload
    def DeserializeInstance(self, serializedData: Set(Byte), offset: UInt32, cimClasses: Iterable[CimClass]) -> Tuple[CimInstance, UInt32]: ...
    def Dispose(self) -> None: ...


class CimSerializer:
    @overload
    def Create() -> CimSerializer: ...
    @overload
    def Create(format: str, flags: UInt32) -> CimSerializer: ...
    def Dispose(self) -> None: ...
    @overload
    def Serialize(self, cimInstance: CimInstance, options: InstanceSerializationOptions) -> Set(Byte): ...
    @overload
    def Serialize(self, cimClass: CimClass, options: ClassSerializationOptions) -> Set(Byte): ...
    @overload
    def Serialize(self, cimInstance: CimInstance, options: InstanceSerializationOptions, buffer: Set(Byte), offset: UInt32) -> Tuple[bool, UInt32]: ...
    @overload
    def Serialize(self, cimClass: CimClass, options: ClassSerializationOptions, buffer: Set(Byte), offset: UInt32) -> Tuple[bool, UInt32]: ...


class ClassSerializationOptions:
    #None = 0
    IncludeParentClasses = 1


class InstanceSerializationOptions:
    #None = 0
    IncludeClasses = 1
