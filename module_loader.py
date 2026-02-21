import importlib
from typing import Dict, Any

class ModuleLoader:
    def __init__(self):
        self.loaded_modules = {}
        self.module_cache = {}

    def load_module(self, module_name: str) -> Any:
        """Load a module dynamically."""
        try:
            if module_name in self.module_cache:
                return self.module_cache[module_name]
            
            module = importlib.import_module(module_name)
            self.loaded_modules[module_name] = module
            self.module_cache[module_name] = module
            logging.info(f"Loaded module {module_name}")
            return module
            
        except Exception as e:
            logging.error(f"Failed to load module {module_name}: {str(e)}")
            raise

    def unload_module(self, module: Any) -> None:
        """Unload a module safely."""
        try:
            if hasattr(module, 'cleanup'):
                module.cleanup()
            del self.loaded_modules[module.__name__]
            logging.info(f"Unloaded module {module.__name__}")
        except Exception as e:
            logging.error(f"Failed to unload module {module.__name__}: {str(e)}")
            raise

    def reload_module(self, module_name: str) -> None:
        """Reload a previously loaded module."""
        try:
            if module_name in self.loaded_modules:
                self.unload_module(self.loaded_modules[module_name])
                self.load_module(module_name)
                logging.info(f"Reloaded module {module_name}")
        except Exception as e:
            logging.error(f"Failed to reload module {module_name}: {str(e)}")
            raise