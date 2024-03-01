from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image

def create_invoice(pdf_file):
    # Create a canvas
    c = canvas.Canvas(pdf_file, pagesize=A4)


    # HEADER
    imagen = "logo.png"
    imagen_obj = Image(imagen, width=70, height=70)
    imagen_obj.drawOn(c, 50, 720)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 700, "Resistiré Helados")


    c.setFont("Helvetica", 12)
    c.drawString(50, 680, "Olavarria 895 - Dolores - Buenos Aires")
    c.drawString(50, 665, "Tel: 2245-470033")
    c.drawString(50, 650, "Email: Heladeriaresistire@gmail.com")
    c.drawString(50, 635, "IVA: Monotributo")


    # Rectangulo del tipo de factura
    c.rect(310, 740, 30,40)

    # Centrar la letra "A" dentro del rectángulo
    x_text = 310 + (30 - c.stringWidth("A", "Helvetica-Bold", 22)) / 2
    y_text = 740 + (40 - 22) / 2  # 22 is font size
    c.setFont("Helvetica-Bold", 22)
    c.drawString(x_text, y_text, "C")

    # Datos fiscales
    c.setFont("Helvetica-Bold", 14)
    c.drawString(350,770, "FACTURA")
    c.drawString(350,755, "N° 00010000")
    c.drawString(350,740, "Fecha: 28/02/2024")
    c.setFont("Helvetica", 12)
    c.drawString(350,680, "CUIT: 203649996978")
    c.drawString(350,665, "Ing. Brutos: 203649996978")
    c.drawString(350,650, "Inicio de act. 02/12/1995")


    c.line(50, 620, 550, 620)  # (x1, y1, x2, y2)
    c.line(300, 800, 300, 620)  # (x1, y1, x2, y2)
    c.line(50, 800, 550, 800)  # (x1, y1, x2, y2)

    # Client
    c.setFont("Helvetica", 12)
    c.drawString(50, 600, "Señor/es: PARDO LEANDRO - TRANSPORTE RESISTIRE")
    c.drawString(50, 585, "Domicilio: SAAVEDRA 910")
    c.drawString(350, 585, "Localidad: DOLORES")
    c.drawString(50, 570, "CUIT: 20388368102. Monotributo")
    c.drawString(350, 570, "Tel: 2245-508392")
    c.drawString(50, 555, "Cond. Venta: CTA CTE.")
    c.drawString(350, 555, "Vto: 28/02/2024")
    c.drawString(50, 540, "Vendedor: JUANITO LAGUNA (002)")
   
    c.line(50, 525, 550, 525)  # (x1, y1, x2, y2)


    # Productos
    # Cantidad, Descripcion, P. Unit. % Desc, Importe
    # Header de la tabla:
    c.line(50,510,550,510)
    c.line(50,485,550,485)
    c.line(50,510,50,485)
    c.line(550,510,550,485)

    c.setFont("Helvetica-Bold", 12)
    x_cant = 55
    x_description = 92
    x_p_unit = 386
    x_discount = 434
    x_import = 490
    c.drawString(55,492,"Cant")
    c.line(86,510,86,485) # Separador 1
    c.drawString(92,492,"Descripción")
    c.line(381,510,381,485) # Separador 2
    c.drawString(386,492,"P Unit.")
    c.line(429,510,429,485) # Separador 3
    c.drawString(434,492,"% Desc.")
    c.line(485,510,485,485) # Separador 4
    c.drawString(490,492,"Importe")
    c.line(485,510,485,485) # Separador
    # print(55 + 5 + c.stringWidth("Cant", "Helvetica-Bold", 12))

    # Productos
    c.setFont('Helvetica', 12)
    y_product = 470
    for i in range (20):
        c.drawString(x_cant, y_product, "10")
        c.drawString(x_description, y_product, "Pal. Agua economico Frutilla")
        c.drawString(x_p_unit, y_product, "10")
        c.drawString(x_discount, y_product, "0")
        c.drawString(x_import, y_product, "$100")
        y_product = y_product - 15

    c.line(50,160,550,160)

    # Totales
    totales = [
        dict(text=f"Subtotal: $1000",
             font="Helvetica",
             size=12,
             margin_up= 15),
        dict(text="Descuento: $0",
             font="Helvetica",
             size=12,
             margin_up=15),
        dict(text="TOTAL: $1000",
             font="Helvetica-Bold",
             size=16,
             margin_up=20),
    ]
    y_product = 100


    for i in totales:
        y_product = y_product - i['margin_up']
        width = c.stringWidth(i['text'],i['font'],i['size'])
        c.setFont(i['font'], i["size"])
        c.drawString(555-width, y_product, i['text'])   

    
    # Save the canvas to the PDF file
    c.save()

