import dotbot

class Rust(dotbot.Plugin):
    def __init__(self, context):
        _directives = {
            "rust": self._handle_rust,
            "cargo": self._handle_cargo
        }

    def can_handle(self, directive):
        return directive in self._directives

    def handle(self, directive, data):
        try:
            return self._directives[directive](data)
        except KeyError:
            return False

    def _handle_rust(self, data):
        self._log.info("Handling Rust toolchain: {}".format(data))
        return False

    def _handle_cargo(self, data):
        self._log.info("Handling Cargo package: {}".format(data))
        return False