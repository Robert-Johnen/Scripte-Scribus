# Erweiterungen zum ScribusGenerator

Diese Scripte hier sind Notlösungen, da der ScribusGenerator mit python3 unter
Scribus Version 1.5.5 (zumindes bei mir) nicht sauber funktioniert.

- meinSG (bash-Script) - nimmt als ersten Parameter den Dateinamen einer Scribus-datei (.sla),
sucht die Datei per locate und wechselt in das Verzeichnis, welches die Datei enthält.
Dort wird im Unterverzeichnis Seriendruckdaten eine .csv mit gleichem Namen erwartet.
Dann wird per ScribusGeneratorCLI.py die Vorlage mit den Seriendruckdaten in einer Datei
zusammengeführt. Danach wird mit Scribus auf einem virtuellen Terminal (per xvfb-run) im Hintergrund mit dem
Script meinSGpdf.py und der zusammengeführten Datei eine PDF erzeugt und in das Unterverzeichnis
Ausgabe verschoben und ein PDF-Betrachter (okular) aufgerufen. Als zweiter Parameter kann noch
die Nummer des Datensatzes angegeben werden, mit dem begonnen werden soll, als dritter Parameter der
Datensatz, mit dem aufgehört werden soll. ScribusGeneratorCLI.py und ScribusGeneratorBackend.py müssen
irgendwo (im gleichen Verzeichnis möglichst) im $HOME des Users liegen

- meinSG.py - macht dasselbe wie oben, aber aus Scribus heraus

- meinSGpdf.py - generiert eine PDF-Datei mit vorher in der Scribus-Datei eingestellten Optionen
(dafür muss mit der Scribus-Datei mindestens einmal eine PDF mit den entsprechenden Einstellungen
erzeugt worden sein). Dieses Script wird für die zwei obigen benötigt.

- meinSGBild2VAR_.py - wenn in Scribus ein Bild markiert ist, wird der Dateiname mit einer
Variablen ersetzt. Diese Variable hat folgendes Schema %VAR_[Objektname]%. Wenn nicht der 
Objektname genommen werden soll, kann dieser Name im Dialog geändert werden.
Die Variable wird dann vom ScribusGeneratorBackend.py mit dem Bildnamen ersetzt, wenn 
in der .csv eine Spalte mit dem Namen [Objektname] existiert. Die Bilder, mit denen 
die Variable ersetzt wird, sollten im gleichen Verzeichnis liegen, wie das Bild, dessen 
Name durch die Variable ersetzt wurde. Bevor das Bild mit der Variablen ersetzt wird, müssen
alle Einstellungen das Bild betreffend (Größe, / an Rahmen anpassen / usw. ) schon
gemacht worden sein. Diese Einstellungen werden dann (für jedes Bild aus der .csv)  übernommen.