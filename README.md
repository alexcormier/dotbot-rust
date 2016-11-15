# Dotbot Rust Plugin

This is a plugin for [Dotbot][dotbot] that handles installing [Rust][rust].
It also allows the installation other [rustup][rustup] components, as well as other Rust software with [Cargo][cargo].

## Installation

Add this repository as submodule to your repository:
```bash
git submodule add https://github.com/alexcormier/dotbot-rust
```

## Usage

Modify your `install` script to load this plugin, as follows:
```bash
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -p dotbot-rust/rust.py -d "${BASEDIR}" -c "${CONFIG}" "${@}"
```
For an example of more advanced usage, with multiple plugins, see [my dotfiles][dotfiles].

## Configuration

None yet...

[dotbot]: https://github.com/anishathalye/dotbot
[rust]: https://www.rust-lang.org/
[rustup]: https://rustup.rs/
[cargo]: http://doc.crates.io/
[dotfiles]: https://github.com/alexcormier/dotfiles
