# 🗂️ AutoCAD File Organizer

A simple Python tool to automatically organize AutoCAD-related files (`.dwg`, `.dxf`, `.pdf`) into categorized folders based on their file type.

---

## 📌 Features

- Organizes `.dwg`, `.dxf`, `.pdf` files from a source folder
- Automatically creates subfolders for each file type
- Moves files to their respective folders
- Lightweight and easy to use – perfect for engineers and architects

---

## 🧰 Built With

- Python 3.x
- Standard libraries: `os`, `shutil`

---

## 🗃️ Folder Structure

AutoCAD_Organizer/
├── input_folder/ # Place your files here
│ ├── drawing1.dwg
│ ├── fireplan.pdf
│ └── plumbing.dxf
├── organized_output/ # Created by the script
│ ├── DWG/
│ ├── DXF/
│ └── PDF/
├── main.py # Main script
└── README.md



---

## ▶️ How to Use

1. Clone or download this repository.
2. Place your `.dwg`, `.dxf`, `.pdf` files into the `input_folder/`.
3. Run the script:

```bash
python main.py


input_folder/
├── HVAC_Plan.dwg
├── FirePlan.pdf
├── plumbing.dxf


organized_output/
├── DWG/
│   └── HVAC_Plan.dwg
├── PDF/
│   └── FirePlan.pdf
├── DXF/
│   └── plumbing.dxf
