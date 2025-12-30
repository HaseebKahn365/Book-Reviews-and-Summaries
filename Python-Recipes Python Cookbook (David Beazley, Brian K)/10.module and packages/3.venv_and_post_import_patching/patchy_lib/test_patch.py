from patchy_lib.import_patch import post_import_hook


@post_import_hook("math")
def patch_math(mod):
    original_cos = mod.cos

    def logged_cos(x):
        print(f"LOG: math.cos({x})")
        return original_cos(x)

    mod.cos = logged_cos


import math

print(math.cos(0))
print(math.cos(1))