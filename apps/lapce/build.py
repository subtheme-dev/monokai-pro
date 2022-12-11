import sublate as sub

print("[+] Lapce")

sub.mkdir("src")

for theme in sub.data["colors"]:
    sub.render(f"src/{theme['id']}.toml", "templates/theme.toml", {
        "theme": theme
    })

sub.rm("templates")
sub.rm("build.py")