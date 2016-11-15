import os
import subprocess

import dotbot

class Rust(dotbot.Plugin):
    def __init__(self, context):
        super(Rust, self).__init__(context)
        self._directives = {
            'rust': self._handle_rust,
            'cargo': self._handle_cargo
        }

    def can_handle(self, directive):
        return directive in self._directives

    def handle(self, directive, data):
        try:
            self._log.info('Handling directive: {}'.format(directive))
            return self._directives[directive](data)
        except KeyError:
            raise ValueError('Shell cannot handle directive {}'.format(directive))

    def _handle_rust(self, data):
        self._log.info('Handling Rust toolchain: {}'.format(data))
        return False

    def _handle_cargo(self, data):
        self._log.info('Handling Rust binary: {}'.format(data))

        success = True
        with open(os.devnull, 'w') as devnull:
            for item in data:
                if isinstance(item, str):
                    args = ''
                    binary = item
                else:
                    success = False
                    self._log.warning('Invalid cargo command: {}'.format(data))

                cmd = ' '.join('cargo install {} {}'.format(args, binary).split())
                self._log.info('Installing Rust binary: {} [{}]'.format(binary, cmd))
                ret = subprocess.call(cmd, shell=True, stdin=devnull, stdout=devnull, stderr=devnull, cwd=self._context.base_directory())
                if ret != 0:
                    success = False
                    self._log.warning('Rust binary {} could not be installed'.format(binary))

        if success:
            self._log.info('All Rust binaries have been installed')
        else:
            self._log.error('Some Rust binaries were not successfully installed')

        return success
