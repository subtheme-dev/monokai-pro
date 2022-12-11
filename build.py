import sublate as sub

sub.load("colors")
sub.rm("output")
sub.cp("apps", "output")
sub.run("output/jetbrains/build.py")
sub.run("output/lapce/build.py")

print("Finished")