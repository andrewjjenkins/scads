
.PHONY: all clean

all: out/stand.scad out/stand.stl

out/stand.scad: stand/stand.py
	mkdir -p out
	python $<

out/stand.stl: out/stand.scad
	openscad -o $@ --export-format binstl $<

clean:
	rm -rf out/
