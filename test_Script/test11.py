import bpy

class MyOperator(bpy.types.Operator):
    bl_idname = "wm.my_operator"
    bl_label = "My Operator"
    
    message: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, self.message)
        return {'FINISHED'}

class Mypanel(bpy.types.Panel):
    bl_label="My Panel"
    bl_idname="OBJECT_PT_my_panel"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My Panel'

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.myoperator", text="ぼたんだよーーー")

class Mytor(bpy.types.Operator):
    bl_idname="wm.myoperator"
    bl_label="My Operator"

    def execute(self, context):
        bpy.ops.wm.my_operator('INVOKE_DEFAULT', message="これはINFOメッセージです")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MyOperator)
    bpy.utils.register_class(Mypanel)
    bpy.utils.register_class(Mytor)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')

    kmi = km.keymap_items.new(.bl_idname, 'S','PRESS', ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(MyOperator)
    bpy.utils.unregister_class(Mypanel)
    bpy.utils.unregister_class(Mytor)

if __name__ == "__main__":
    register()

    # テスト実行
