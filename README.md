# ASL_pymol_updated
Updated pymol repo that will NOT have branches

README / Summary:
=================

This script is designed to automate the process of loading molecular structures into PyMOL, selecting and visualizing antigenic sites, clade and subclade-defining mutations, and generating high-quality images of these structures. It includes functions for setting up the base structure, highlighting specific sites and mutations, and exporting images. This updated repo will not include branches. 

To use this script:
1. Ensure PyMOL is installed and running.
2. Place this script in your working directory.
3. Set the following paths and constants in the script:
   - `DEFAULT_OUTPUT_LOCATION`: Set to the directory where you want the images to be saved.
   - `DEFAULT_SESSION_LOCATION`: Set to the directory where you want the PyMOL sessions to be saved.
   - `cif_file_path`: Set this path to the location of your `.cif` file.
4. Run the script directly using PyMOL's Python environment (e.g., `run /path/to/your/Pymol_mark_mutations_GitHub.py`).
5. The script will output images to the specified directory, organized by protein and sequence name.

Main Sections:
--------------
1. Initialization and Setup Functions
2. Antigenic Sites and Mutation Visualization
3. Image Export Functions
4. Process Sequence Function

## How to Use This Script

### Running the Script in PyMOL

This script is designed to be run directly in the PyMOL environment. Due to PyMOL's execution model, you need to manually run the `process_sequence()` function in the PyMOL command line after loading the script.

### Step-by-Step Instructions

1. **Load the Script in PyMOL**:
   - Use the following command in the PyMOL command line to load the script:
     ```
     run /path/to/your/Pymol_mark_mutations_GitHub.py
     ```

2. **Run the `process_sequence()` Function**:
   - Manually copy and paste one of the following commands into the PyMOL command line:
   
   **Example for H1N1:**
   ```python
   process_sequence(seq_name='H1_01', cif_file_path='/path_to_your_cif_file.cif', strain_type='H1N1', clade='5a.2a', subclade='C.1', H1_mutations=[], H2_mutations=[91,177])
   ```

   **Example for H3N2:**
   ```python
    process_sequence(seq_name='H3_01_AAID07', cif_file_path='/path_to_your_cif_file.cif', strain_type='H3N2', clade='2a.1', subclade='G.1.1', H1_mutations=[], H2_mutations=[174])
   ```
