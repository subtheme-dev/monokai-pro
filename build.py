#!/usr/bin/env python3
import sublate as sub

sub.data.update({
    "date": sub.date_iso(),
    "colors": sub.read("colors/*.yaml").values(),
})

sub.rm("output")
sub.cp("theme", "output")
sub.run("output/*/build.py")
