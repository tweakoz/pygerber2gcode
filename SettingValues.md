# Setting values in "pyg2g.conf" #

### For CAD datas ###
  * CAD\_UNIT
  * DRILL\_UNIT
  * EDGE\_UNIT
  * IN\_INCH\_FLAG : If unit of input file is INCH, set 1
  * OUT\_INCH\_FLAG : If unit of output file is INCH, set 1
### For Cutting machine ###
  * INI\_X,INI\_Y,INI\_Z : Start position of the cutting tool
  * MOVE\_HEIGHT : Moving height (without cutting)
  * XY\_SPEED : In-plane cutting speed
  * Z\_SPEED : Z axis cutting speed
### For Cutting and Dill ###
  * CUT\_DEPTH : Pattern cutting depth
  * TOOL\_D : Diameter of the cutting tool
  * DRILL\_D : Drill diameter
  * DRILL\_SPEED : Drill down speed
  * DRILL\_DEPTH : Drill depth
  * EDGE\_TOOL\_D : Edge cutting tool diameter
  * EDGE\_DEPTH : Edge cutting depth
  * EDGE\_SPEED : Edge cutting speed
  * EDGE\_Z\_SPEED : Edge down speed
  * Z\_STEP : z step
### For Drawing ###
  * GERBER\_COLOR : Pattern color
  * DRILL\_COLOR : Drill color
  * EDGE\_COLOR : Edge color
  * CONTOUR\_COLOR : Contour color
### For G-code data ###
  * LEFT\_X : Left side of the converted G code will be shifted to LEFT\_X
  * LOWER\_Y : Bottom of the converted G code will be shifted to LOWER\_Y
  * MCODE\_FLAG : If you want insert M code (ex. spindle on), set 1
  * MERGE\_DRILL\_DATA : If you want to merge drill data and pattern data, set 1.
  * GERBER\_EXT : Extension of the patern cutting gerber files
  * DRILL\_EXT : Extension of the drill files
  * EDGE\_EXT : Extension of the edge cutting files
  * GCODE\_EXT : Extension of the cutting G-code files
  * GDRILL\_EXT : Extension of the drill G-code files
  * GEDGE\_EXT : Extention of the edge G-code files