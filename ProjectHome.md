


# The project development has been moved on [SourceForge](https://sourceforge.net/projects/pygerber2gcode/) #
Google code will be [close](http://google-opensource.blogspot.jp/2015/03/farewell-to-google-code.html).

Google codeが閉鎖するので[SourceForge](https://sourceforge.net/projects/pygerber2gcode/)に移動します。

# Alternative programs #
  * [FlatCAM](http://flatcam.org/)
  * [PCB to Gcode](https://sourceforge.net/projects/pcb2gcode/)

---

[日本語ページ (Japanese page)](http://eng.homuzorow.net/pyGerber2Gcode.html)

pyGerber2Gcode is a Pyhon based Gerber to G-code converter. It works on many operating systems (Linux, Windows ...) which provide Python.

This program is tested with [KiCAD](http://kicad.sourceforge.net/) Gerber data.
But you can use this program for other Gerber data.

# Features #
  * Read Gerber data and convert to G code data
  * Generate contour boundary of pattern and filled zone (polygon zone is recommended).
  * Read and convert Drill data and Edge Cutting data
    * Use endmill for drill and edge Cutting
    * If you want to use normal drill bit, set drill diameter to larger than maximum drill hole diameter.
  * Multi-Scrape to remove unnecessary copper area
  * Mirroring and Rotating also support

# Program File #
[Sourcefroge](https://sourceforge.net/projects/pygerber2gcode/files/current/)
  * File server is changed.
# Requirements #
  * [Shapely](https://pypi.python.org/pypi/Shapely)
  * [wxPython](http://wxpython.org/) for GUI version
  * [matplotlib](http://matplotlib.org/) for CUI version (Quick look)
    * mtplotlib requires
      * numpy
      * six
      * dateutil (python-dateutil)
      * pyparsing
# Attention #
  * Many calculation processes (ex. rotation, zoom, fit to window and so on) use "Front" data.  If you have no "Front" data, you have to read "Back" data as a "Front" data. Maybe it needs change the extension of the "Back" data file to ".gtl" or change "Front" data file extension (GERBER\_EXT) .
# [Install](https://code.google.com/p/pygerber2gcode/wiki/Install) #

# Examples #
## Gerber data ##
### All layer ###
![https://lh3.googleusercontent.com/-syNOnxRJvGc/U_I1fbMwjVI/AAAAAAAAAIo/b1cMmIPDBow/w617-h644-no/gerber1.png](https://lh3.googleusercontent.com/-syNOnxRJvGc/U_I1fbMwjVI/AAAAAAAAAIo/b1cMmIPDBow/w617-h644-no/gerber1.png)
### Front only ###
![https://lh6.googleusercontent.com/-4in6-bWif_c/U_I1fnoK0uI/AAAAAAAAAIw/EYP9i_jXUec/w573-h603-no/gerber_front.png](https://lh6.googleusercontent.com/-4in6-bWif_c/U_I1fnoK0uI/AAAAAAAAAIw/EYP9i_jXUec/w573-h603-no/gerber_front.png)
## Read front pattern,backside pattern, drill data and edge data ##
![https://lh6.googleusercontent.com/-PZJRONQPlIs/U_I1eZqnR2I/AAAAAAAAAIQ/jNtdAmhTrM0/w1004-h777-no/all.png](https://lh6.googleusercontent.com/-PZJRONQPlIs/U_I1eZqnR2I/AAAAAAAAAIQ/jNtdAmhTrM0/w1004-h777-no/all.png)
## Generated contour pattern (Multi-scrape) ##
![https://lh5.googleusercontent.com/-v-u6Ja0SCco/U_I1egeNNOI/AAAAAAAAAIc/Nm5b_ySoLPA/w1004-h777-no/all_cut.png](https://lh5.googleusercontent.com/-v-u6Ja0SCco/U_I1egeNNOI/AAAAAAAAAIc/Nm5b_ySoLPA/w1004-h777-no/all_cut.png)
## Zoom up ##
### gerberdata ###
![https://lh6.googleusercontent.com/-RSPqS2gdBqM/U_I1gKNBXtI/AAAAAAAAAI4/744FHlHwN4k/w1225-h739-no/gerber_front_zoom.png](https://lh6.googleusercontent.com/-RSPqS2gdBqM/U_I1gKNBXtI/AAAAAAAAAI4/744FHlHwN4k/w1225-h739-no/gerber_front_zoom.png)
### Contour patterna ###
![https://lh6.googleusercontent.com/-ToEHI5wiR8Y/U_I1fIT0w0I/AAAAAAAAAIg/EbdHd-vuOLA/w1004-h777-no/front_cut_zoom.png](https://lh6.googleusercontent.com/-ToEHI5wiR8Y/U_I1fIT0w0I/AAAAAAAAAIg/EbdHd-vuOLA/w1004-h777-no/front_cut_zoom.png)