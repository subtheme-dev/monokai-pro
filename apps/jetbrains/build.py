import sublate as sub

print("[+] Monokai Pro")

sub.mkdir("resources/schemes")
sub.mkdir("src")

for name, theme in sub.data["colors"].items():
    # schemes
    sub.render(f"resources/schemes/{name}.xml", "templates/scheme.xml", {
        "theme": theme, "italics": True
    })
    sub.render(f"resources/schemes/{name}-no-italics.xml", "templates/scheme.xml", {
        "theme": theme, "italics": False
    })

    # themes
    sub.render(f"src/{name}.theme.json", "templates/theme.json", {
        "theme": theme
    })

sub.rm("templates")
sub.rm("build.py")