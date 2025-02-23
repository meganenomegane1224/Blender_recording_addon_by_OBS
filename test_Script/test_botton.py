import bpy

def function(self, context):
    self.report({'INFO'}, "ボタンが押されました")

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
        function(self,context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Mypanel)
    bpy.utils.register_class(MyOperator)

def unregister():
    bpy.utils.unregister_class(Mypanel)
    bpy.utils.unescape_identifier(MyOperator)

if __name__ == "__main__":
    register()