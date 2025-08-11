# Ties 🔗

[![PyPI version](https://badge.fury.io/py/ties.svg)](https://badge.fury.io/py/ties)
[![Python versions](https://img.shields.io/pypi/pyversions/ties.svg)](https://pypi.org/project/ties/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Linting: Ruff](https://img.shields.io/badge/ruff-enabled-yellow?style=flat&labelColor=000000&logo=ruff)](https://github.com/astral-sh/ruff)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A powerful CLI tool to duplicate and sync file content with advanced
transformations. Keep your repository files in sync automatically with
intelligent content synchronization.

## ✨ Features

- **File Synchronization**: Automatically keep multiple files in sync across
  your repository
- **Advanced Transformations**: Apply custom transformations during file copying
- **Pre-commit Integration**: Enforce file consistency as part of your
  development workflow
- **Configuration-Driven**: Simple TOML-based configuration
- **Environment Variable Support**: Embed environment variables in target files
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install ties

# Or install with YAML support
pip install ties[yaml]

# Or install from source
git clone https://github.com/AlonKellner/ties.git
cd ties
pip install -e .
```

### Basic Usage

1. **Create a configuration** in your `pyproject.toml`:

```toml
[tool.ties]
[[tool.ties.tie]]
name = "gitignore sync"
source = ".gitignore"
target = "examples/.gitignore"
```

2. **Check for discrepancies**:

```bash
ties check
```

3. **Fix discrepancies automatically**:

```bash
ties fix
```

### Advanced Configuration

```toml
[tool.ties]
[[tool.ties.tie]]
name = "Environment Config"
source = ".ties/config.template"
targets = [".env.local", ".env.production"]
transform = "ties:embed_environ"

[[tool.ties.tie]]
name = "Documentation Sync"
source = "README.md"
target = "docs/README.md"
transform = "transform:markdown_cleanup"
```

## 📖 Documentation

- [User Guide](docs/user-guide.md) - Complete usage instructions
- [Configuration Reference](docs/configuration.md) - All configuration options
- [Transformations](docs/transformations.md) - Available transformation
  functions
- [Examples](docs/examples.md) - Common use cases and examples

## 🤝 Contributing

We welcome contributions! Please see our
[Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

#### Prerequisites
- [Docker](https://www.docker.com/get-started/)
- [VSCode](https://code.visualstudio.com/download)/[Cursor](https://cursor.com/downloads) (or any IDE with [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) support)

#### Steps

1. `git clone https://github.com/AlonKellner/ties.git`
2. Open the repository using VSCode/Cursor
3. `cmd+shift+p`/`ctrl+shift+p`
4. Type "reopen"
5. Choose "Dev Containers: Reopen in Container"

This will automatically:
1. Build and start a devcontainer with binary requirements
2. Install the `pre-commit` hooks
3. Use `uv` to install python and all python dependencies into a local `.venv`

## 📝 License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern Python tooling (uv, ruff, pytest)
- CI/CD powered by GitHub Actions
- Security scanning with Trivy

## 📊 Project Status

- **Development Status**: Alpha
- **Python Support**: 3.10+
- **License**: MIT
- **Maintainer**: [Alon Kellner](mailto:me@alonkellner.com)

---

## Made with ❤️ by the Ties community
