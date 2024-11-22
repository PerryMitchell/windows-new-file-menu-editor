import winreg as reg
import os

def add_context_menu_option(file_extension, null_file=True, template_file=None):
    """
    Adds a new file type to the Windows context menu for creating new files.

    :param file_extension: The file extension (e.g., ".txt").
    :param null_file: Whether to create a blank file. Default is True.
    :param template_file: Path to a template file. Default is None.
    """
    try:
        # Ensure the extension starts with a dot
        if not file_extension.startswith("."):
            file_extension = "." + file_extension

        # Open HKEY_CLASSES_ROOT and create the file extension key if it doesn't exist
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, file_extension) as ext_key:
            print(f"Created or opened key for {file_extension}")

        # Navigate to or create the ShellNew key under the file extension
        shell_new_path = f"{file_extension}\\ShellNew"
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, shell_new_path) as shell_new_key:
            print(f"Created or opened ShellNew key for {file_extension}")

            if null_file:
                # Add NullFile entry for blank file creation
                reg.SetValueEx(shell_new_key, "NullFile", 0, reg.REG_SZ, "")
                print("Added NullFile entry for blank file creation.")
            elif template_file:
                # Add FileName entry pointing to the template file
                if os.path.exists(template_file):
                    reg.SetValueEx(shell_new_key, "FileName", 0, reg.REG_SZ, template_file)
                    print(f"Added FileName entry pointing to {template_file}.")
                else:
                    print(f"Template file does not exist: {template_file}")
                    return False

        print(f"Successfully added {file_extension} to the context menu.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# Example Usage
if __name__ == "__main__":
    # Add .txt files with a blank template
    add_context_menu_option(".py", null_file=True)

    # Add .html files with a blank template
    add_context_menu_option(".html", null_file=True)

    # Add .docx files with a custom template
    #add_context_menu_option(".docx", null_file=False, template_file="C:\\Templates\\Template.docx")
