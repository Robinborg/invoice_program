from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import  Paragraph, Table, TableStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from datetime import datetime
import numpy as np
import pandas as pd
from typing import List



class InvoiceTemplate:
    """The invoice template"""
    def __init__(self, invoice_number: int):
        """Start the template with a Canvas and get the today's date"""
        self.PAGE_SIZE = A4 #(595.27, 841.90)
        self.c = canvas.Canvas(invoice_number + ".pdf", pagesize=self.PAGE_SIZE, bottomup=0)
        self.width, self.height = A4
        self.date = datetime.today().strftime('%d-%m-%Y')

    def make_data_table(self, data_table: List):
        """Create the Table for the products"""
        first_table = Table(data_table, rowHeights=2*cm, colWidths=4*cm)
        first_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
        self.table = first_table
         

    def create_document(self, invoice_number=0, customer_name: str = None, customer_phone: int = 0):
        """Create the invoice canvas"""
        #Information section
        self.c.translate(10, 40)
        self.c.scale(1, -1)
        self.c.scale(1, -1)
        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawCentredString(400, 10, "Invoice")
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawCentredString(130, 1, "Company Ab Oy")
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawCentredString(130, 20, "Address: company's street 1")
        self.c.drawCentredString(130, 40, "Postal: number 123")
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawCentredString(130, 60, "Business ID: 999999-9")
        #Middle section 
        self.c.roundRect(5, 80, 570, 100, 10, stroke=1, fill=0)
        self.c.setFont("Times-Bold", 12)
        self.c.drawRightString(200, 100, f"Invoice number: {invoice_number}" )
        self.c.drawRightString(200, 120, f"Date: {self.date} ")
        self.c.drawRightString(200, 140, f"Customer name: {customer_name} ")
        self.c.drawRightString(200, 160, f"Phone number: {customer_phone}")
        #Table
        table_info = self.table
        table_info.wrapOn(self.c, self.width, self.height)
        table_info.drawOn(self.c, -1*mm, 80*mm)
        #Bottom section
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(20, 780, "We declare that above mentioned information is true")
        self.c.drawString(20, 790, "(This system generated invoice)")
        self.c.showPage()

    def save_pdf(self):
        """Saves the pdf to the project folder"""
        self.c.save()

