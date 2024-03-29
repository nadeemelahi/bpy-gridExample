import bpy
import bmesh
import mathutils
from math import radians
from math import sqrt

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

# ref/credit: 
# http://sinestesia.co/blog/tutorials/python-2d-grid/

# Settings 
name = 'Gridtastic' 
rows = 5 
columns = 10

verts = []
faces = [] 



for yloc in range ( columns ) :
	for xloc in range ( rows ) :
		print( xloc , yloc )
		# 0: 0 0
		# 1: 1 0
		# 2: 2 0
		# 3: 3 0
		# 4: 4 0
		# ----
		# 5: 0 1
		# 6: 1 1
		# 7: 2 1
		# 8: 3 1
		# . . 0:0, 5:1, 10:1, 15:2, 20:3, 25:4
		#    30:5,35:6,40:7,45:8,50:9
		# ----
		# 50: 0 9
		# 51: 1 9
		# . .
		# 54: 4 9
		verts.append ( [ xloc , yloc , 0 ] ) 

# FACES
# using indices
'''
faces = [ 
		(0, 1, 6, 5), 
		(1, 2, 7, 6), 
		(2, 3, 8, 7), 
		(3, 4, 9, 8), 
		(5, 6, 11, 10)
		]
print ( faces )
'''

faces = []

# 4, 8, 12, ... 
# 54, 50,
tmp = 0
for idx in range ( 44 ) :
	# print ( idx , idx + 1 , idx + 6 , idx + 5 ) 
	print (tmp)
	if tmp == 4 :
		tmp = 0
		continue

	faces.append ( [ idx , idx + 1 , idx + 6 , idx + 5 ] )
	tmp += 1

print ( faces )

# Create Mesh Datablock 
mesh = bpy.data.meshes.new ( name ) 
mesh.from_pydata ( verts, [], faces ) 
# mesh from vertices, edges and faces. 
# if you pass a faces list you can skip edges




# Create Object and link to scene 
obj = bpy.data.objects.new(name, mesh) 
bpy.context.scene.collection.objects.link ( obj ) 





# Select the object 
bpy.context.view_layer.objects.active = obj 
obj.select_set ( True )
bpy.ops.object.mode_set(mode='EDIT')
