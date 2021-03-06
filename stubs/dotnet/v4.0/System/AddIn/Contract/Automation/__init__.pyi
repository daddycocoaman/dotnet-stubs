from typing import Tuple, Set, Iterable, List


class IRemoteDelegateContract:
    def InvokeDelegate(self, args: IRemoteArgumentArrayContract) -> RemoteArgument: ...


class IRemoteEventInfoContract:
    def GetAddMethod(self) -> IRemoteMethodInfoContract: ...
    def GetMemberData(self) -> RemoteMemberData: ...
    def GetRemoveMethod(self) -> IRemoteMethodInfoContract: ...


class IRemoteFieldInfoContract:
    def GetFieldData(self) -> RemoteFieldData: ...
    def GetValue(self, obj: IRemoteObjectContract) -> RemoteArgument: ...
    def SetValue(self, obj: IRemoteObjectContract, value: RemoteArgument, localeId: int) -> None: ...


class IRemoteMethodInfoContract:
    def GetMethodData(self) -> RemoteMethodData: ...
    def Invoke(self, target: IRemoteObjectContract, bindingFlags: BindingFlags, parameters: IRemoteArgumentArrayContract, localeId: int) -> RemoteArgument: ...


class IRemoteObjectContract:
    def GetRemoteType(self) -> IRemoteTypeContract: ...
    def RemoteCast(self, canonicalName: str) -> RemoteArgument: ...


class IRemotePropertyInfoContract:
    def GetGetMethod(self) -> IRemoteMethodInfoContract: ...
    def GetPropertyData(self) -> RemotePropertyData: ...
    def GetSetMethod(self) -> IRemoteMethodInfoContract: ...
    def GetValue(self, obj: IRemoteObjectContract, bindingFlags: BindingFlags, index: IRemoteArgumentArrayContract, localeId: int) -> RemoteArgument: ...
    def SetValue(self, target: IRemoteObjectContract, value: RemoteArgument, bindingFlags: BindingFlags, index: IRemoteArgumentArrayContract, localeId: int) -> Tuple[RemoteArgument]: ...


class IRemoteTypeContract:
    def GetCanonicalName(self) -> str: ...
    def GetEvent(self, name: str, bindingFlags: BindingFlags) -> IRemoteEventInfoContract: ...
    def GetEvents(self, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetField(self, name: str, bindingFlags: BindingFlags) -> IRemoteFieldInfoContract: ...
    def GetFields(self, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetInterface(self, canonicalName: str) -> IRemoteTypeContract: ...
    def GetInterfaces(self) -> IArrayContract: ...
    def GetMember(self, name: str, memberTypes: MemberTypes, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetMembers(self, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetMethod(self, name: str, bindingFlags: BindingFlags, remoteTypes: IArrayContract) -> IRemoteMethodInfoContract: ...
    def GetMethods(self, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetProperties(self, bindingFlags: BindingFlags) -> IArrayContract: ...
    def GetProperty(self, name: str, bindingFlags: BindingFlags, remoteReturnType: IRemoteTypeContract, remoteTypes: IArrayContract) -> IRemotePropertyInfoContract: ...
    def GetTypeData(self) -> RemoteTypeData: ...
    def InvokeMember(self, name: str, bindingFlags: BindingFlags, target: IRemoteObjectContract, remoteArgs: IRemoteArgumentArrayContract, remoteArgModifiers: Set(bool), localeId: int) -> RemoteArgument: ...


class RemoteFieldData(ValueType):
    pass


class RemoteMemberData(ValueType):
    pass


class RemoteMethodData(ValueType):
    pass


class RemoteParameterData(ValueType):
    pass


class RemotePropertyData(ValueType):
    pass


class RemoteTypeData(ValueType):
    pass
