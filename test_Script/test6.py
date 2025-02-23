import bpy

def function():
    print("こんにちは")


if __name__=="__main__":
    bpy.app.handlers.load_post.append(function)