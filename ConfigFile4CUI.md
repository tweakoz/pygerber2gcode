# Setting values in "pyg2g\_cui.conf" #

### For Gerber data ###
  * GERBER\_DIR : Gerber date directory
  * FRONT\_FILE : Front pattern data file name
  * BACK\_FILE : Back pattern data file name
  * DRILL\_FILE : Drill pattern data file name
  * EDGE\_FILE : Edge pattern data file name
  * CAD\_UNIT : Unit of the pattern data on the PCB CAD. Default MIL/10 = Inch/10000
  * DRILL\_UNIT : Unit of the drill data on the PCB CAD. Default inch
  * EDGE\_UNIT :  Unit of the edge data on the PCB CAD. Default MIL/10 = Inch/10000
  * IN\_INCH\_FLAG : If the unit of input files are INCH, set 1. Set 0 for MM. Default 1

### For Cutting machine ###
  * SET\_INI : If you want set initial position of the tool (INI\_X, INI\_Y, INI\_Z), set 1. Default 1
  * INI\_X, INI\_Y, INI\_Z : Start (Initial) position of the cutting tool. For example, home position (0,0,0).
  * MOVE\_HEIGHT : Moving height (without cutting).
  * XY\_SPEED : In-plane cutting speed
  * Z\_SPEED : Z axis cutting speed
  * PATTERN\_SHIFT : Set "1" for pattern shift to (LEFT\_X,LOWER\_Y). Default 1
  * LEFT\_X : Left side of the converted G code will be shifted to LEFT\_X.
  * LOWER\_Y : Bottom of the converted G code will be shifted to LOWER\_Y
  * DRILL\_SPEED : Drill down speed.
  * DRILL\_DEPTH : Drill depth.
  * CUT\_DEPTH : Pattern cutting depth.
  * TOOL\_D : Diameter of the cutting tool.
  * DRILL\_D : Drill diameter.
  * EDGE\_TOOL\_D : Edge cutting tool diameter.
  * EDGE\_DEPTH : Edge cutting depth.
  * EDGE\_SPEED : Edge cutting speed.
  * EDGE\_Z\_SPEED : Edge down speed.
  * MERGE\_DRILL\_DATA : If you want to merge drill data and pattern data, set 1. Default 0
  * Z\_STEP : cutting step in z axis.
  * DRILL\_TYPE : If you use endmill for drilling, set 1. When set 1 this flag, large drill (> endmill diameter) holes will be converted to circle cutting. Default 1
### For data convert ###
  * MIRROR\_FRONT :  if you want MIRROR the front pattern, set 1. Default 0
  * MIRROR\_BACK :  if you want MIRROR the back pattern, set 1. Default 0
  * MIRROR\_DRILL :  if you want MIRROR the drill pattern, set 1. Default 0
  * MIRROR\_EDGE : if you want MIRROR the edge pattern, set 1. Default 0
  * ROT\_ANG : Rotation angle (degree) of the converted data. Default 0

  * CUT\_ALL\_FRONT : if you want scrape all non-copper area, set 1. See bottom of this page. Default 0
  * CUT\_ALL\_BACK :  N/A (for future version). Default 0
  * CUT\_STEP\_R : cutting step ratio. = (TOOL\_D - overwrap)/TOOL\_D
  * CUT\_MAX : Max number of the cutting loop.

### For G-code output ###
  * MCODE\_FLAG : If you want insert M code (ex. spindle on "M03"), set 1. Default 0
  * OUT\_INCH\_FLAG : If the unit of output files are INCH, set 1. Set 0 for MM. Default 0
  * OUT\_DIR : G-code data directory
  * OUT\_FRONT\_FILE : Front pattern g-code file name
  * OUT\_BACK\_FILE : Back pattern g-code file name
  * OUT\_DRILL\_FILE : Drill pattern g-code file name
  * OUT\_EDGE\_FILE : Edge pattern g-code file name

### For future (GUI version) ###
  * GERBER\_COLO: N/A for CUI version
  * DRILL\_COLOR: N/A for CUI version
  * EDGE\_COLOR: N/A for CUI version
  * CONTOUR\_COLOR: N/A for CUI version
  * GERBER\_EXT: N/A for CUI version
  * DRILL\_EXT: N/A for CUI version
  * EDGE\_EXT: N/A for CUI version
  * GCODE\_EXT: N/A for CUI version
  * GDRILL\_EXT: N/A for CUI version
  * GEDGE\_EXT: N/A for CUI version

## About CUT\_ALL ##
### CAD Pattern ###
![https://lh6.googleusercontent.com/-JuC4gSDeZB4/UhHlYZqgBUI/AAAAAAAAAGA/xhRqwSd8Pqk/w375-h492-no/test_pattern.png](https://lh6.googleusercontent.com/-JuC4gSDeZB4/UhHlYZqgBUI/AAAAAAAAAGA/xhRqwSd8Pqk/w375-h492-no/test_pattern.png)

### CNC simulation result by [OpenSCAM](http://openscam.com/) ###
CUT\_MAX = 30
![https://lh3.googleusercontent.com/-hQqykbgYcSM/UhHldvZawsI/AAAAAAAAAGI/vUEiZOMpDpE/w787-h550-no/cut_all30loops.png](https://lh3.googleusercontent.com/-hQqykbgYcSM/UhHldvZawsI/AAAAAAAAAGI/vUEiZOMpDpE/w787-h550-no/cut_all30loops.png)