#!/usr/bin/env python
#
# Erstellt ein neues Scribus Dokument,
# und importiert jedes Bild aus einem Verzeichnis
# auf eine eigene A4 Seite in der Groesse A4 
#
# (c) Robert Johnen

# Importiere Funktionsbibliothemen und pruefe, ob das Script in Scribus ausgefuehrt wurde
import os, sys
try:
    from scribus import *
# wenn nicht in Scribus, dann Script beenden
except ImportError:
    print ("Dieses Script laeuft nur unter Scribus")
    print ("Oeffnen sie Scribus und waehlen Sie: Script(er)->Script ausfuehren...")
    sys.exit(1)

# Dateitypen zum Importieren auflisten
filetype = []
dicttype = {'j':'.jpg','p':'.png','t':'.tif','g':'.gif','P':'.pdf','J':'.jpeg'}
Dicttype = {'j':'.JPG','p':'.PNG','t':'.TIF','g':'.GIF','P':'.PDF','J':'.JPEG'}

# Verzeichnisname holen, in dem die Dateien liegen
imagedir = valueDialog('Bildver','Vollstaendigen Pfad des Bildverzeichnisses angeben (z.B. /home/user/Bilder)')
# Dateityp der Bilder erfragen
imagetype = valueDialog('Dateityp der Bilder','Dateityp der Bilder angeben:\n j=jpg,J=jpeg,p=png,t=tif,g=gif,P=pdf\n "jJptgP" waehlt alle','jJptgP')

# Dateitypen auflisten
for t in imagetype[0:]:
    filetype.append(dicttype[t])
    filetype.append(Dicttype[t])

# im angegebenen Verzeichnis Namen aller Bilder in ein Array einlesen
D=[]
d = os.listdir(imagedir)
for file in d:
    for format in filetype:
        if file.endswith(format):
            D.append(file)
# Sortiere nach Standard (Name)
D.sort()

# Koordinate der oberen linken Ecke des Bildframes auf jeder Seite 
xpos = 0
ypos = 0
# Breite und Hoehe des Bildes in pt (DTP-Punkt) 1pt = 0,352mm
# Format A4 (210mmx297mm / b x h)
# Der Wert ergeben sich sich aus folgenden Formeln:
# width: Aufrunden(210mm/0,352mm), heigth: Aufrunden(297mm/0,352mm)
width = 597
heigth = 844

# Zaehlvariable initialisieren
imagecount = 0
# Wenn im das Array der Dateinamen mindestens einen Namen enthaelt
if len(D) > 0:
    # dann lege ein neues Dokument an
    if newDoc(PAPER_A4, (0,0,0,0),PORTRAIT, 1, UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT):
        # ist die Zaehlvariable kleiner als die Bildanzahl im Array
        while imagecount < len(D):
            # erstelle einen Bildrahmen auf der aktiven Seite an Position x,y
            f = createImage(0, 0, 597, 844)
            # Lade Bild aus Verzeichnis mit dem Namen aus dem Array im erstellten imageframe
            loadImage(imagedir + '/' + D[imagecount], f)
            # skaliere Bild proportional auf Framegroesse
            setScaleImageToFrame(scaletoframe=1, proportional=1, name=f)
            # erhoehe den Zaehler fuer das naechste Bild
            imagecount = imagecount + 1
            # solange imagecount kleiner als Bildanzahl im Array
            if imagecount < len(D):
               # erstelle eine neue Seite und mache diese zur aktiven Seite
                newPage(-1)
    # Zeichne den Bildschirminhalt neu
    setRedraw(1)
    redrawAll()
# Wenn kein Name im Bildarray
else:
    # Fehlermeldung ausgeben
    result = messageBox ('Nichts gefunden','Es wurden keine\nBilder gefunden',BUTTON_OK)
