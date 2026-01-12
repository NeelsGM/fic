import mrmeshpy as mm
import google.generativeai as genai
import os

# --- STEP 1: Setup the AI Brain ---
# Get your key from https://aistudio.google.com/
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-pro')

def process_scan_to_step(input_scan):
    print(f"--- Processing {input_scan} ---")
    
    # --- STEP 2: The Repairman (MeshLib) ---
    # Load your messy scan (STL, OBJ, or PLY)
    mesh = mm.loadMesh(input_scan)
    
    # Get dimensions (Bounding Box)
    bbox = mesh.computeBoundingBox()
    size_x = bbox.max.x - bbox.min.x
    size_y = bbox.max.y - bbox.min.y
    size_z = bbox.max.z - bbox.min.z
    
    print(f"Detected Dimensions: {size_x:.2f} x {size_y:.2f} x {size_z:.2f} mm")

    # --- STEP 3: The Architect (Gemini) ---
    prompt = f"""
    I have a 3D scan of a mechanical part with these dimensions: 
    X={size_x:.2f}mm, Y={size_y:.2f}mm, Z={size_z:.2f}mm.
    
    The part is an L-bracket with a central hole. 
    Write a Python CadQuery script that:
    1. Creates a solid L-shape based on these dimensions.
    2. Adds a 10mm hole in the center of the base.
    3. Exports the result as a file named 'reverse_engineered.step'.
    
    Provide ONLY the Python code, no explanation.
    """
    
    print("AI is reverse engineering the geometry...")
    response = model.generate_content(prompt)
    cad_code = response.text.replace("```python", "").replace("```", "")

    # --- STEP 4: The Builder (CadQuery) ---
    # We save Gemini's code to a temporary file and run it
    with open("temp_cad_builder.py", "w") as f:
        f.write(cad_code)
    
    print("Building the STEP file...")
    os.system("python temp_cad_builder.py")
    print("Success! Your editable STEP file is ready.")

# RUN IT
# Change "my_bracket_scan.stl" to your actual scan filename
process_scan_to_step("my_bracket_scan.stl")
