import subprocess
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

# Set event loop policy for Windows to avoid the warning
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

def run_notebook(notebook_path):
    try:
        # Command to execute the Jupyter notebook
        cmd = [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute", 
            "--inplace",  # Modify the existing notebook
            notebook_path
        ]
        
        # Running the command using subprocess
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)

        if result.returncode == 0:
            print(f"Notebook {notebook_path} executed successfully.")
        else:
            print(f"Error executing notebook {notebook_path}: {result.stderr}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error while executing notebook: {e}")
    except FileNotFoundError:
        print("Jupyter is not installed or not found in PATH.")


# Specify the path to your .ipynb file
run_notebook("C:/Users/raahu/Desktop/ipl2025pre/IPL2025pre/r1.ipynb")



  # Wait for Flask to start, adjust as needed



