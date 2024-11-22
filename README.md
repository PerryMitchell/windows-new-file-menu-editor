# Windows New File Menu Editor

A Python utility that adds custom file types to the Windows "New" context menu. This tool modifies the Windows Registry to enable right-click creation of new files with specified extensions.

## Features

- Add any file extension to Windows' "New" context menu
- Create blank files or use template files
- Simple API with safety checks
- Supports both administrator and non-administrator contexts
- Error handling and verbose logging

## Requirements

- Windows Operating System
- Python 3.x
- Administrator privileges (for registry modifications)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/windows-new-file-menu-editor
```

2. No additional dependencies required - uses only built-in Python libraries.

## Usage

### Basic Usage

```python
from context_menu_creator import add_context_menu_option

# Add .py files with a blank template
add_context_menu_option(".py", null_file=True)

# Add .html files with a blank template
add_context_menu_option(".html", null_file=True)

# Add .docx files with a custom template
add_context_menu_option(".docx", null_file=False, template_file="C:\\Templates\\Template.docx")
```

### Function Parameters

- `file_extension`: String - The file extension to add (with or without leading dot)
- `null_file`: Boolean - Whether to create blank files (default: True)
- `template_file`: String - Path to template file (optional)

## Security Note

This script modifies the Windows Registry. Always run with administrator privileges and be cautious when making registry modifications.

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
