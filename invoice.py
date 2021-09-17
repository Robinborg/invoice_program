from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


class InvoiceTemplate:
    def __init__(self,name, number_invoice):
        self.name = name
        self.number_invoice = number_invoice

    def blank_canvas(self):
        #Creating the canvas
        c = canvas.Canvas("fromclass.pdf",pagesize=(595.27,841.89), bottomup=0)
        #Creating the logo
        c.translate(10,40)
        c.scale(1, -1)
        #c.drawImage("logo.jpg", 0, 0, width=50, height=30)
        #Title section
        c.scale(1, -1)
        c.setFont("Helvetica-Bold", 5)
        c.drawCentredString(30, 0, "Oomph Technology Ab Oy")
        c.setFont("Helvetica-Bold", 2)
        c.drawCentredString(30, 2, "Address xyz")
        c.drawCentredString(30, 6, "Postal number 123")
        c.setFont("Helvetica-Bold", 2)
        c.drawCentredString(30, 10, "Business ID: ")
        c.line(5, 15, 250, 15)
        #Middle section 
        c.setFont("Courier-Bold", 10)
        c.drawCentredString(80, -10, "Invoice")
        
        c.roundRect(5, 23, 170, 40, 10, stroke=1, fill=0)
        c.setFont("Times-Bold", 3)
        c.drawRightString(45, 30, "Invoice number: " )
        c.drawRightString(45, 40, "Date: ")
        c.drawRightString(45, 50, "Customer name: ")
        c.drawRightString(45, 60, "Phone number: ")
       
        c.roundRect(5, 70, 175, 130, 10, stroke=1, fill=0)
        c.line(5, 80, 180, 80)
        c.drawCentredString(28, 75, "Serial number: ")
        c.drawCentredString(60, 75, "Goods description: ")
        c.drawCentredString(120, 75, "Rate: ")
        c.drawCentredString(145, 75, "QTY: ")
        c.drawCentredString(165, 75, "Total: ")
        
        c.line(35, 80, 35, 200)
        c.line(115, 80, 115, 200)
        c.line(135, 80, 135, 200)
        c.line(160, 80, 160, 200)
        
        c.line(15, 220, 185, 220)
        c.line(100, 220, 100, 238)
        c.drawString(20, 225, "We declare that above mentioned")
        c.drawString(20, 230, "information is true")
        c.drawString(20, 235, "(This system generated invoice)")
        c.drawRightString(180, 235, "Authorised signatory")
        
        c.showPage()
        c.save()

