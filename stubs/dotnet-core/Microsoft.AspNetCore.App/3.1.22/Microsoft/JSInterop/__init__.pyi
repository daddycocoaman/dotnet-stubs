__all__ = ['Infrastructure']
from typing import Tuple, Set, Iterable, List


class DotNetObjectReference:
    def Create(value: TValue) -> DotNetObjectReference: ...




class IJSInProcessRuntime:
    def Invoke(self, identifier: str, args: Set(Object)) -> T: ...


class IJSRuntime:
    @overload
    def InvokeAsync(self, identifier: str, args: Set(Object)) -> ValueTask: ...
    @overload
    def InvokeAsync(self, identifier: str, cancellationToken: CancellationToken, args: Set(Object)) -> ValueTask: ...


class JSException:
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


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
