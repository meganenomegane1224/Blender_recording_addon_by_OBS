import bpy

class SimpleAddonProperties(bpy.types.PropertyGroup):
    input_1: bpy.props.StringProperty(name="Input 1")
    input_2: bpy.props.StringProperty(name="Input 2")
    input_3: bpy.props.StringProperty(name="Input 3")
    input_4: bpy.props.StringProperty(name="Input 4")
    display_info: bpy.props.BoolProperty(name="Display Info")

class SimpleAddonPanel(bpy.types.Panel):
    bl_label = "Simple Addon"
    bl_idname = "PT_SimpleAddon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Simple Addon'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "input_1")
        layout.prop(mytool, "input_2")
        layout.prop(mytool, "input_3")
        layout.prop(mytool, "input_4")
        layout.prop(mytool, "display_info")
        layout.operator("wm.simple_operator")

class SimpleOperator(bpy.types.Operator):
    bl_label = "Print Inputs"
    bl_idname = "wm.simple_operator"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        if mytool.display_info:
            self.report({'INFO'}, f"Input 1: {mytool.input_1}")
            self.report({'INFO'}, f"Input 2: {mytool.input_2}")
            self.report({'INFO'}, f"Input 3: {mytool.input_3}")
            self.report({'INFO'}, f"Input 4: {mytool.input_4}")

        return {'FINISHED'}

classes = [SimpleAddonProperties, SimpleAddonPanel, SimpleOperator]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=SimpleAddonProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
