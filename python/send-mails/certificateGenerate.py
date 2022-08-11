from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

"""
    Método que faz a criação de um certificado em pdf com base em um template e um
    texto

    @param name: Nome do proprietário do certificado
    @param text: Texto que será imprimido no PDF
    @param templateName: nome do template, com a extensão
    @param count: numero usado para criar um nome único para o pdf

    @return: o nome do pdf
"""
def certificateGenerate(
    name: str,
    text: str,
    templateName: str,
    count: int
) -> str:
    fileName = "cert_"+ name.replace(" ", "_").lower() + str(count) + ".pdf"

    lines = []
    
    i = 0
    line = ""
    for char in text:
        line += char
        if i > 90:
            if  char == " ":
                lines.append(line)
                line = ""
                i = 0
        i+=1
    if line != "":
        lines.append(line)

    cv = canvas.Canvas("certificates/"+fileName,pagesize=(297*mm,210*mm))
    cv.drawImage("templates/"+templateName,0,0,width=842,height=596)

    positionY = 298
    for line in lines:
        cv.drawCentredString(x=421,y=positionY,text=line, charSpace=1)
        positionY -= 12

    cv.drawCentredString(x=421,y=positionY-24,text="Feira de Santana - BA, 10 de Agosto de 2022.")
    cv.save()
    return fileName