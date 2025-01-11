#!/usr/bin/env python3

import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generateReport():
    '''Generate disk free report
    '''
    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE, text=True)
    return p.stdout.readlines()

def createPDF(input, output = "disk_report.pdf"):
    now = datetime.datetime.now()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, 11 * inch)
    textobj.textLine('''
                     Disk Capacity Report: %s
                     ''' % date)
    for line in input:
        textobj.textLine(line.strip())
    c.drawText(textobj)
    c.save()

if __name__ == "__main__":
    report = generateReport()
    createPDF(report)