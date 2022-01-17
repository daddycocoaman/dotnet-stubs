from typing import Tuple, Set, Iterable, List


class WindowsFormsComponentEditor(ComponentEditor):
    @overload
    def EditComponent(self, context: ITypeDescriptorContext, component: Object) -> bool: ...
    @overload
    def EditComponent(self, component: Object, owner: IWin32Window) -> bool: ...
    @overload
    def EditComponent(self, context: ITypeDescriptorContext, component: Object, owner: IWin32Window) -> bool: ...
