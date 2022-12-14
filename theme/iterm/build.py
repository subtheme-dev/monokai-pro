import sublate as sub

print("[+] iTerm")

for theme in sub.data["colors"]:
    # convert colors to rgb decimal
    _theme = {"colors": {}}
    for k,v in theme["colors"].items():
        r, g, b = tuple(int(v[1:][i:i+2], 16)/255 for i in (0, 2, 4))
        _theme["colors"][k] = {
            "r":  r,
            "g":  g,
            "b":  b,
        }

    sub.render(f"{theme['name']}.itermcolors".replace(" ", "_"), "template.itermcolors", {
        "theme": _theme
    })

sub.rm("template.itermcolors")
sub.rm("build.py")
