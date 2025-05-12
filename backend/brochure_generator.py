from fpdf import FPDF
import os

def generate_brochure(user_profile, project_details, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Brochure for {user_profile['name']}")
    pdf.multi_cell(0, 10, f"Preferences: {user_profile['preferences']}")
    pdf.multi_cell(0, 10, f"Project Details: {project_details}")
    pdf.output(output_path)
