import os
import sys
import pymol

def pdb_to_png(pdb_files, output_dir="output_images", dpi=300):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pymol.finish_launching(['pymol', '-cq'])
    # Loop through each PDB file and generate the PNG image
    for pdb_file in pdb_files:
        # Extract the file name without extension to name the PNG
        file_name = os.path.basename(pdb_file).replace(".pdb", "")

        # Load the PDB file into PyMOL
        cmd.load(pdb_file)

        # Set visualization style and color by chain
        cmd.show("cartoon")  # You can also use 'stick', 'ribbon', etc.
        cmd.color("cyan", "all")  # Set a base color for visibility
        cmd.util.cbc()  # Color by chain

        # Zoom and adjust the scene
        cmd.zoom("all")
        cmd.bg_color("white")  # Optional: white background for visualization purposes

        # Set transparent background for PNG
        cmd.set("ray_opaque_background", 0)

        # Save the image as a PNG in the output directory
        output_path = os.path.join(output_dir, f"{file_name}.png")
        print(f"Saving image to '{output_path}'")
        cmd.png(output_path, dpi=dpi)

        # Clear the session to prepare for the next PDB file
        cmd.delete("all")

    # Quit PyMOL after all files are processed
    cmd.quit()
