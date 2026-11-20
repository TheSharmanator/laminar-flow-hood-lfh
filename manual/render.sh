#!/bin/bash
# name scene camera size [extra -D]
n=$1; sc=$2; cam=$3; sz=${4:-1200,900}; ex=$5
xvfb-run -a openscad -o img/$n.png --imgsize=$sz -D "scene=\"$sc\"" $ex --camera=$cam --colorscheme=Tomorrow scene.scad >/dev/null 2>&1
echo "$n done"
