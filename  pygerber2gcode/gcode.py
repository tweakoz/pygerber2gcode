#
#G code data generation
#
import os
import sys
import re
import math

class Gcode:
	def __init__(self):
		self.mcode_sw = 0
		self.inch = 1
		self.mm = 0
		self.unit = 0
		self.initialize = 0
		self.ini_x = 0.0
		self.ini_y = 0.0
		self.ini_z = 5.0
		self.move_height = 1.0
		self.height = self.move_height
		self.xy_speed = 100
		self.z_speed = 60
		self.move_speed = self.xy_speed*2.0
		self.move_speed_z = self.z_speed*2.0
		self.axis_num = 3
		self.shift_x = 0
		self.shift_y = 0
		self.tmp_x = self.ini_x
		self.tmp_y = self.ini_y
		self.tmp_z = self.ini_z
		self.out_data = ""
		self.cut_length = 0.0
		self.cut_length_z = 0.0
		self.move_length = 0.0
		self.move_length_z = 0.0
		self.cut_time = 0.0
		self.cut_time_z = 0.0
		self.move_time = 0.0
		self.move_time_z = 0.0
	def add_polygon(self,height,polygons,xy_speed, z_speed):
		print "Convert to G-code"
		for poly in polygons:
			if (poly.active == 0):
				continue
			self.add_path(height,poly.points,xy_speed,z_speed)

	def add_drill(self,height,point, z_speed=0):
		ret_data = ""
		height=float(height)
		self.tmp_z=float(self.tmp_z)
		self.move(point[0]+float(self.shift_x),point[1]+float(self.shift_y))
		self.tmp_z = height
		if(z_speed):
			ret_data += "G01Z" + str(height) + "F" + str(z_speed) + "\n"
		else:
			ret_data += "G01Z" + str(height) + "\n"
		if(ret_data):
			self.out_data += ret_data

	def add_path(self,height,points,xy_speed, z_speed):
		ret_data = ""
		out_data = "G01"
		gcode_tmp_flag = 0
		height=float(height)
		self.tmp_z=float(self.tmp_z)
		#move to Start position
		self.move(points[0][0]+float(self.shift_x),points[0][1]+float(self.shift_y))
		#move to cuting heght
		if(height != self.tmp_z):
			self.cut_length_z += abs(self.tmp_z-height)
			self.cut_time_z += abs(self.tmp_z-height)/float(z_speed)
			self.tmp_z = height
			ret_data += "G01Z" + str(height) + "F" + str(z_speed) + "\n"
		i = 0
		while i< len(points):
			px=points[i][0]+self.shift_x
			py=points[i][1]+self.shift_y
			pre_x = self.tmp_x
			pre_y = self.tmp_y
			if (px != self.tmp_x):
				self.tmp_x=px
				out_data +="X" + str(px)
				gcode_tmp_flag = 1
			if(py != self.tmp_y):
				self.tmp_y=py
				out_data +="Y" + str(py)
				gcode_tmp_flag=1
			if(gcode_tmp_flag):
				#Goto initial X-Y position
				out_data +="F" + str(xy_speed)
				ret_data += out_data + "\n"
				out_data ="G01"
			gcode_tmp_flag=0
			self.cut_length += self.calc_dist(pre_x,pre_y,px,py)
			self.cut_time += self.calc_dist(pre_x,pre_y,px,py)/float(xy_speed)
			i += 1
		#print gFRONT_DATA
		if(ret_data):
			self.out_data += ret_data
	def add_circle(self,height,cx,cy,r,dir,xy_speed, z_speed):
		ret_data = ""
		height=float(height)
		self.tmp_z=float(self.tmp_z)
		self.move_height=float(self.move_height)
		if(self.move_height != self.tmp_z):
			self.move_length_z += abs(self.tmp_z-self.move_height)
			self.move_time_z += abs(self.tmp_z-self.move_height)/self.move_speed_z
			self.tmp_z = self.move_height
			ret_data += "G00Z" + str(self.move_height) + "\n"

		ret_data += "G00X" + str(cx-r) + "Y". str(cy) + "\n"
		if(height != self.tmp_z):
			self.cut_length_z += abs(self.tmp_z-height)
			self.cut_time_z += abs(self.tmp_z-height)/float(z_speed)
			self.tmp_z = height
			ret_data += "G01Z" + str(height) + "F" + str(z_speed) + "\n"
		ret_data += "G17\n"	#Set XY plane
		# from initial position to set position
		if(dir):
			#CCW
			ret_data += "G03X" + str(cx+r) + "Y" + str(cy) + "R" + str(r) +  "F" + str(xy_speed) + "\n"
			ret_data += "G03X" + str(cx-r) + "Y"+ str(cy) + "R" + str(r) +  "F" + str(xy_speed) + "\n"
		else:
			# from initial position to set position
			#CW
			ret_data += "G02X" + str(cx+r) + "Y" + str(cy) + "R" + str(r) + "F" + str(xy_speed) + "\n"
			ret_data += "G02X" + str(cx-r) + "Y"+ str(cy) + "R" + str(r) + "F" + str(xy_speed) + "\n"
		self.tmp_x=cx+r
		self.tmp_y=cy
		self.cut_length += 2.0*math.pi*r
		self.cut_time += 2.0*math.pi*r/float(xy_speed)
		if(ret_data):
			self.out_data += ret_data
	def add_box(self,height,x1,y1,x2,y2,xy_speed, z_speed):
		if(x1 == x2):
			print "Same X"
		if(y1 == y2):
			print "Same Y"
		#
		#Change 
		if(x1 > x2):
			tmp_x=x1
			x1=x2
			x2=tmp_x
		if(y1 > y2):
			tmp_y=y1
			y1=y2
			y2=tmp_y
		self.add_path(height,[(x1,y1),(x1,y2),(x2,y2),(x2,y1),(x1,y1)],xy_speed,z_speed)
	def move(self,x,y):
		ret_data = ""
		out_data = "G00"
		gcode_tmp_flag = 0
		pre_x = float(self.tmp_x)
		pre_y = float(self.tmp_y)
		self.tmp_z=float(self.tmp_z)
		self.move_height=float(self.move_height)
		if(x != self.tmp_x):
			self.tmp_x = x
			out_data += "X" + str(x)
			gcode_tmp_flag=1
		if(y != self.tmp_y):
			self.tmp_y = y
			out_data +="Y" + str(y)
			gcode_tmp_flag = 1
		if(self.move_height !=self.tmp_z):
			self.move_length_z += abs(self.tmp_z-self.move_height)
			self.move_time_z += abs(self.tmp_z-self.move_height)/self.move_speed_z
			self.tmp_z = self.move_height
			#Goto moving Z position
			ret_data += "G00Z" + str(self.move_height) + "\n"
		if(gcode_tmp_flag):
			#Goto X-Y position
			ret_data += out_data + "\n"

		self.move_length += self.calc_dist(pre_x,pre_y,x,y)
		self.move_time += self.calc_dist(pre_x,pre_y,x,y)/self.move_speed
		#print "ret=" + ret_data
		if(ret_data):
			self.out_data += ret_data

	def out(self, dir,out_file):
		self.out_header = "(Generated by " + sys.argv[0] +" )\n"
		#self.out_header += "( " + get_date() +" )\n"
		self.out_header += "(Initialize)\n"
		self.out_header += "G90"	#Absolute coordinate
		if self.initialize:
			self.out_header += "G54G92X" + str(self.ini_x) + "Y" + str(self.ini_y) + "Z" + str(self.ini_z) + "\n"
		else:
			self.out_header += "\n"

		if self.unit == self.inch:
			self.out_header += "(Set to Inch unit)\n"
			self.out_header += "G20\n"
		else:
			self.out_header += "(Set to MM unit)\n"
			self.out_header += "G21\n"

		self.out_header += "\n" + "(Start form here)\n"
		if self.mcode_sw:
			self.out_header += "(Spindl and Coolant ON)\n"
			self.out_header += "M03\n"
			self.out_header += "M08\n"

		self.out_footer = "\n(Goto to Initial position)\n"
		#Goto initial Z position
		self.out_footer += "G00Z" + str(self.move_height) + "\n"
		if self.mcode_sw:
			#STOP Coolant
			self.out_footer += "M09\n"
			#STOP spindl
			self.out_footer += "M05\n"	
		#Goto initial X-Y position
		self.out_footer += "G00X" + str(self.ini_x) + "Y" + str(self.ini_y) + "\n"
		#Goto initial Z position
		self.out_footer += "G00Z" + str(self.ini_z) + "\n"
		#Program END
		self.out_footer += "(File end)\n"
		if self.mcode_sw:
			self.out_footer += "M30\n"
		#self.out_footer += "M30\n"
		self.out_footer += "%\n"

		self.out_header += self.out_data + self.out_footer
		self.write_file(dir,out_file,self.out_header)

	def write_file(self, dirname,filename,datas):
		file_name = os.path.join(dirname, filename)
		if(datas):
			f = open(file_name, 'w')
			f.write(datas)
			f.close()
		else:
			print "ERROR : No save data"
	def calc_dist(self,px,py,x,y):
		dx = x-px
		dy = y-py
		return math.sqrt(dx*dx+dy*dy)

