__all__ = ['Implementation','Implementation','Infrastructure','Infrastructure','Infrastructure']
from typing import Tuple, Set, Iterable, List


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