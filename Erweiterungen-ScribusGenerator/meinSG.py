#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
### Dieses Script starten ein Bashscripr, das den Seriengenerator ueber die Kommandozeile (ein Bash-Script)
### und ueber das CLI-Interface ablaufen laesst. Dies ist ein Wuergaround, da der ScribusGenerator unter 
### Scribus 1.5.5 mit Geld und guten Worten nicht zum funktionieren zu bringen war.
###
### (c) by Robert Johnen
"""
import os, sys, subprocess
try:
    import scribus
except ImportError:
    print("Dieses Script läuft nur in Verbindung mit Scribus.")
    sys.exit(1)

def main():
    # habe ich ein Scribus-Dokument
    if scribus.haveDoc():
        # dann speichere das
        scribus.saveDoc()
        # finde den Namen heraus
        name=scribus.getDocName()
        # nur den Dateinamen, ohne ext
        suchname=os.path.splitext(os.path.split(name)[1])[0]
        # frage nach erstem datensatz
        von=scribus.valueDialog("Daten von","Daten aus "+suchname+".csv werden verarbeitet.\nBeginne bei Datensatz (keine Eingabe = von Anfang an):", "")
        # frage nach letztem datensatz
        bis=scribus.valueDialog("Daten bis","Daten aus "+suchname+".csv werden verarbeitet.\nEnde bei Datensatz (keine Eingabe = bis zum letzten):", "")
        # starte das Bashscript fuer den Seriengenerator
        subprocess.call(['bash', '~/bin/scribus/meinSG', suchname, von, bis])
    else:
        scribus.messageBox("Fehler","kein Dokument geöffnet", scribus.ICON_CRITICAL)
        
if __name__ == '__main__':
    main()
