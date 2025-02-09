
.PHONY: all clean

all: out/stand.scad

out/stand.scad: stand/stand.py
	mkdir -p out
	python $<

clean:
	rm -rf out/
