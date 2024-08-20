# ASL_pymol_updated
Updated pymol repo that will NOT have branches

README / Summary:
=================

This script is designed to automate the process of loading molecular structures into PyMOL, selecting and visualizing antigenic sites, clade and subclade-defining mutations, and generating high-quality images of these structures. It includes functions for setting up the base structure, highlighting specific sites and mutations, and exporting images. This updated repo will not include branches. 

To use this script:
1. Ensure PyMOL is installed and running.
2. Place this script in your working directory.
4. Run the script directly using PyMOL's Python environment (e.g., `run pymol_script.py`).
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
   
   **Example 1:**
   ```python
   process_sequence(seq_name='temp6', cif_file_path='/path_to_your_cif_file.cif', strain_type='H1N1', clade='5a.2a.1', subclade='D', H1_mutations=[], H2_mutations=[])


Author: [Ashley Sobel Leonard]
Date: [08/09/2024]

