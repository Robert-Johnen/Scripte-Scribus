#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
### Dieses Script ersetzt den Dateinamen eine Bildes
### durch einen Variablenname, nach dem Schema %VAR_[Objektname]%
### der vom Scribusgenerator genutzt werden kann.
###
### (c) Robert Johnen
"""
import os, sys
try:
    import scribus
except ImportError:
    print("Dieses Script läuft nur in Verbindung mit Scribus.")
    sys.exit(1)

def main():
    # haben wir ein Dokument geoeffnet
    if scribus.haveDoc():
        # haben wir in diesem Dokument genau *ein* Objekt markiert
        if (scribus.selectionCount()==1):
            # Ist dieses Objekt ein Bild, dann
            if (scribus.getObjectType()=="ImageFrame"):
                # lese den vollstaendigen Namen der datei (inkl. Pfad) in die Variable name
                name=scribus.getImageFile()
                # bastele einen neuen Namen aus dem Pfad, %VAR_ und dem Objektnamen und schreibe ihn als Standardwert in den Dialog
                newname=scribus.valueDialog(os.path.split(name)[1]+" wird ersetzt durch %VAR_[name]%","Variablenname ergänzen: ", os.path.split(name)[0]+"/%VAR_"+scribus.getSelectedObject()+"%")
                # uebernehme den Wert aus dem Dialogfenster (keine plausibilitaetspruefung. das ist ein beliebiger String
                scribus.loadImage(newname)
            else:
                scribus.messageBox("Fehler","markierter Frame ist kein Bildrahmen", scribus.ICON_CRITICAL)
        else:
            scribus.messageBox("Fehler","bitte *einen* Bildrahmen markieren", scribus.ICON_CRITICAL)
    else:
        scribus.messageBox("Fehler","kein Dokument geöffnet", scribus.ICON_CRITICAL)
        
if __name__ == '__main__':
    main()
