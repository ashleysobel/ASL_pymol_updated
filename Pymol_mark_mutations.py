# Pymol_mark_mutations_GitHub.py

# To run this code through pymol, copy: "run /path/to/code/location" into pymol command line input
# Ex: run /Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Pymol_mark_mutations_local.py
# Must update the following to run on a new computer: 
# 1. DEFAULT_OUTPUT_LOCATION: set to wherever you want the images to be saved to
# 2. cif_file_path: set this path to wherever your "4lxv-assembly1.cif" is saved to
# 3. strain_type: set this as either "H1N1 or "H3N2" (though H3N2 is not set up right now)
# 4. If you want to change the background color for the protein structure, you can do it here
# Instructions for running the code for a sequence or set of sequences: 
# Option 1: Fill out the process_sequence() definition for each of the sequences. This will generate 2 views of the protein for each of the listed sequnces. The final sequence will remain visible in the pymol interface
# Option 2: Copy and paste the entries for the process_sequence() definition one by one into the interface. This will generate and export the images, but will leave each structure visible.
# Option 3: You can run each of the individual functions separately, but remember to clear_all_selections() between seperate sampels to reset labelled residues

from pymol import cmd
import os

# Constants 
DEFAULT_OUTPUT_LOCATION = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Python_code/ImageOutput/"
DEFAULT_SESSION_LOCATION = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Python_code/StructureSessions/"
DEFAULT_COLOR = 'grey70'

# ---------------------------------------------------
# Initialization and Setup Functions
# ---------------------------------------------------

def clear_all_selections():
    """Clear all selections, reset colors, and remove custom selections."""
    cmd.hide('everything')
    cmd.color(DEFAULT_COLOR, 'all')
    cmd.show('surface')
    cmd.show('cartoon')
    cmd.delete('all')

def set_base(cif_file_path):
    """Set up the base configuration for the structure."""
    cmd.load(cif_file_path)
    cmd.hide('all')
    cmd.show('surface')
    cmd.show('cartoon')
    cmd.set('surface_color', DEFAULT_COLOR)
    cmd.set('cartoon_color', DEFAULT_COLOR)
    cmd.set('bg_rgb', [1, 1, 1])
    cmd.set('ambient', 0.4)
    cmd.space('cmyk')
    cmd.set('ray_trace_fog', 0)
    cmd.set('depth_cue', 1)
    cmd.set('ray_trace_mode', 1)
    cmd.set('ray_trace_gain', 0.002)

# ---------------------------------------------------
# Antigenic Sites and Mutation Visualization
# ---------------------------------------------------

def set_antigenic_sites(strain_type):
    """Set and color the antigenic sites based on the strain type."""
    
    # Define color mapping for each site
    site_colors = {
        'site_Sa': 'lightpink',
        'site_Sb': 'lightblue',
        'site_Ca1': 'paleyellow',
        'site_Ca2': 'palecyan',
        'site_Cb': 'lightorange',
        'site_A': 'lightpink',
        'site_B': 'lightblue',
        'site_C': 'paleyellow',
        'site_D': 'palecyan',
        'site_E': 'lightorange',
    }
    
    if strain_type == 'H1N1':
        antigenic_sites = {
            'site_Sa': '(chain A or chain C or chain E) and resi 124-125+153-157+159-164',
            'site_Sb': '(chain A or chain C or chain E) and resi 184-194',
            'site_Ca1': '(chain A or chain C or chain E) and resi 166-170+203-205+235-237',
            'site_Ca2': '(chain A or chain C or chain E) and resi 137-142+221-222',
            'site_Cb': '(chain A or chain C or chain E) and resi 70-75',
        }
    elif strain_type == 'H3N2':
        antigenic_sites = {
            'site_A': "chain A+A-2+A-3 and resi 122-127+129+131-138+142-146",
            'site_B': "chain A+A-2+A-3 and resi 155-160+164+188-190+193-194+196-197",
            'site_C': "chain A+A-2+A-3 and resi 50+53+54+275",
            'site_D': "chain A+A-2+A-3 and resi 201-207+213+217-220+230+244",
            'site_E': "chain A+A-2+A-3 and resi 62-63+75+79-83",
        }
    else:
        print("Invalid strain type. Please use 'H1N1' or 'H3N2'.")
        return

    # Apply selections and colors
    for site, selection in antigenic_sites.items():
        cmd.select(site, selection)
        cmd.color(site_colors[site], site)  # Use the correct color from the dictionary
        cmd.show('surface', site)
        cmd.set('surface_color', site, site)

def set_clade_subclade(strain_type, clade_name, subclade_name=None):
    print(f"Debug: strain_type={strain_type}, clade_name={clade_name}, subclade_name={subclade_name}")

    if subclade_name and not subclade_name.startswith("Subclade_"):
        subclade_name = f"Subclade_{subclade_name}"
    print(f"Constructed subclade_name: {subclade_name}")

    clade_residues = {
        'H1N1': {
            '5a.2': {'A+C+E': '74+97+129+162+163+164+185+216+256+295','B+D+F':'124'},
            '5a.2a': {'A+C+E': '54+129+156+161+185+186+189+308'},
            '5a.2a.1': {'A+C+E': '54+129+137+142+156+161+185+186+189+308'}
        },
        'H3N2': {
            '2a.1':{
                'A+A-2+A-3': '3+45+48+53+62+83+94+104+121+131+142+144+159+159+160+164+171+186+190+193+195+276+311',
                'B+B-2+B-3': '77+155+160+103+200'
            },
            '2a.1b':{
                'A+A-2+A-3': '45+48+3+144+159+160+121+171+62+142+311+131+83+94+164+186+190+193+195+156+53+104+276+140+299',
                'B+B-2+B-3': '160+77+155+200+193'
            },
            '2b':{
                'A+A-2+A-3': '45+48+3+144+159+160+121+171+62+142+311+131+83+94+164+186+190+193+195+50+79+140',
                'B+B-2+B-3': '160+77+155+200+193'
            }
        }
    }
    
    subclade_residues = {
        'H3N2': {
            '2a.1': {
                'Subclade_G.1.1': {
                    'A+A-2+A-3': '159+160+164+186+190+193+195+156+53+104+276'
                }
            },
            '2a.1b': {
                'Subclade_G.1.1.2': {
                    'A+A-2+A-3': '159+160+164+186+190+193+195+156+53+104+276+140+299'
                }
            },
            '2b': {
                'Subclade_G.2': {
                    'A+A-2+A-3': '159+160+164+186+190+193+195+50+79+140'
                },
                'Subclade_G.2.1': {
                    'A+A-2+A-3': '159+160+164+186+190+193+195+50+79+140+135+262'
                }
            }
        },
        'H1N1': {
            '5a.2': {
                'Subclade_C': {'A+C+E': '156+161'}
            },
            '5a.2a': {
                'Subclade_C.1': {'A+C+E': '54+186+189+308'},
                'Subclade_C.1.8': {'A+C+E': '54+186+189+308+120+47'},
                'Subclade_C.1.9': {'A+C+E': '54+186+189+308+120+169'}
            },
            '5a.2a.1': {
                'Subclade_C.1.1': {'A+C+E': '137+142'},
                'Subclade_D': {'A+C+E': '54+186+189+308+216'},
                'Subclade_D.1': {'A+C+E': '54+186+189+308+45+216'},
                'Subclade_D.2': {'A+C+E': '54+186+189+308+113+216'},
                'Subclade_D.3': {'A+C+E': '54+186+189+308+120', 'B+D+F': '45'}
            }
        }
    }

    # Check if the clade name exists
    if clade_name not in clade_residues[strain_type]:
        print(f"Clade {clade_name} not recognized. Please ensure the clade name is correct.")
        return

    for chain_group, residues in clade_residues[strain_type][clade_name].items():
        cmd.select(clade_name, f'chain {chain_group} and resi {residues}')
        cmd.color('tv_blue', clade_name)
        cmd.show('surface', clade_name)
        cmd.set('surface_color', clade_name, clade_name)

    if subclade_name:
        subclades_in_clade = subclade_residues[strain_type].get(clade_name, {}).keys()
        print(f"Available subclades for clade {clade_name}: {list(subclades_in_clade)}")

        if subclade_name in subclades_in_clade:
            for chain_group, residues in subclade_residues[strain_type][clade_name][subclade_name].items():
                cmd.select(subclade_name, f'chain {chain_group} and resi {residues}')
                cmd.color('tv_green', subclade_name)
                cmd.show('surface', subclade_name)
                cmd.set('surface_color', subclade_name, subclade_name)
        else:
            print(f"Subclade {subclade_name} does not match clade {clade_name}.")

        
def assess_mutations_HA(seq_name, H1_mutations=None, H2_mutations=None, color='grey20'):
    """Assess and display mutations for HA protein chains under the same selection name."""
    selection_string = ""
    if H1_mutations:
        H1_residues = "+".join(map(str, H1_mutations))
        selection_string += f"(chain A+C+E and resi {H1_residues})"
    if H2_mutations:
        H2_residues = "+".join(map(str, H2_mutations))
        if selection_string:
            selection_string += " or "
        selection_string += f"(chain B+D+F and resi {H2_residues})"

    if selection_string:
        cmd.select(seq_name, selection_string)
        cmd.color(color, seq_name)
        cmd.show('surface', seq_name)
        cmd.set('surface_color', color, seq_name)

# ---------------------------------------------------
# Image Export
# ---------------------------------------------------

def generate_image(seq_name, view, protein, clade, subclade, output_location=None):
    """Generate an image with the specified view and save it to the output location."""
    if output_location is None:
        output_location = DEFAULT_OUTPUT_LOCATION

    print(f"The protein is defiend as {protein}")

    # Set the view based on the protein type
    if protein == 'H1':  # H1N1 View
        if view == 'side':
            cmd.set_view([
                0.888682842,  0.371483058, -0.268776417,
               -0.303239465,  0.915848851,  0.263189942,
                0.343927294, -0.152389228,  0.926546395,
                0.000021487,  0.000063539, -474.919036865,
               76.153892517, 223.045745850, 287.983581543,
             -19575.746093750, 20525.484375000,  -20.000000000
            ])
        elif view == 'top':
            cmd.set_view([
                0.795617044,  0.577678502,  0.182431772,
               -0.285880089,  0.092522122,  0.953790188,
                0.534102142, -0.811003804,  0.238758013,
                0.000021487,  0.000063539, -474.919036865,
               76.153892517, 223.045745850, 287.983581543,
             -21575.746093750, 22525.484375000,  -20.000000000
            ])
    elif protein == 'H3':  # H3N2 View
        if view == 'side':
            cmd.set_view([
                0.136302233,    0.264822513,   -0.954613864,\
                0.989724994,    0.005639514,    0.142883018,\
                0.043221079,   -0.964281559,   -0.261330694,\
                -0.000014514,    0.000120746, -413.245788574,\
                46.526790619,  -30.711526871,  -48.703193665,\
                346.461273193,  480.010101318,  -20.000000000
            ])
        elif view == 'top':
            cmd.set_view([
                0.645424068,    0.758313954,   -0.091568671,\
                0.763582408,   -0.643582523,    0.052419290,\
                -0.019184131,   -0.103754535,   -0.994418800,\
                -0.000014514,    0.000120746, -413.245788574,\
                46.526790619,  -30.711526871,  -48.703193665,\
                346.461273193,  480.010101318,  -20.000000000
            ])
    
    # Create the subdirectory for the protein if it doesn't exist
    protein_path = os.path.join(output_location, protein)
    os.makedirs(protein_path, exist_ok=True)
    
   # Generate the filename based on provided arguments
    # Corrected code snippet for filename generation:
    filename_parts = [seq_name or 'NoSeqName']
    filename_parts.append(protein)
    filename_parts.append(clade.replace('.', ''))

    if subclade:
        filename_parts.append(subclade.replace('.', ''))

    filename_parts.append(view)
    filename = "_".join(filename_parts) + ".png"

    full_path = os.path.join(protein_path, filename)
    
    # Clear selections to avoid showing selection dots in the image
    cmd.deselect()
    
    # Aggressively zoom in on the visible structure to reduce white space
    cmd.zoom('visible', buffer=0)  # Tight zoom
    
    # Further adjust clipping planes to reduce white space
    cmd.clip('near', -5)  # Adjust near clipping plane
    cmd.clip('far', 5)    # Adjust far clipping plane
    
    # Save the image with high DPI
    cmd.png(full_path, dpi=300)
    print(f"Image saved to: {full_path}")

# Example usage:
# generate_image(seq_name='AAID1', view='side', protein='H1', clade='5a.2a', subclade='C.1.9')

def save_pymol_session(seq_name, clade, subclade, protein, output_location=None):
    """Save the current PyMOL session to a .pse file."""
    if output_location is None:
        output_location = DEFAULT_SESSION_LOCATION

    # Create the subdirectory for the protein if it doesn't exist
    session_path = os.path.join(output_location, protein)
    os.makedirs(session_path, exist_ok=True)

    # Generate the session filename
    filename_parts = [seq_name] if seq_name else []
    filename_parts.append(clade.replace('.', ''))

    if subclade:
        filename_parts.append(subclade.replace('.', ''))

    filename = "_".join(filename_parts) + ".pse"

    full_path = os.path.join(session_path, filename)

    # Save the session
    cmd.save(full_path)
    print(f"Session saved to: {full_path}")

def process_sequence(seq_name, cif_file_path, strain_type, clade, subclade, H1_mutations, H2_mutations, color='grey20'):
    """Process a sequence by setting up the base, assessing mutations, and generating images."""
    
    # Clear prior functions
    clear_all_selections()

    # Determine the protein based on the strain type
    if strain_type == 'H1N1':
        protein = 'H1'
    elif strain_type == 'H3N2':
        protein = 'H3'
    else:
        raise ValueError(f"Unknown strain type: {strain_type}. Please use 'H1N1' or 'H3N2'.")

    # Set up the base environment
    set_base(cif_file_path)
    set_antigenic_sites(strain_type)
    set_clade_subclade(strain_type, clade, subclade)
    
    # Assess mutations and generate images
    assess_mutations_HA(seq_name, H1_mutations, H2_mutations, color=color)
    generate_image(seq_name=seq_name, view='side', protein=protein, clade=clade, subclade=subclade)
    generate_image(seq_name=seq_name, view='top', protein=protein, clade=clade, subclade=subclade)

    # Save the PyMOL session
    save_pymol_session(seq_name=seq_name, clade=clade, subclade=subclade, protein=protein)

print("Loaded Functions")
 

# ----------------------------------------------
# Manual Execution Instructions
# ----------------------------------------------

# Set the path for the cif file
cif_file_path_H1 = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Hemagglutinin/H1/4lxv-assembly1.cif"
cif_file_path_H3 = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Hemagglutinin/H3/4o5n-assembly1.cif"
# To use this script, manually run the `process_sequence()` function in the PyMOL command line or script. 
# Example 1: Generate images for specific mutations
# Copy and paste the following line into the PyMOL command line (has options filled out):

# Sequences for H1N1
# process_sequence(seq_name='H1_01', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1', H1_mutations=[], H2_mutations=[91,177])
# process_sequence(seq_name='H1_02', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1', H1_mutations=[137], H2_mutations=[91])
# process_sequence(seq_name='H1_03', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1.8', H1_mutations=[96], H2_mutations=[200])
# process_sequence(seq_name='H1_04', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1.8', H1_mutations=[96,265], H2_mutations=[200])
# process_sequence(seq_name='H1_05', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1.9', H1_mutations=[112], H2_mutations=[183])
# process_sequence(seq_name='H1_06', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1.9', H1_mutations=[160,216], H2_mutations=[179])
# process_sequence(seq_name='H1_07', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a', subclade='C.1.9', H1_mutations=[127,216], H2_mutations=[179])
# process_sequence(seq_name='H1_08', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='C.1.1', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H1_09', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='C.1.1', H1_mutations=[54], H2_mutations=[])
# process_sequence(seq_name='H1_10', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H1_11', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[274], H2_mutations=[])
# process_sequence(seq_name='H1_12', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[183,274], H2_mutations=[])
# process_sequence(seq_name='H1_13', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[], H2_mutations=[88])
# process_sequence(seq_name='H1_14', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[35], H2_mutations=[])
# process_sequence(seq_name='H1_15', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D', H1_mutations=[], H2_mutations=[88,125])
# process_sequence(seq_name='H1_16', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.1', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H1_17', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.1', H1_mutations=[141], H2_mutations=[])
# process_sequence(seq_name='H1_18', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.1', H1_mutations=[302], H2_mutations=[])
# process_sequence(seq_name='H1_19', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.1', H1_mutations=[250], H2_mutations=[78])
# process_sequence(seq_name='H1_20', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.2', H1_mutations=[186], H2_mutations=[])
# process_sequence(seq_name='H1_21', cif_file_path=cif_file_path_H1, strain_type='H1N1', clade ='5a.2a.1', subclade='D.2', H1_mutations=[274], H2_mutations=[])

# Sequences for H3N2 
process_sequence(seq_name='H3_01_AAID07', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2a.1', subclade='G.1.1', H1_mutations=[], H2_mutations=[174])
# process_sequence(seq_name='H3_02_AAID04', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2a.1b', subclade='G.1.1.2', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H3_03_AAID02', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[101], H2_mutations=[])
# process_sequence(seq_name='H3_04', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[81], H2_mutations=[149])
# process_sequence(seq_name='H3_05_AAID12', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[275], H2_mutations=[])
# process_sequence(seq_name='H3_06', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[27], H2_mutations=[])
# process_sequence(seq_name='H3_07_AAID09', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[50,242], H2_mutations=[139,202])
# process_sequence(seq_name='H3_08_AAID16', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[82], H2_mutations=[])
# process_sequence(seq_name='H3_09_AAID01', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[81], H2_mutations=[])
# process_sequence(seq_name='H3_10_AAID10', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[81], H2_mutations=[])
# process_sequence(seq_name='H3_11_AAID08', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[79,122], H2_mutations=[])
# process_sequence(seq_name='H3_12_AAID15', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[105,312], H2_mutations=[])
# process_sequence(seq_name='H3_13_AAID03', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[], H2_mutations=[82])
# process_sequence(seq_name='H3_14_AAID05', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[], H2_mutations=[212])
# process_sequence(seq_name='H3_15_Consensus', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H3_16', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[], H2_mutations=[43])
# process_sequence(seq_name='H3_17_AAID14', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2', H1_mutations=[137,188,233], H2_mutations=[])
# process_sequence(seq_name='H3_18_AAID11', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2.1', H1_mutations=[122], H2_mutations=[])
# process_sequence(seq_name='H3_19_AAID13', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2.1', H1_mutations=[328], H2_mutations=[])
# process_sequence(seq_name='H3_20_AAID06', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2.1', H1_mutations=[], H2_mutations=[])
# process_sequence(seq_name='H3_21_AAID17', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='2b', subclade='G.2.1', H1_mutations=[], H2_mutations=[116,158])


# process_sequence(seq_name='', cif_file_path=cif_file_path_H3, strain_type='H3N2', clade ='', subclade='', H1_mutations=[], H2_mutations=[])

# Example 2: Generate images with no mutations
# Copy and paste the following line into the PyMOL command line (instructions for filling out command below):
# process_sequence(seq_name='your_sequence_name', cif_file_path='/path_to_your_cif_file.cif', strain_type='H1N1', clade='your_clade', subclade='your_subclade', H1_mutations=[], H2_mutations=[])
