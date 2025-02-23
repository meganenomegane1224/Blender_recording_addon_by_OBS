import bpy
import time

bl_info = {
    "name": "Hello World Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}

def delayed_hello():
    bpy.ops.report({'INFO'}, message="hello world")
    return None  # タイマーを停止

def on_load_handler(dummy):
    bpy.app.timers.register(delayed_hello, first_interval=10.0)
    print("konnnitiha")
    time.sleep(12)
    print("konnnitiha121212")
    

def register():
    bpy.app.handlers.load_post.append(on_load_handler)

def unregister():
    bpy.app.handlers.load_post.remove(on_load_handler)

if __name__ == "__main__":
    register()
