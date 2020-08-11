#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
### exportiert die geoeffnete Datei mit den zuletzt 
### eingestellten Optionen als PDF
"""

import os,  sys
try:
    import scribus
except ImportError:
    print("Dieses Script benötigt ein laufendes Scribus.")
    sys.exit(1)
    
def main():
    # hole Pfad aus der geoeffneten Datei
    dateiPfad = os.path.split(scribus.getDocName())[0]
    # extrahiere den Dateinamen ohne Erweiterung
    dateiName = os.path.splitext(os.path.basename(scribus.getDocName()))[0]
    # pdf-Objekt erzeugen
    pdf = scribus.PDFfile()
    # PDF-Info fuer Konformitaet PDF-X[34] irgendwas reinschreiben
    pdf.info = "Scribus-Source file -" + dateiName + ".sla - created by Robert Johnen"
    # Dateiname fuer PDF-Objekt festlegen
    pdf.file = dateiPfad + "/" + dateiName + ".pdf"
    # PDF-Objekt speichern
    pdf.save()
    
if __name__ == "__main__":
    if scribus.haveDoc():
        main()
    else:
        scribus.messageBox("Fehler", "Es wird eine geöffnete Scribus-Datei benötigt.")
        sys.exit(1)
    
