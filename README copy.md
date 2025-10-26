# CardCrafter

[![Docs](https://readthedocs.org/projects/CardCrafter/badge/?version=latest)](https://CardCrafter.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/jparisu/CardCrafter/actions/workflows/ci.yml/badge.svg)](https://github.com/jparisu/CardCrafter/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jparisu/CardCrafter/branch/main/graph/badge.svg)](https://codecov.io/gh/jparisu/CardCrafter)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/jparisu/CardCrafter/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)


**CardCrafter** - Scheduler for agenda and tasks orchestration via YAML

A simple yet powerful task scheduler that allows you to define and manage scheduled tasks using YAML configuration files, with a beautiful Streamlit-based web interface.

## ✨ Features

- 📝 **YAML-based Configuration**: Define tasks in simple, readable YAML format
- ⏰ **Flexible Scheduling**: Support for various schedule patterns (seconds, minutes, hours, days, weeks)
- 🎯 **Action System**: Predefined actions (print, log) with extensibility for custom actions
- 🖥️ **Web Interface**: Beautiful Streamlit-based UI for managing tasks
- 📊 **Monitoring**: Track task execution history and statistics
- 🐍 **Python API**: Programmatic access to scheduler functionality
- 🔧 **Daemon Mode**: Run as a background service with management scripts

## 🚀 Quick Start

### Installation

```bash
pip install CardCrafter
```

Or install from source:

```bash
git clone https://github.com/jparisu/CardCrafter.git
cd CardCrafter
pip install -e .
```


### Using YAML Configuration

Create a `config.yaml` file:

```yaml
tasks:
  - name: morning_greeting
    description: Print a morning greeting
    schedule: every day at 08:00
    action: print
    enabled: true
    parameters:
      message: "Good morning! Time to start the day."

  - name: hourly_check
    description: Hourly status check
    schedule: every 1 hour
    action: log
    enabled: true
    parameters:
      message: "Hourly check complete"
      level: info
```

Load and run:

```python
from CardCrafter.utils import create_scheduler_from_config

scheduler = create_scheduler_from_config("config.yaml")
scheduler.run()
```

## 📖 Documentation

Full documentation is available at [https://jparisu.github.io/CardCrafter](https://jparisu.github.io/CardCrafter)

- [Installation Guide](docs/getting-started/installation.md)
- [Quick Start](docs/getting-started/quickstart.md)
- [Configuration](docs/getting-started/configuration.md)
- [User Guide](docs/user-guide/tasks.md)

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/jparisu/CardCrafter.git
cd CardCrafter
pip install -e ".[dev,docs]"
```

### Run Tests

```bash
pytest
```

### Run Linters

```bash
ruff check .        # Linting
ruff format .       # Formatting
mypy CardCrafter app    # Type checking
codespell           # Spell checking
```

### Build Documentation

```bash
mkdocs serve
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
