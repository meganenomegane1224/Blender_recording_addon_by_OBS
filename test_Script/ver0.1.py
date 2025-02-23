import bpy
import subprocess
import os
import obsws_python as obs
import time

HOST="localhost"
PORT="4455"
PASSWORD="ja3QZZHqfZxWs7Fr"

client = obs.ReqClient(host=HOST, port=PORT, password=PASSWORD)

def start_obs(self):
    obs_path="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    obs_dir_path="C:\\Program Files\\obs-studio\\bin\\64bit"

    try:
        os.chdir(obs_dir_path)
        subprocess.Popen([obs_path])
    except FileNotFoundError:
        self.report({'ERROR'}, "指定されたパスでは動作しません")
    else:
        self.report({'INFO'}, "OBSを起動しました")
    
    time.sleep(10)

    start_recording()
    time.sleep(10)
    stop_recording()


def start_recording():
    client.start_record()


def stop_recording():
    client.stop_record()

class Mypanel(bpy.types.Panel):
    bl_label="My Panel"
    bl_idname="OBJECT_PT_my_panel"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My Panel'

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.myoperator", text="ぼたんだよーーー")
    
class MyOperator(bpy.types.Operator):
    bl_idname="wm.myoperator"
    bl_label="My Operator"

    def execute(self, context):
        start_obs(self)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Mypanel)
    bpy.utils.register_class(MyOperator)

def unregister():
    bpy.utils.unregister_class(Mypanel)
    bpy.utils.unregister_class(MyOperator)

if __name__=="__main__":
    register()
 
 