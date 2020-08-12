# Scripte-Scribus

Scripte und Erweiterungen für das Layoutprogramm Scribus

Erweiterungen-ScribusGenerator - eigene Workarounds zum bei mir nicht funktionierenden
SerienGenerato für Scribus 1.5.5

Verzeichnis_mit_Bildern_auf_A4-Seiten_importieren.py - Erzeugt eine Scribus-Datei aus 
einem Verzeichnis mit Bilddaten. Für jedes Bild wird eine A4-Seite generiert, das 
Bild auf Pos (0, 0) gesetzt und auf A4 skaliert.

Verzeichnisstruktur_anlegen.py - Legt eine Verzeichnisstruktur zur datensortierung an, die ich
unter Scribus nutze. Existiert ein Verzeichnis ~/Vorlagen/scribus/NEU mit entsprechenden 
Unterverzeichnissen wird dieser Verzeichnisbaum als Vorlage genommen, ansonsten wird per 
mkdir -p ein Verzeichnisbaum aus den im Script definierten Variablen erzeugt. Ein Verzeichnis
mit Rohdaten wird ausgelesen und die erkannten Dateitypen werden auf die entsprechenden 
Unterverzeichnisse verteilt.


