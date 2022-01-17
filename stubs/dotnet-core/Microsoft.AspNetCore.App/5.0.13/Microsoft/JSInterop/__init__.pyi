__all__ = ['Implementation','Infrastructure']
from typing import Tuple, Set, Iterable, List


class DotNetObjectReference:
    def Create(value: TValue) -> DotNetObjectReference: ...




class IJSInProcessObjectReference:
    def Invoke(self, identifier: str, args: Set(Object)) -> TValue: ...


class IJSInProcessRuntime:
    def Invoke(self, identifier: str, args: Set(Object)) -> TResult: ...


class IJSObjectReference:
    @overload
    def InvokeAsync(self, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(self, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...


class IJSRuntime:
    @overload
    def InvokeAsync(self, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(self, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...


class IJSUnmarshalledObjectReference:
    @overload
    def InvokeUnmarshalled(self, identifier: str) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0, arg1: T1) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0, arg1: T1, arg2: T2) -> TResult: ...


class IJSUnmarshalledRuntime:
    @overload
    def InvokeUnmarshalled(self, identifier: str) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0, arg1: T1) -> TResult: ...
    @overload
    def InvokeUnmarshalled(self, identifier: str, arg0: T0, arg1: T1, arg2: T2) -> TResult: ...


class JSCallResultType:
    Default = 0
    JSObjectReference = 1


class JSException:
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class JSInProcessObjectReferenceExtensions:
    def InvokeVoid(jsObjectReference: IJSInProcessObjectReference, identifier: str, args: Set(Object)) -> None: ...


class JSInProcessRuntime(JSRuntime):
    def Invoke(self, identifier: str, args: Set(Object)) -> TValue: ...


class JSInProcessRuntimeExtensions:
    def InvokeVoid(jsRuntime: IJSInProcessRuntime, identifier: str, args: Set(Object)) -> None: ...


class JSInvokableAttribute:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, identifier: str): ...
    @property
    def Identifier(self) -> str: ...


class JSObjectReferenceExtensions:
    @overload
    def InvokeAsync(jsObjectReference: IJSObjectReference, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(jsObjectReference: IJSObjectReference, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(jsObjectReference: IJSObjectReference, identifier: str, timeout: TimeSpan, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsObjectReference: IJSObjectReference, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsObjectReference: IJSObjectReference, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsObjectReference: IJSObjectReference, identifier: str, timeout: TimeSpan, args: Set(Object)) -> ValueTask: ...


class JSRuntime:
    @overload
    def InvokeAsync(self, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(self, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...


class JSRuntimeExtensions:
    @overload
    def InvokeAsync(jsRuntime: IJSRuntime, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(jsRuntime: IJSRuntime, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(jsRuntime: IJSRuntime, identifier: str, timeout: TimeSpan, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsRuntime: IJSRuntime, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsRuntime: IJSRuntime, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeVoidAsync(jsRuntime: IJSRuntime, identifier: str, timeout: TimeSpan, args: Set(Object)) -> ValueTask: ...
