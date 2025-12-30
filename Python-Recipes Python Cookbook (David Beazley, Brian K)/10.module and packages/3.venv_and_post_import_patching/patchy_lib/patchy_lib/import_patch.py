import sys
import importlib
import importlib.abc
import importlib.util


class PostImportFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        self._hooks = {}

    def register(self, name, hook):
        self._hooks.setdefault(name, []).append(hook)

    def find_spec(self, fullname, path, target=None):
        if fullname not in self._hooks:
            return None

        for finder in sys.meta_path:
            if finder is self:
                continue
            spec = finder.find_spec(fullname, path, target)
            if spec is not None:
                break
        else:
            return None

        original_loader = spec.loader
        hooks = self._hooks.pop(fullname)

        spec.loader = PostImportLoader(original_loader, hooks)
        return spec


class PostImportLoader(importlib.abc.Loader):
    def __init__(self, loader, hooks):
        self.loader = loader
        self.hooks = hooks

    def create_module(self, spec):
        if hasattr(self.loader, "create_module"):
            return self.loader.create_module(spec)
        return None

    def exec_module(self, module):
        self.loader.exec_module(module)
        for hook in self.hooks:
            hook(module)


_finder = PostImportFinder()
sys.meta_path.insert(0, _finder)


def post_import_hook(module_name):
    def decorator(func):
        if module_name in sys.modules:
            func(sys.modules[module_name])
        else:
            _finder.register(module_name, func)
        return func
    return decorator