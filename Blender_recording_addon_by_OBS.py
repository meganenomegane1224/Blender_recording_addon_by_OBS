import bpy
import os
import subprocess
import psutil
import time
import signal 
import obsws_python as obs

addon_keymaps = []

bl_info = {
    "name": "Hello World Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}

class AddonProPerties(bpy.types.PropertyGroup):
    OBS_host: bpy.props.StringProperty(name="", default="localhost")
    OBS_port_number: bpy.props.StringProperty(name="", default="4455")
    OBS_password: bpy.props.StringProperty(name="")
    seencollection_name: bpy.props.StringProperty(name="")
    profile_name: bpy.props.StringProperty(name="")
    record_start_wait_time: bpy.props.FloatProperty(name="", default=1.0)
    obs_dir_path: bpy.props.StringProperty(name="", default="C:\\Program Files\\obs-studio\\bin\\64bit")
    recording_bool: bpy.props.BoolProperty(name="Recording", default=False)


class recording_button_operator(bpy.types.Operator):
    bl_label ="Record Start"
    bl_idname="wm.recording_button"

    def execute(self, context):
        
        bool = start_recording()
        if bool:
            self.report({'INFO'}, "OBSの録画を開始しました")
        else:
            self.report({'ERROR'}, "OBSの録画を開始できませんでした")
        return {'FINISHED'}

class IntegrationTerminationProcessing(bpy.types.Operator):
    bl_label="Integration Termination Processing"
    bl_idname="wm.integration_termination_processing"

    def execute(self, context):
        stop_recording(self)

        try:
            bpy.ops.wm.save_file_operator()
        except:
            self.report({'ERROR'}, "バックアップの生成に失敗しました")
            return {'FINISHED'}

        bpy.ops.wm.quit_blender()
        return {'FINISHED'}

class stop_recording_button_operator(bpy.types.Operator):
    bl_label ="Record Stop"
    bl_idname="wm.recording_stop_button"

    def execute(self, context):
        stop_recording(self)
        return {'FINISHED'}

class Addon_UI(bpy.types.Panel):
    bl_label="OBS recording"
    bl_idname ="OBS"
    bl_space_type="VIEW_3D"
    bl_region_type="UI"
    bl_category="Recording"

    def draw(self, context):
        layout=self.layout
        pro=context.scene.addon_pro

        layout.label(text="websocket host name")
        layout.prop(pro, "OBS_host")
        layout.label(text="websocket port number")
        layout.prop(pro, "OBS_port_number")
        layout.label(text="websocket password")
        layout.prop(pro, "OBS_password")
        layout.separator()
        layout.label(text="seencollection name")
        layout.prop(pro, "seencollection_name")
        layout.label(text="Profile name")
        layout.prop(pro, "profile_name")
        layout.separator()
        layout.label(text="directory of obs")
        layout.prop(pro, "obs_dir_path")
        layout.separator()
        layout.label(text="start record wait time")
        layout.prop(pro, "record_start_wait_time")
        layout.prop(pro, "recording_bool")
        layout.separator()
        layout.operator("wm.recording_button")
        layout.operator("wm.recording_stop_button")

def is_obs_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name']=="obs64.exe":
            print("kidousiteru")
            return True
        return False

def start_OBS(dummy):#ここに引数を必ず1つは入れないと動かない
    if not bpy.context.scene.addon_pro.recording_bool:
        return
    os.chdir(bpy.context.scene.addon_pro.obs_dir_path)
    obs_path=os.path.join(bpy.context.scene.addon_pro.obs_dir_path, "obs64.exe")
    subprocess.Popen([obs_path])
    time.sleep(bpy.context.scene.addon_pro.record_start_wait_time)

    start_recording()
        


def stop_OBS():
    return
    obs_process=find_obs_process()

    if obs_process:
        try:
            os.kill(obs_process.pid, signal.SIGTERM)
            print(f"process {obs_process.name()} (PID: {obs_process.pid}) has been terminated.")
        except Exception as e:
            print(f"Failed to terminate the process. error: {e}")
    else:
        print("OBS process not found")

def find_obs_process():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'].lower()=='obs64.exe':
            return proc
    return None
    

def stop_recording(self):
    try:
        connect_OBS().stop_record()
    except:
        self.report({'ERROR'}, "OBSの録画停止に失敗しました。")
    else:
        connect_OBS().disconnect()
        self.report({'INFO'}, "OBSの録画を停止しました。")


def connect_OBS():
    try:
        return obs.ReqClient(host=bpy.context.scene.addon_pro.OBS_host, port=bpy.context.scene.addon_pro.OBS_port_number, password=bpy.context.scene.addon_pro.OBS_password)
    except Exception as e:
        print(f"OBSへの接続に失敗しました。ERROR: {e}")
        return None

def start_recording():
    try:
        client = connect_OBS()
        client.set_current_profile(bpy.context.scene.addon_pro.profile_name)
        client.set_current_scene_collection(bpy.context.scene.addon_pro.seencollection_name)
        client.start_record()
        client.disconnect()
    except Exception as e:
        print(f"OBSの録画開始処理に失敗しました ERROR: {e}")
        return False
    
    return True



def register():
    bpy.app.handlers.load_post.append(start_OBS)
    bpy.utils.register_class(AddonProPerties)
    bpy.utils.register_class(recording_button_operator)
    bpy.utils.register_class(IntegrationTerminationProcessing)
    bpy.utils.register_class(stop_recording_button_operator)
    bpy.utils.register_class(Addon_UI)
    bpy.types.Scene.addon_pro=bpy.props.PointerProperty(type=AddonProPerties)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')

    kmi = km.keymap_items.new(IntegrationTerminationProcessing.bl_idname, 'E','PRESS', ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.app.handlers.load_post.remove(start_OBS)
    bpy.utils.unregister_class(AddonProPerties)
    bpy.utils.unregister_class(recording_button_operator)
    bpy.utils.unregister_class(IntegrationTerminationProcessing)
    bpy.utils.unregister_class(stop_recording_button_operator)
    bpy.utils.unregister_class(Addon_UI)
    del bpy.types.Scene.addon_pro

    wm=bpy.context.window_manager
    km=wm.keyconfigs.addon.keymaps['Window']
    for kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
