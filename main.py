import glob
import pandas as pd
import openpyxl
from pathlib import Path

from fpdf import FPDF

filepaths = glob.glob('invoices/*xlsx')
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {int(invoice_nr)}", align='L', ln=1)
    pdf.output(f"PDFs/{filename}.pdf")
    

