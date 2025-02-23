bl_info = {
    "name": "Hello World Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import time

def show_message():
    def draw(self, context):
        self.layout.label(text="こんにちは")
    
    time.sleep(5)

    print("ここにきてますよ")
    bpy.context.window_manager.popup_menu(draw, title="メッセージ", icon='INFO')

class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Hello World"

    def execute(self, context):
        show_message()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(HelloWorldOperator)
    bpy.app.handlers.load_post.append(show_message)

def unregister():
    bpy.utils.unregister_class(HelloWorldOperator)
    bpy.app.handlers.load_post.remove(show_message)

if __name__ == "__main__":
    register()
