import bpy

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Simple Operator"

    message: bpy.props.StringProperty(name="Message")

    def execute(self, context):
        bpy.context.window_manager.popup_menu(self.draw_func, title="Info", icon='INFO')
        return {'FINISHED'}

    def draw_func(self, self_arg, context):
        layout = self_arg.layout
        layout.label(text=self.message)

def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname)

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()

    # オペレーターを実行する例
    bpy.ops.object.simple_operator('INVOKE_DEFAULT', message="こんにちは、Blender!")
