import bpy
import threading

def show_message():
    bpy.ops.wm.info_msg("INVOKE_DEFAULT", message="Blenderが起動しました")

def delayed_message(dummy):
    threading.Timer(10.0, show_message).start()

class InfoMsgOperator(bpy.types.Operator):
    bl_idname = "wm.info_msg"
    bl_label = "Info Message"
    message: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, self.message)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(InfoMsgOperator)
    bpy.app.handlers.load_post.append(delayed_message)

def unregister():
    bpy.utils.unregister_class(InfoMsgOperator)
    bpy.app.handlers.load_post.remove(delayed_message)

if __name__ == "__main__":
    register()
