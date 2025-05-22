import os
import shutil

# Define input and output paths
input_path = 'input_folder'
output_path = 'organized_output'

# Supported CAD-related file extensions
cad_extensions = ['.dwg', '.dxf', '.pdf']

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Get all files in input folder
try:
    all_files = os.listdir(input_path)
except FileNotFoundError:
    print(f"Input folder '{input_path}' not found.")
    exit()

# Filter CAD files
cad_files = [f for f in all_files if os.path.splitext(f)[1].lower() in cad_extensions]

# Create folders by extension and move files
for file in cad_files:
    ext = os.path.splitext(file)[1].lower()
    ext_folder = ext[1:].upper()  # '.dwg' -> 'DWG'
    target_folder = os.path.join(output_path, ext_folder)
    os.makedirs(target_folder, exist_ok=True)

    source_path = os.path.join(input_path, file)
    dest_path = os.path.join(target_folder, file)

    try:
        shutil.move(source_path, dest_path)
        print(f"Moved: {file} → {ext_folder}/")
    except Exception as e:
        print(f"Error moving {file}: {e}")

print("\n✅ All CAD files have been organized.")
