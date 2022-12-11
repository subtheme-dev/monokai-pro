import sublate as sub

print("[+] Lapce")

sub.mkdir("src")

for name, theme in sub.data["colors"].items():
    sub.render(f"src/{name}.toml", "templates/theme.toml", {
        "theme": theme
    })

sub.rm("templates")
sub.rm("build.py")