#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
###------------------------------------------------------------------------------------#
###
### Aufruf: 
### ~$> python3 000_Verzeichnisstruktur_anlegen.py -q QuellVrz -r StammVrz -d NameZielVrz -r RohdatenVrz
###
### Dieses Script legt im Zielverzeichnis <StammVrz/NameZielVRZ> eine Verzeichnisstruktur, 
### die in <QuellVrz> vorgegeben ist, mit de Inhalten aus <RohdatenVrz> an
### Es erscheint auf jeden Fall ein Dialog, in welchem die eingegebenen Parameter 
### beim Klick auf [OK] ueberprueft werden.
### Das Script kann sowohl innerhalb, als auch außerhalb von Scribus aufgerufen werden.
### Wird das Script innerhalb von Scribus aufgerufen und ist ein Dokument geoeffnet,
### wird dieses Dokument im Wurzelverzeichnis der neuen Verzeichnisstruktur gespeichert.
### Ist Scribus nicht aktiv, wird nach dem Anlegen der Verzeichnisstruktur Scribus gestartet.
###
### Kommandozeilenparameter (alle Parameter sind optional):
###
### -q QuellverzeichnisDatenstruktur : Das Verzeichnis, welches die Verzeichnis-
###                                    struktur fuer die neue Datenablage enthaelt
### -z Stammverzeichnis : Das Stammverzeichnis, in welchem das neue Datenverzeichnis
###                       angelegt werden soll
### -d Zeielverzeichnis : Der Name des neu anzulegenden Datenverzeichnisses
### -r Rohdatenverzeichnis : das Verzeichnis, das die einzukopierenden Daten enthaelt
###
### (c) Robert Johnen
###------------------------------------------------------------------------------------#
"""

###------------------------------------------------------------------------------------#
#----------------------------- Importierte Bibliotheken -------------------------------#
###------------------------------------------------------------------------------------#
# 
import sys, shutil, os, getopt
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog

#try:
#    import scribus
#except ImportError:
#    print('Dieses Script läuft nur in Scribus')
#    sys.exit(1)


###------------------------------------------------------------------------------------#
#----------------------- Deklaration von globalen Konstanten --------------------------#
###------------------------------------------------------------------------------------#
#
# hier definiere ich, dass bei dem Versuch eine der unter 
# _const angegeben Konstanten zu aendern ein TypeError erscheint.
def constant(name):
    def fset(self,value):       # kein veraendern des Wertes moeglich
        raise TypeError
    def fget(self):             # Abfragen geht
        return name()
    return property(fget,fset)  # Methoden des Objektes festlegen

# hier lege ich die Konstanten als Unterprogramme mit
# festem Rueckgabewert in einer Klasse an
class _const(object):
    @constant
    def SCRIPTNAME(): return sys.argv[0]
    @constant
    def PARAMETERLISTE(): return sys.argv
    @constant
    def PARAMETERZAHL(): return len(sys.argv)
    @constant
    def HOME(): return os.getenv("HOME")
    @constant
    def QUELLVERZEICHNIS(): return "Oeffentlich/Vorlagen/scribus/NEU"
    @constant
    def ZIELVERZEICHNIS(): return "Dokumente/Layoutdaten"
    @constant
    def DATENVERZEICNIS(): return "NEU"
    @constant
    def ROHDATENVERZEICHNIS(): return "Dokumente/AuW/MTD@work/Pruefungsvorbereitung"

# ab hier koennen meine Konstanten mit
# myC.KONSTANTENNAME referenziert werden
myC = _const()

###------------------------------------------------------------------------------------#
#----------- Deklaration von Variablen, Klassen, Dictionarys und Funktionen -----------#
###------------------------------------------------------------------------------------#
# 
def ife(testausdruck, ergebnis_if,  ergebnis_else):
    """Ein schnelles, kurzes if """
    if (testausdruck):      # wenn testausdruck wahr,
        return ergebnis_if  # dann gebe ergebnis_if zurueck
    return ergebnis_else    # wenn nicht, dann ergebnis_else

def inc(wert):
    """schnelle Addition"""
    wert += 1       # erhoeht wert um 1
    return wert     # und gibt ihn zurueck

def dec(wert):
    """schnelle Subtraktion"""
    wert -= 1       # vermindert wert um 1
    return wert     # und gibt ihn zurueck

# eine allgemeine Zaehlvariable
zaehler = 0

### Standardwerte festlegen
class _datenObjekt():
    # Datenklasse anlegen und bei Zuweisung immer mit Stadardwerten referenzieren
    def __init__(self):
        # erste Zuweisung, falls keine Parameter angegeben wurden
        self.quellVerzeichnis=myC.HOME+"/"+myC.QUELLVERZEICHNIS
        self.zielVerzeichnis=myC.HOME+"/"+myC.ZIELVERZEICHNIS
        self.datenVerzeichnis="NEU"
        self.rohdatenVerzeichnis=myC.HOME+"/"+myC.ROHDATENVERZEICHNIS
        # testen auf falsche Parameter
        try:
            __opts, __args = getopt.getopt(sys.argv[1:], "hq:z:d:r:", ["quellvb=", "zielvb=", "neuverz=", "rohdatenverz="])
        except getopt.GetoptError:
            # wenn nur *ein* Parameter falsch ist, sage wie es richtig geht...
            print("Aufruf: ", myC.SCRIPTNAME, "-q /Quelle/fuer/Verzeichnisbaum -z /Stammverzeichnis/Ziel -d NameNeuesVerzeichnis -r /Verzeichnis/mit/Rohdaten")
            # und beende dich mit Fehlercode
            sys.exit(2)
        # wenn Parameter angegeben wurden, dann ersetzte die Standardwerte mit den angegeben Werten im Parameter
        for __opt,  __arg in __opts:
            if __opt == '-h': 
                # Parameter -h = Hilfe
                print("Aufruf: ", myC.SCRIPTNAME, "-q /Quelle/fuer/Verzeichnisbaum -z /Stammverzeichnis/Ziel -d NameNeuesVerzeichnis -r /Verzeichnis/mit/Rohdaten")
                # nach Hilfe exit
                sys.exit()
            # Parameter -q angegeben ersetze Quellverzeichnis mit Parameter
            elif __opt in ('-q', '--quellvb'):
                self.quellVerzeichnis=__arg
            # Parameter -q angegeben ersetze zielVerzeichnis mit Parameter (Stammverzeichnis)
            elif __opt in ('-z', '--zielvb'):
                self.zielVerzeichnis=__arg
            # Parameter -q angegeben ersetze datenVerzeichnis mit Parameter (Zielverzeichnisname)
            elif __opt in ('-d', '--neuverz'):
                self.datenVerzeichnis=__arg
            # Parameter -q angegeben ersetze rohdatenVerzeichnis mit Parameter
            elif __opt in ('-r', '--rohdatenverz'):
                self.rohdatenVerzeichnis=__arg

std=_datenObjekt()

class _mainWindow():
    # initialisiere den Konstruktor fuer die grafische Oberflaeche
    def __init__(self):    
        self.root=tk.Tk()
        # initialisiere und setze Variablen, die innerhalb der grafischen Oberflaeche genutzt werden
        # keine dieser Variablen soll direkt von aussen ansprechbar sein, deswegen self.__
        self.__fehler=False
        self.__quellVerzeichnis=tk.StringVar()
        self.__quellVerzeichnis.set(std.quellVerzeichnis)
        self.__zielVerzeichnis=tk.StringVar()
        self.__zielVerzeichnis.set(std.zielVerzeichnis)
        self.__datenVerzeichnis=tk.StringVar()
        self.__datenVerzeichnis.set(std.datenVerzeichnis)
        self.__rohdatenVerzeichnis=tk.StringVar()
        self.__rohdatenVerzeichnis.set(std.rohdatenVerzeichnis)
        self.__schliesseDialog=tk.IntVar()
        self.__schliesseDialog.set(1)
        # Meine bevorzugte Loesung fuer den Aufbau eines Dialoge ist grid()
        # dafuer lege ich hier ein paar Standardwerte fest
        self.__gridZeile = 0                # Anfangszeile
        self.__gridSpalte = 0               # Anfangsspalte
        self.__gridPadx = 10                # Abstand Text bzw Eingabeelement zum Zellenrand oben und unten
        self.__gridPady = 10                # Abstand Text bzw Eingabeelement zum Zellenrand rechts und links
        # Laenge der Eingabefelder
        self.__entryWidth=70
        # Farben des Dialogs und der Widgets definieren
        self.__colorBg="#f0f0f0"            # Standardhintergrund
        self.__colorFg="#000000"            # Standardvordergrund (Schriftfarbe)
        self.__colorOk="#00ff00"            # Hintergrund wenn ok
        self.__colorErr="#ff0000"           # Hintergrund bei Fehleingabe
        self.__colorBgEntry="#ffffff"       # Hintergrund Eingabefeld
        # Standardschrift der Widgets definieren
        self.__fontSize = 10                # Schriftgroesse
        self.__fontFamily = 'sans serif'    # Schriftart
        self.__fontWeight = tkFont.NORMAL   # Schriftschnitt
        # Fenster mit Fenstertitel, Hintergrund und Groesse
        self.__windowTitle = "Fenster von " + myC.SCRIPTNAME
        self.root.title(self.__windowTitle)
        self.root.configure(bg=self.__colorBg)
        #self.root.geometry('300x200') # Fenstergroesse festlegen
        self.root.resizable(0, 0)   # auskommentieren, dann ist Fenstergroesse fix
        # Schrift definieren
        self.__fontDo=tkFont.Font(family=self.__fontFamily,  size=self.__fontSize,  weight=self.__fontWeight)

        ### Fensterbestandteile und Layout erstellen (meine bevorzugte Loesung ist .grid())
        # Beschriftung ueber Eingabefeld Quellverzeichnis
        self.tkqVLabel=tk.Label(self.root, text="\n(Q)uellverzeichnis des anzulegenden Verzeichnisbaums angeben:", fg=self.__colorFg, font=self.__fontDo)
        # Position Beschriftung im Grid
        self.tkqVLabel.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # fuers Grid jetzt in die naechste Zeile 
        self.__gridZeile+=1
        # Eingabefeld Quellverzeichnis
        self.tkqVEntry=tk.Entry(self.root, text=self.__quellVerzeichnis, fg=self.__colorFg, bg=self.__colorBgEntry, font=self.__fontDo, width=self.__entryWidth)
        # Position Eingabefeld im Grid
        self.tkqVEntry.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # Button fuer Suchdialog Quellverzeichnis
        self.tkqVButton=tk.Button(self.root, text="suchen", command=self.tkqVButtonhandler, font=self.__fontDo, fg=self.__colorFg)
        # Position Button im grid
        self.tkqVButton.grid(column=self.__gridSpalte+1, row=self.__gridZeile, padx=self.__gridPadx)
        # Tastenkombination fuer Suchdialog Quellverzeichnis
        self.root.bind('<Alt-q>', self.tkqVButtonhandler)

        # fuers Grid jetzt in die naechste Zeile 
        self.__gridZeile+=1
        # Beschriftung Eingabefeld Zielverzeichnis
        self.tkzVLabel=tk.Label(self.root, text="\n(S)tammverzeichnis für neues Datenverzeichnis angeben:", fg=self.__colorFg, font=self.__fontDo)
        # Position im Grid
        self.tkzVLabel.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # fuers Grid jetzt in die naechste Zeile 
        self.__gridZeile+=1
        # Eingabefeld Zielverzeichnis
        self.tkzVEntry=tk.Entry(self.root, text=self.__zielVerzeichnis, fg=self.__colorFg, bg=self.__colorBgEntry, font=self.__fontDo, width=self.__entryWidth)
        # Position Eingabefeld im Grid
        self.tkzVEntry.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # Button fuer Suchdialog Zielverzeichnis
        self.tkzVButton=tk.Button(self.root, text="suchen", command=self.tkzVButtonhandler, font=self.__fontDo, fg=self.__colorFg)
        # Position Button im grid
        self.tkzVButton.grid(column=self.__gridSpalte+1, row=self.__gridZeile, padx=self.__gridPadx)
        # Tastenkombination fuer Suchdialog Zielverzeichnis+Eventhandler
        self.root.bind('<Alt-s>', self.tkzVButtonhandler)

        # fuers grid in die naechste Zeile
        self.__gridZeile+=1
        # Beschriftung Eingabefeld  Datenverzeichnis
        self.tkdVLabel=tk.Label(self.root, text="\n(N)ame für neues Datenverzeichnis angeben:", font=self.__fontDo, fg=self.__colorFg)
        # Position Beschriftung Eingabefeld datenverzeichnis im grid
        self.tkdVLabel.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # naechste Zeile im Grid
        self.__gridZeile+=1
        # Eingabefeld Datenverzeichnis
        self.tkdVEntry=tk.Entry(self.root, text=self.__datenVerzeichnis,  bg=self.__colorBgEntry, fg=self.__colorFg, font=self.__fontDo, width=self.__entryWidth)
        # Position Eingabefeld Datenverzeichnis im grid
        self.tkdVEntry.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # Tastenkombination fuer Eingabefeld+Eventhandler
        self.root.bind('<Alt-n>', self.tkdVEntryHandler)

        # naechste zeile im grid
        self.__gridZeile+=1
        # Beschriftung Eingabefeld Rohdatenverzeichnis
        self.tkrVLabel=tk.Label(self.root, text="\n(V)erzeichnis der Roh- bzw. Ursprungsdaten:", font=self.__fontDo, fg=self.__colorFg)
        # Position Beschriftung Eingabefeld Rohdatenverzeichnis im Grid
        self.tkrVLabel.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")
        # nachste zeile im Grid
        self.__gridZeile+=1
        # Eingabefeld Rohdatenverzeichnis
        self.tkrVEntry=tk.Entry(self.root, text=self.__rohdatenVerzeichnis,  bg=self.__colorBgEntry, fg=self.__colorFg, font=self.__fontDo, width=self.__entryWidth)
        # Position Eingabefeld Rohdatenverzeichnis im grid
        self.tkrVEntry.grid(column=self.__gridSpalte, row=self.__gridZeile, padx=self.__gridPadx, sticky="w")

        # Button fuer Suchdialog Rohdatenverzeichnis mit Handler definieren
        self.tkrVButton=tk.Button(self.root, text="suchen", command=self.tkrVButtonhandler, font=self.__fontDo, fg=self.__colorFg)
        # Position Button im Grid
        self.tkrVButton.grid(column=self.__gridSpalte+1, row=self.__gridZeile, padx=self.__gridPadx)
        # Tastenkombination fuer Suchdialog + Eventhandler
        self.root.bind('<Alt-v>', self.tkzVButtonhandler)
        # naechste zeile im Grid
        self.__gridZeile+=1
        # noch eine Zeile mehr (obwohl leere zeilen im Grid nicht angezeigt werden ;-)
        (self.__gridZeile, self.__gridSpalte) = (inc(self.__gridZeile), 0)

        # OK-Button+Handler, Checkbox+Handler und Cancel-Button+Handler definieren
        # sind alle in einer Zeile
        self.okButton=tk.Button(self.root, width=8, height=1, text="OK", font=self.__fontDo, fg=self.__colorFg, command=self.OKButtonHandler)
        # Position OK-Button im grid
        self.okButton.grid(row=self.__gridZeile, column=self.__gridSpalte, pady=self.__gridPady, padx=self.__gridPadx, sticky="w")
        # Tastenkombination OK
        self.root.bind('<Alt-Return>', self.OKButtonHandler)

        # Checkbutton mit Beschriftung
        self.closeCheckbutton=tk.Checkbutton(self.root, text="(D)ialog nach Klick auf [OK] schließen.", font=self.__fontDo, fg=self.__colorFg, variable=self.__schliesseDialog)
        # kleine Trickserei im Grid: ich habe zwar nur zwei Spalten im Grind, aber duch das
        # columspan in der Positionierung fasse ich beide Spalten zusammen und positioniere die Checkbox
        # in der Mitte ohne eine eigene Spalte dafuer zu definieren (eine extra Spalte wuerde das Layout auseinanderreissen)
        self.closeCheckbutton.grid(row=self.__gridZeile, column=self.__gridSpalte, columnspan=2, pady=self.__gridPady, padx=self.__gridPadx)
        # Tastenkombi fuer Checkbox
        self.root.bind('<Alt-d>', self.CloseCheckbuttonHandler)

        # 2. Spalte
        self.__gridSpalte=1
        # Cancel-Button und Buttonhandler festlegen
        self.cancelButton=tk.Button(self.root, width=8, height=1, text="Abbrechen", font=self.__fontDo, command=self.CancelButtonHandler)
        # Position Cancelbutton im grid
        self.cancelButton.grid(row=self.__gridZeile, column=self.__gridSpalte, pady=self.__gridPady, padx=self.__gridPadx, sticky="e")
        # Tastenkombination Cancel-Button
        self.root.bind('<Escape>', self.CancelButtonHandler)

        # Eingabefokus auf Zielverzeichnis
        self.tkdVEntry.focus_set()
        # komplettes Eingabefeld auswaehlen (bei Eingabe wird der Text dann direkt ersetzt)
        self.tkdVEntry.select_range(0, tk.END)

        ### Fenster aufbauen
        self.root.mainloop()
        
    def tkdVEntryHandler(self, *event):
        """Handler fuer Eingabe des Datenverzeichnisses"""
        # Fokus setzen
        self.tkdVEntry.focus_set()
        # Inhalt markieren
        self.tkdVEntry.select_range(0, tk.END)
        
    def CloseCheckbuttonHandler(self, *event):
        """Handler fuer Checkbutton Dialog schliessen oder nicht"""
        # aktuellen wert holen
        ergebnis=self.__schliesseDialog.get()
        # aktuellen Wert umkehren
        self.__schliesseDialog.set(ife((ergebnis==1), 0, 1))
        
    def tkqVButtonhandler(self, *event):
        """Handler fuer Button suche Quellverzeichnis"""
        # Initialen Wert holen
        initdir=self.__quellVerzeichnis.get()
        # Dateidialog oeffnen mit Start im initialen Verzeichnis
        ergebnis=tkFileDialog.askdirectory(title="Quellverzeichnis wählen", initialdir=initdir)
        # neuen Wert setzen
        self.__quellVerzeichnis.set(ife((ergebnis==""), initdir, ergebnis))
   
    def tkrVButtonhandler(self, *event):
        """Handler fuer Button suche Quellverzeichnis"""
        # Initiales Verzeichnis holen
        initdir=self.__rohdatenVerzeichnis.get()
        # Dateidialog oeffnen
        ergebnis=tkFileDialog.askdirectory(title="Roh- bzw. Ursprungsdatenverzeichnis wählen", initialdir=initdir)
        # neuen Wert setzen
        self.__rohdatenVerzeichnis.set(ife((ergebnis==""), initdir, ergebnis))
        
    def tkzVButtonhandler(self, *event):
        """Handler fuer Button suche Stamm- bzw Zielverzeichnis"""
        # initiales Verzeichnis holen
        initdir=self.__zielVerzeichnis.get()
        # dateidialog oeffnen
        ergebnis=tkFileDialog.askdirectory(title="Stammverzeichnis wählen", initialdir=initdir)
        # neues verzeichnis setzen
        self.__zielVerzeichnis.set(ife((ergebnis==""), initdir, ergebnis))
        
    def OKButtonHandler(self, *event):
        """Handler fuer OK-Button"""
        # noch kein Fehler aufgetreten
        self.__Fehler=False
        # Hintergrundfarbe der Labels fuer die Ueberpruefung auf Standard setzen
        self.tkqVLabel["background"]=self.__colorBg
        self.tkzVLabel["background"]=self.__colorBg
        self.tkrVLabel["background"]=self.__colorBg
        # Variablen auslesen und in standard speichern
        std.quellVerzeichnis=self.__quellVerzeichnis.get()
        std.zielVerzeichnis=self.__zielVerzeichnis.get()
        std.datenVerzeichnis=self.__datenVerzeichnis.get()
        std.rohdatenVerzeichnis=self.__rohdatenVerzeichnis.get()
        # pruefen ob Quellverzeichnis existiert
        if not(os.path.isdir(std.quellVerzeichnis)):
            # wenn nicht, Labelhintergrund auf Fehlerfarbe
            self.tkqVLabel["background"]=self.__colorErr
            # Fehler ist passiert
            self.__Fehler=True
        # pruefen ob Stammverzeichnis (Ziel) existiert
        if not(os.path.isdir(std.zielVerzeichnis)):
            # wenn nicht, Labelhintergrund auf Fehlerfarbe
            self.tkzVLabel["background"]=self.__colorErr
            # Fehler ist passiert
            self.__Fehler=True
        # pruefen, ob Rohdatenverzeichnis existiert
        if not(os.path.isdir(std.rohdatenVerzeichnis)):
            # wenn nicht, Labelhintergrund auf Fehlerfarbe
            self.tkrVLabel["background"]=self.__colorErr
            # Fehler ist passiert
            self.__Fehler=True
        # wenn Fehler aufgetaucht, dann
        if self.__Fehler:
            # Nachricht und zurueck in das Dialogfeld
            tkMessageBox.showerror("Fehler", "Rot markierte Verzeichnisse existieren nicht!")
            return
        # fragen, wenn existentes Verzeichnis ueberschrieben werden soll
        if os.path.isdir(std.zielVerzeichnis+"/"+std.datenVerzeichnis):
            weiter=tkMessageBox.askyesno("Fehler", "Das Datenverzeichnis existiert bereits im Verzeichnisbaum!\nevtl. vorhandene Daten könnten überschrieben werden.\n\nFortfahren?")
            # wenn nicht, zurueck in das Dialogfeld
            if not(weiter): return
        # fragen, wenn Datei gleichen Namens bereits existiert ob Dtei geloescht werden soll    
        if os.path.isfile(std.zielVerzeichnis+"/"+std.datenVerzeichnis):
            weiter=tkMessageBox.askyesno("Fehler", "Eine Datei gleichen Namens wie das Datenverzeichnis existiert bereits im Verzeichnisbaum!\n\nLöschen?")
            # wenn nicht, dann zurueck in das Dialogfeld
            if not(weiter): return
            # ansonsten versuche die Datei zu loeschen
            try:
                os.path.rm(std.zielVerzeichnis+"/"+std.datenVerzeichnis)
            except:
                # Fehler beim loeschen, Fehlermeldung und zurueck ins Dialogfeld
                tkMessageBox.showerror("Fehler", "Datei "+std.zielVerzeichnis+"/"+std.datenVerzeichnis+" konnte nicht gelöscht werden.")
                return
        # alle vorherigen Abfragen sind ok gewesen dann
        try:
            # versuche den Verzeichnisbaum anzulegen
            shutil.copytree(std.quellVerzeichnis, std.zielVerzeichnis+"/"+std.datenVerzeichnis, symlinks=False, ignore_dangling_symlinks=True, dirs_exist_ok=True)
        except:
            # ein Fehler ist aufgetreten (Verzeichnis kann trotzdem existieren)
            print("Fehler beim Kopieren der Verzeichnisse (wenn Zielverzeichnis NTFS-Dateisystem: keine Permissions)")
        try:
            # kopiere die Rohdaten ins Zielverzeichnis
            shutil.copytree(std.rohdatenVerzeichnis, std.zielVerzeichnis+"/"+std.datenVerzeichnis+'/Backup/Rohdaten', symlinks=False, ignore_dangling_symlinks=True, dirs_exist_ok=True)
        except:
            # ein Fehler ist aufgetreten (Daten koennen trotzdem kopiert sein)
            print("Fehler beim Kopieren der Rohdaten (wenn Zielverzeichnis NTFS-Dateisystem: keine Permissions)")
#        tkMessageBox.showinfo()
        # Hole den Verzeichnisinhalt und Bilddaten, Videodaten, Audiodaten,
        # Textdaten, Tabellen usw in entsprechende Verzeichnisse
        for root, dirs, files in os.walk(std.zielVerzeichnis+"/"+std.datenVerzeichnis+'/Backup/Rohdaten'):
            for file in files:
                try:
                    if file.endswith((".bmp", ".png", ".tif", ".tiff", ".jpg", ".jpeg", ".jfif", ".psd", ".xcf", ".png", ".gif", ".pdf")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Bilddaten")
                    if file.endswith((".svg", ".ps", ".cdr", ".ai", ".sk1", ".dxf", ".dwg", ".eps", ".lww", ".pdf")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Bilddaten/Grafiken")
                    if file.endswith((".avi", ".mpg", ".mkv", ".mpeg", ".vob")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Bilddaten/Videos")
                    if file.endswith((".icc", ".icm")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Bilddaten/Profile")
                    if file.endswith((".ani", ".flv")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Bilddaten/Animationen")
                    if file.endswith((".txt", ".doc", ".docx", ".docm", ".odt", ".lyx")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Textdaten")
                    if file.endswith((".xls", ".xlsx", ".xlsm", ".csv", ".ods")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Textdaten/Tabellen")
                    if file.endswith((".otf", ".ttf", ".cf1", ".lwf", ".cxf")):
                        shutil.copy(os.path.join(root, file), std.zielVerzeichnis+"/"+std.datenVerzeichnis+"/Textdaten/Schriften")
                except:
                    # Fehler beim kopieren, mache trotzdem weiter
                    print("Fehler beim Kopieren (wenn Zielverzeichnis NTFS-Dateisystem: keine Permissions)")
        # wenn Chckbox Dialog schliessen nach OK, dann
        if self.__schliesseDialog.get():
            # schliesse den Dialog
            self.root.destroy()
        
    def CancelButtonHandler(self, *event):
        """Cancel-Button Handler"""
        # Fenster schliessen
        self.root.destroy()
        # Programm mit Exit-Code verlassen
        sys.exit()

def main():
    """Hauptfunktion des Programmes"""
    # Fenster erzeugen
    app = _mainWindow()
    del app

#--------------------------------------------------------------------------------------#
#------------------------------------ Hauptprogramm -----------------------------------#
#--------------------------------------------------------------------------------------#
# je nach Taetigkeit anderes Feld ausfuehren

if __name__ == "__main__":
    # Hauptfunktion ausfuehren
    main()
    # versuche jetzt Modul scribus zu importiern
    try:
        # klapp nur, wenn Script aus Scribus gestartet wurde
        import scribus
        # teste ob Dokument geoeffnet ist
        if scribus.haveDoc():
            # wenn ja, dann speichere das im Zielverzeichnis
            scribus.saveDocAs(std.zielVerzeichnis+"/"+std.datenVerzeichnis+".sla")
        else:
            # wenn nicht, lege ein neues Dokument an
            scribus.newDoc(std.zielVerzeichnis+"/"+std.datenVerzeichnis+".sla")
    except:
        # sribusmodul konnte nicht importiert werden, dann versuche scribus zu starten
        if (os.system("scribus")):
            # hat nicht geklappt / Fehlermeldung
            print("Scribus konnte nicht gestartet werden")
    # Programm beenden
#    sys.exit()
        

