from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


class InvoiceTemplate:
    def __init__(self, invoice_number):
        self.PAGE_SIZE = (595.27, 841.90)
        self.c = canvas.Canvas(invoice_number + ".pdf", pagesize=self.PAGE_SIZE, bottomup=0)

    def create_document(self):
        '''template invoice'''
        self.c.translate(10, 40)
        self.c.scale(1, -1)
        self.c.setFont("Helvetica-Bold", 5)
        self.c.drawCentredString(30, 0, "Oomph Technology Ab Oy")
        
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
        self.c.drawRightString(45, 40, "Date: ")
        self.c.drawRightString(45, 50, "Customer name: ")
        self.c.drawRightString(45, 60, "Phone number: ")

        self.c.roundRect(5, 70, 175, 130, 10, stroke=1, fill=0)
        self.c.line(5, 80, 180, 80)
        self.c.drawCentredString(28, 75, "Serial number: ")
        self.c.drawCentredString(60, 75, "Goods description: ")
        self.c.drawCentredString(120, 75, "Rate: ")
        self.c.drawCentredString(145, 75, "QTY: ")
        self.c.drawCentredString(165, 75, "Total: ")

        self.c.line(35, 80, 35, 200)
        self.c.line(115, 80, 115, 200)
        self.c.line(135, 80, 135, 200)
        self.c.line(160, 80, 160, 200)
        
        #Bottom section
        self.c.line(15, 220, 185, 220)
        self.c.line(100, 220, 100, 238)
        self.c.drawString(20, 225, "We declare that above mentioned")
        self.c.drawString(20, 230, "information is true")
        self.c.drawString(20, 235, "(This system generated invoice)")
        self.c.drawRightString(180, 235, "Authorised signatory")

        self.c.showPage()

    def make_table(self, client, product):
        #Make table
        pass

    def save_pdf(self):
        self.c.save()

