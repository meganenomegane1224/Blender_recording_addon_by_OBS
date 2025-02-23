import bpy
import os
import subprocess
import psutil
import time
import obsws_python as obs

HOST="localhost"
PORT="4455"
PASSWORD="KQH5Ze21mvypZUkU"
SEENCOLLECTION_NAME="megane_MIKU"
PROFILE_NAME="megane_MIKU"
RECORDING_BOOL=False

addon_keymaps = []

bl_info = {
    "name": "Hello World Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}

obs_path="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
obs_dir_path="C:\\Program Files\\obs-studio\\bin\\64bit"

class AddonProPerties(bpy.types.PropertyGroup):
    OBS_host: bpy.props.StringProperty(name="")
    OBS_port_number: bpy.props.StringProperty(name="")
    OBS_password: bpy.props.StringProperty(name="")
    seencollection_name: bpy.props.StringProperty(name="")
    profile_name: bpy.props.StringProperty(name="")
    record_start_wait_time: bpy.props.IntProperty(name="")
    obs_dir_path: bpy.props.StringProperty(name="")
    recording_bool: bpy.props.BoolProperty(name="Recording")


class recording_button_operator(bpy.types.Operator):
    bl_label ="Record Start"
    bl_idname="wm.recording_button"

    def execute(self, context):
        pro=context.scene.addon_pro
        start_recording()
        return {'FINISHED'}

class stop_recording_button_operator(bpy.types.Operator):
    bl_label ="Record Stop"
    bl_idname="wm.recording_stop_button"

    def execute(self, context):
        stop_OBS(self)
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
        layout.prop(pro, "obs_dir_path")
        layout.prop(pro, "recording_bool")
        layout.separator()
        layout.operator("wm.recording_button")
        layout.operator("wm.recording_stop_button")

class message_class(bpy.types.Operator):
    bl_label ="message Stop"
    bl_idname="wm.message"

    def execute(self, context):
        self.report({'INFO'}, "うおうおうおうおうおう")
def set_client():
    try:
        client = obs.ReqClient(host=HOST, port=PORT, password=PASSWORD)
    except:
        custom_info_message("OBS_websocketへのアクセスに失敗しました")
    else:
        return client

def is_obs_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name']=="obs64.exe":
            print("kidousiteru")
            return True
        return False

def start_OBS(dummy):#ここに引数を必ず1つは入れないと動かない
    if not bpy.context.scene.addon_pro.recording_bool:
        return
    os.chdir(obs_dir_path)
    subprocess.Popen([obs_path])

    time.sleep(1)

    start_recording()

def stop_OBS(self):
    client = obs.ReqClient(host=bpy.context.scene.addon_pro.OBS_host, port=bpy.context.scene.addon_pro.OBS_port_number, password=bpy.context.scene.addon_pro.OBS_password)
    try:
        client.set_current_profile(bpy.context.scene.addon_pro.profile_name)
        client.set_current_scene_collection(bpy.context.scene.addon_pro.seencollection_name)
        client.stop_record()
    except:
        self.report({'ERROR'}, "OBSの録画停止に失敗しました。")
    else:
        client.disconnect()
        self.report({'INFO'}, "OBSの録画を停止しました。")


def start_recording():
    if not bpy.context.scene.addon_pro.recording_bool:
        return
    client = obs.ReqClient(host=bpy.context.scene.addon_pro.OBS_host, port=bpy.context.scene.addon_pro.OBS_port_number, password=bpy.context.scene.addon_pro.OBS_password)
    client.set_current_profile(bpy.context.scene.addon_pro.profile_name)
    client.set_current_scene_collection(bpy.context.scene.addon_pro.seencollection_name)
    client.start_record()
    client.disconnect()



# カスタムメッセージ関数
def custom_info_message(message="",title="Mesage Box",icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


def register():
    bpy.app.handlers.load_post.append(start_OBS)
    bpy.utils.register_class(AddonProPerties)
    bpy.utils.register_class(message_class)
    bpy.utils.register_class(recording_button_operator)
    bpy.utils.register_class(stop_recording_button_operator)
    bpy.utils.register_class(Addon_UI)
    bpy.types.Scene.addon_pro=bpy.props.PointerProperty(type=AddonProPerties)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')

    kmi = km.keymap_items.new(stop_recording_button_operator.bl_idname, 'E','PRESS', ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.app.handlers.load_post.remove(start_OBS)
    bpy.utils.unregister_class(AddonProPerties)
    bpy.utils.unregister_class(message_class)
    bpy.utils.unregister_class(recording_button_operator)
    bpy.utils.unregister_class(stop_recording_button_operator)
    bpy.utils.unregister_class(Addon_UI)
    del bpy.types.Scene.addon_pro

    for km, kmi in addon_keymaps:
        km.keymap_items.remive(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
