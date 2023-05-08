import inspect
import os
import sys
import nbformat


def main():
    # Get the current directory
    current_dir = os.getcwd()

    # Read the Jupyter file
    file_name = 'FinanceDataProject.ipynb'  # Replace with the name of your Jupyter file
    notebook_path = os.path.join(current_dir, file_name)

    with open(notebook_path, 'r') as file:
        nb = nbformat.read(file, nbformat.NO_CONVERT)

    # Get the functions from the notebook
    functions = []

    for cell in nb.cells:
        if cell.cell_type == 'code' and cell.source.startswith('def'):
            source_lines = cell.source.split('\n')
            function_line = source_lines[0].strip()
            function_name = function_line.split(' ')[1].split('(')[0]
            functions.append(function_name)

    # Print the checklist of functions
    print("Functions implemented in the notebook:\n")

    for function in functions:
        print(f"[x] {function}")


# Run the main function
if __name__ == '__main__':
    main()
