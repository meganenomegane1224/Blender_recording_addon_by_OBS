import bpy
import os
import subprocess

bl_info = {
    "name": "Hello World Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}
@bpy.app.handlers.persistent
def my_handler(dummy):
    bpy.ops.wm.info_msg("INVOKE_DEFAULT", message="hello world")
    obs_path="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    obs_dir_path="C:\\Program Files\\obs-studio\\bin\\64bit"
    os.chdir(obs_dir_path)
    subprocess.Popen([obs_path])

class InfoMsgOperator(bpy.types.Operator):
    bl_idname = "wm.info_msg"
    bl_label = "Info Message"
    message: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, self.message)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(InfoMsgOperator)
    bpy.app.handlers.load_post.append(my_handler)

def unregister():
    bpy.utils.unregister_class(InfoMsgOperator)
    bpy.app.handlers.load_post.remove(my_handler)

if __name__ == "__main__":
    register()
