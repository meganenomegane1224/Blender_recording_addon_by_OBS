import bpy

# カスタムオペレーターの定義
class SimpleMoveOperator(bpy.types.Operator):
    bl_idname = "object.simple_move_operator"
    bl_label = "Simple Move Operator"
    
    def execute(self, context):
        obj = context.active_object
        if obj:
            obj.location.x += 1.0
            self.report({'INFO'}, f"Moved {obj.name} by 1.0 unit on X axis.")
        return {'FINISHED'}

# Blenderにクラスを登録
def register():
    bpy.utils.register_class(SimpleMoveOperator)

def unregister():
    bpy.utils.unregister_class(SimpleMoveOperator)

if __name__ == "__main__":
    register()

    # オペレーターを実行
    bpy.ops.object.simple_move_operator()
