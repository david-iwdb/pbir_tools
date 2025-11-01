# pbir_tools

A Python library to create and edit PBIX files that are stored using the new PBIR format.

## Overview

`pbir_tools` provides a simple and intuitive API for working with Power BI files in the PBIR format. This format stores Power BI projects as directory structures with JSON metadata, making it easier to version control and programmatically manipulate Power BI files.

## Installation

You can install `pbir_tools` using pip:

```bash
pip install pbir_tools
```

### Development Installation

For development, you can install the package in editable mode with development dependencies:

```bash
git clone https://github.com/david-iwdb/pbir_tools.git
cd pbir_tools
pip install -e ".[dev]"
```

## Quick Start

Here's a simple example to get you started:

```python
from pbir_tools import PBIRHandler

# Create a new PBIR handler
handler = PBIRHandler()

# Create a new PBIR structure
handler.create_new(
    name="My Dashboard",
    description="A sample Power BI dashboard"
)

# Add a table to the data model
handler.add_table("Sales", [
    {"name": "OrderID", "type": "int"},
    {"name": "Date", "type": "datetime"},
    {"name": "Amount", "type": "decimal"}
])

# Save the PBIR structure
handler.save("my_dashboard")

# Load an existing PBIR structure
handler2 = PBIRHandler("my_dashboard")
info = handler2.get_info()
print(f"Loaded: {info['name']} with {info['table_count']} tables")
```

## Features

- **Create PBIR structures**: Initialize new Power BI projects programmatically
- **Load existing files**: Read and parse PBIR format files
- **Modify data models**: Add tables, columns, and relationships
- **Save changes**: Write modified structures back to disk
- **Simple API**: Easy-to-use interface for common operations

## API Reference

### PBIRHandler

The main class for working with PBIR files.

#### Methods

- `__init__(path=None)`: Initialize the handler, optionally loading from a path
- `create_new(name, description="")`: Create a new PBIR structure
- `load()`: Load PBIR metadata from the current path
- `save(output_path=None)`: Save PBIR metadata to disk
- `add_table(table_name, columns=None)`: Add a table to the data model
- `get_tables()`: Get all tables from the data model
- `get_info()`: Get general information about the PBIR file

## Example Usage

Run the included example to see the library in action:

```bash
python -m pbir_tools.pbir_handler
```

This will demonstrate:
1. Creating a new PBIR structure
2. Adding tables with columns
3. Saving the structure to disk
4. Loading it back and displaying information

## Building from Source

To package the library yourself:

```bash
# Install build tools
pip install build

# Build the package
python -m build

# This creates distribution files in the dist/ directory:
# - pbir_tools-0.1.0.tar.gz (source distribution)
# - pbir_tools-0.1.0-py3-none-any.whl (wheel distribution)
```

## Publishing to PyPI

To publish the package to PyPI:

```bash
# Install twine
pip install twine

# Upload to PyPI
python -m twine upload dist/*

# Or upload to TestPyPI first for testing
python -m twine upload --repository testpypi dist/*
```

## Requirements

- Python >= 3.8
- No external dependencies for core functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Project Status

This project is in alpha stage. The API may change in future versions.

## Links

- **GitHub Repository**: https://github.com/david-iwdb/pbir_tools
- **Issue Tracker**: https://github.com/david-iwdb/pbir_tools/issues
