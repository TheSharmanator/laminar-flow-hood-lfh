#!/bin/bash
# usage: export.sh PART POSE
p=$1; pose=$2; out=stl_${pose}/${p}.stl
[ "$pose" = "asm" ] && pz=assembly || pz=print
xvfb-run -a openscad -o $out -D "part=\"$p\"" -D "pose=\"$pz\"" -D '$fn=64' lfh_ref.scad > logs_${p}_${pose}.txt 2>&1
echo "$p $pose $(grep -o 'Total rendering time.*' logs_${p}_${pose}.txt) $(grep -ci warning logs_${p}_${pose}.txt) warnings"
