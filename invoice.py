from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import  Paragraph, Table, TableStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from datetime import datetime
import numpy as np
import pandas as pd



class InvoiceTemplate:
    def __init__(self, invoice_number):
        '''Start canvas'''
        self.PAGE_SIZE = (595.27, 841.90)
        self.c = canvas.Canvas(invoice_number + ".pdf", pagesize=self.PAGE_SIZE, bottomup=0)
        self.width, self.height = A4
        self.date = datetime.today().strftime('%d-%m-%Y')

    def make_data_table(self, data_table):
        self.style = TableStyle([
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN', (0,-1), (-1,-1), "CENTER"),
            ('VALIGN', (3,3), (-1,-1), "BOTTOM"),
            ('FONTSIZE', (0,0), (-1,-1), 5),
            ])
        self.table = Table(data_table, style=self.style)

    def create_document(self, product=None, customer=None):
        '''template invoice'''
        #Information section
        self.c.translate(10, 40)
        self.c.scale(1, -1)
        self.c.scale(1, -1)
        self.c.setFont("Helvetica-Bold", 5)
        self.c.drawCentredString(30, 0, "Company Ab Oy")
        self.c.setFont("Helvetica-Bold", 2)
        self.c.drawCentredString(30, 2, "Address xyz")
        self.c.drawCentredString(30, 6, "Postal number 123")
        self.c.setFont("Helvetica-Bold", 2)
        self.c.drawCentredString(30, 10, "Business ID: ")
        self.c.line(5, 15, 250, 15)
        #Middle section 
        self.c.setFont("Courier-Bold", 10)
        self.c.drawCentredString(80, -10, "Invoice")
        self.c.roundRect(5, 23, 170, 40, 10, stroke=1, fill=0)
        self.c.setFont("Times-Bold", 3)
        self.c.drawRightString(45, 30, "Invoice number: " )
        self.c.drawRightString(45, 40, f"Date: {self.date} ")
        self.c.drawRightString(45, 50, "Customer name: ")
        self.c.drawRightString(45, 60, "Phone number: ")
        #Table
        table_info = self.table
        table_info.wrapOn(self.c, self.width, self.height)
        table_info.drawOn(self.c, 0*mm, 30*mm)
        #Bottom section
        self.c.line(15, 220, 185, 220)
        self.c.line(100, 220, 100, 238)
        self.c.drawString(20, 225, "We declare that above mentioned")
        self.c.drawString(20, 230, "information is true")
        self.c.drawString(20, 235, "(This system generated invoice)")
        self.c.drawRightString(180, 235, "Authorised signatory")
        self.c.showPage()

    def save_pdf(self):
        self.c.save()


