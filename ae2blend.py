names = ['camera_1', 'plane_1', 'plane_2']
isCamera = [True,False,False]
position_scale = 2160
world_scale = 2
# position_scale is width of solid, world_scale is multiply factor of real world.
# if scale in after effects is 1200% and world scale is 1, it has 1200cm (12m) in blender world.
# if world scale is 2, it has 2400cm (24m) in blender world.
file_path = "C:/Users/marks/OneDrive/Documents/blender project/tracking/data.txt"

position_scale = position_scale / world_scale

f = open(file_path, "r")
str = f.read()
lst = [s.split('\n') for s in str.split("End of Keyframe Data")]

import bpy
from math import pi

def assign_to_object(obj_property_list, obj_name, isCamera = False) :
    obj_transforms_list = []
    for s in obj_property_list :
        if('Transform' in s):
            obj_transforms_list.append([s.replace('\t', '_')])
        elif(len(s) != 0 and len(obj_transforms_list) != 0):
            try:
                obj_transforms_list[-1].append([float(i) for i in s.split()])
            except:
                obj_transforms_list[-1].append(s.split())

    obj_transforms_dict = {}

    for lst in obj_transforms_list :
        obj_transforms_dict[lst[0]] = lst[2:]

    obj = bpy.data.objects[obj_name]
    if("Transform_Position" in obj_transforms_dict.keys()) :
        positions = obj_transforms_dict["Transform_Position"]
        if(len(positions) == 1 and len(positions[0]) == 3) : 
            obj.location = [positions[0][0]/position_scale, positions[0][2]/position_scale, -positions[0][1]/position_scale]
        elif(len(positions) >= 1 and len(positions[0]) == 4):
            for position in positions: 
                obj.location = [position[1]/position_scale, position[3]/position_scale, -position[2]/position_scale]
                obj.keyframe_insert(data_path="location", frame = int(position[0]))
    
    if("Transform_Orientation" in obj_transforms_dict.keys()) :
        obj.rotation_mode = 'ZYX'
        rotations = obj_transforms_dict["Transform_Orientation"]
        if(len(rotations) == 1 and len(rotations[0]) == 3) : 
            if(isCamera) : obj.rotation_euler = [pi/2 + rotations[0][0]/180*pi, -rotations[0][1]/180*pi, -rotations[0][2]/180*pi]
            else : obj.rotation_euler = [-pi/2 + rotations[0][0]/180*pi, rotations[0][1]/180*pi, rotations[0][2]/180*pi]
        elif(len(rotations) >= 1 and len(rotations[0]) == 4):
            for rotation in rotations: 
                if(isCamera) : obj.rotation_euler = [pi/2 + rotation[1]/180*pi, -rotation[2]/180*pi, -rotation[3]/180*pi]
                else : obj.rotation_euler = [-pi/2 + rotation[1]/180*pi, rotation[2]/180*pi, rotation[3]/180*pi]
                obj.keyframe_insert(data_path="rotation_euler", frame = int(rotation[0]))
    
    if("Transform_Scale" in obj_transforms_dict.keys()) :
        scales = obj_transforms_dict["Transform_Scale"]
        if(len(scales) == 1 and len(scales[0]) == 3) : 
            obj.scale = [scales[0][0]/200*world_scale, scales[0][1]/200*world_scale, scales[0][2]/200*world_scale]
        elif(len(scales) >= 1 and len(scales[0]) == 4):
            for scale in scales: 
                obj.scale = [scale[1]/200*world_scale, scale[2]/200*world_scale, scale[3]/200*world_scale]
                obj.keyframe_insert(data_path="scale", frame = int(scale[0]))


#print(obj_transforms_dict)

if __name__ == "__main__" :
    for i in range(len(names)):
        assign_to_object(lst[i], names[i], isCamera[i])