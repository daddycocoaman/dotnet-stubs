from typing import Tuple, Set, Iterable, List


class AssemblyExtensions(Object):
    def GetExportedTypes(assembly: Assembly) -> Set(Type): ...
    def GetModules(assembly: Assembly) -> Set(Module): ...
    def GetTypes(assembly: Assembly) -> Set(Type): ...


class EventInfoExtensions(Object):
    @overload
    def GetAddMethod(eventInfo: EventInfo) -> MethodInfo: ...
    @overload
    def GetAddMethod(eventInfo: EventInfo, nonPublic: bool) -> MethodInfo: ...
    @overload
    def GetRaiseMethod(eventInfo: EventInfo) -> MethodInfo: ...
    @overload
    def GetRaiseMethod(eventInfo: EventInfo, nonPublic: bool) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(eventInfo: EventInfo) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(eventInfo: EventInfo, nonPublic: bool) -> MethodInfo: ...


class MemberInfoExtensions(Object):
    def GetMetadataToken(member: MemberInfo) -> int: ...
    def HasMetadataToken(member: MemberInfo) -> bool: ...


class MethodInfoExtensions(Object):
    def GetBaseDefinition(method: MethodInfo) -> MethodInfo: ...


class ModuleExtensions(Object):
    def GetModuleVersionId(module: Module) -> Guid: ...
    def HasModuleVersionId(module: Module) -> bool: ...


class PropertyInfoExtensions(Object):
    @overload
    def GetAccessors(property: PropertyInfo) -> Set(MethodInfo): ...
    @overload
    def GetAccessors(property: PropertyInfo, nonPublic: bool) -> Set(MethodInfo): ...
    @overload
    def GetGetMethod(property: PropertyInfo) -> MethodInfo: ...
    @overload
    def GetGetMethod(property: PropertyInfo, nonPublic: bool) -> MethodInfo: ...
    @overload
    def GetSetMethod(property: PropertyInfo) -> MethodInfo: ...
    @overload
    def GetSetMethod(property: PropertyInfo, nonPublic: bool) -> MethodInfo: ...


class TypeExtensions(Object):
    def GetConstructor(type: Type, types: Set(Type)) -> ConstructorInfo: ...
    @overload
    def GetConstructors(type: Type) -> Set(ConstructorInfo): ...
    @overload
    def GetConstructors(type: Type, bindingAttr: BindingFlags) -> Set(ConstructorInfo): ...
    def GetDefaultMembers(type: Type) -> Set(MemberInfo): ...
    @overload
    def GetEvent(type: Type, name: str) -> EventInfo: ...
    @overload
    def GetEvent(type: Type, name: str, bindingAttr: BindingFlags) -> EventInfo: ...
    @overload
    def GetEvents(type: Type) -> Set(EventInfo): ...
    @overload
    def GetEvents(type: Type, bindingAttr: BindingFlags) -> Set(EventInfo): ...
    @overload
    def GetField(type: Type, name: str) -> FieldInfo: ...
    @overload
    def GetField(type: Type, name: str, bindingAttr: BindingFlags) -> FieldInfo: ...
    @overload
    def GetFields(type: Type) -> Set(FieldInfo): ...
    @overload
    def GetFields(type: Type, bindingAttr: BindingFlags) -> Set(FieldInfo): ...
    def GetGenericArguments(type: Type) -> Set(Type): ...
    def GetInterfaces(type: Type) -> Set(Type): ...
    @overload
    def GetMember(type: Type, name: str) -> Set(MemberInfo): ...
    @overload
    def GetMember(type: Type, name: str, bindingAttr: BindingFlags) -> Set(MemberInfo): ...
    @overload
    def GetMembers(type: Type) -> Set(MemberInfo): ...
    @overload
    def GetMembers(type: Type, bindingAttr: BindingFlags) -> Set(MemberInfo): ...
    @overload
    def GetMethod(type: Type, name: str) -> MethodInfo: ...
    @overload
    def GetMethod(type: Type, name: str, bindingAttr: BindingFlags) -> MethodInfo: ...
    @overload
    def GetMethod(type: Type, name: str, types: Set(Type)) -> MethodInfo: ...
    @overload
    def GetMethods(type: Type) -> Set(MethodInfo): ...
    @overload
    def GetMethods(type: Type, bindingAttr: BindingFlags) -> Set(MethodInfo): ...
    def GetNestedType(type: Type, name: str, bindingAttr: BindingFlags) -> Type: ...
    def GetNestedTypes(type: Type, bindingAttr: BindingFlags) -> Set(Type): ...
    @overload
    def GetProperties(type: Type) -> Set(PropertyInfo): ...
    @overload
    def GetProperties(type: Type, bindingAttr: BindingFlags) -> Set(PropertyInfo): ...
    @overload
    def GetProperty(type: Type, name: str) -> PropertyInfo: ...
    @overload
    def GetProperty(type: Type, name: str, bindingAttr: BindingFlags) -> PropertyInfo: ...
    @overload
    def GetProperty(type: Type, name: str, returnType: Type) -> PropertyInfo: ...
    @overload
    def GetProperty(type: Type, name: str, returnType: Type, types: Set(Type)) -> PropertyInfo: ...
    def IsAssignableFrom(type: Type, c: Type) -> bool: ...
    def IsInstanceOfType(type: Type, o: Object) -> bool: ...
