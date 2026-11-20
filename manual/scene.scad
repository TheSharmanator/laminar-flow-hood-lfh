// Render scenes for the visual manual. Imports the reference STLs.
scene = "hero";
$fn = 48;
DEPTH = 230; CLAMP_DEPTH = 31.5; TUBE_L = 227;

C = [ ["Q1","#4F6D8C"],["Q2","#6A8DB0"],["Q3","#4F6D8C"],["Q4","#6A8DB0"],
      ["B1","#8FA7BD"],["B2","#A3B8CB"],["B3","#8FA7BD"],["B4","#A3B8CB"],
      ["C1","#C2612A"],["C2","#D9803F"],["C3","#C2612A"],["C4","#D9803F"],
      ["SOCKET","#3E8E6E"],["RING","#B23A48"],["BELL","#D9A441"],["LID","#E6C46A"],
      ["V1","#9FD3EC99"],["V2","#9FD3EC99"],["MAGS","#B8BCC4"],["FILTER","#EDEDED"],["EPDM","#1E1E1E"],["FAN","#2B2B2E"],["DISC","#3A3A3A"],["BOLTS","#9A9AA0"] ];
function col(n) = C[search([n], C)[0]][1];
module P(n, dir="stl_asm") color(col(n)) import(str(dir, "/", n, ".stl"), convexity=8);
module PP(n) P(n, "stl_print");
module arrow(len=120, d=8) color("#E03C31") { cylinder(d=d, h=len - 3*d); translate([0,0,len - 3*d]) cylinder(d1=2.6*d, d2=0, h=3*d); }
module bench(w=700, l=600) color("#D8D4CC") translate([-w/2, -l/2, -6]) cube([w, l, 6]);
module bed(s=256) color("#BFC5CC") translate([-s/2, -s/2, -1.5]) cube([s, s, 1.5]);

// poses
module flange_down() rotate([90,0,0]) children();                       // box on bench, flange down (assembly Y -> up)
module rear_down()   translate([0,0,DEPTH]) rotate([-90,0,0]) children(); // back on bench, outer face down
module face_down()   translate([0,0,CLAMP_DEPTH]) rotate([90,0,0]) children(); // clamp on bench, front face down

ALL_Q = ["Q1","Q2","Q3","Q4"]; ALL_B = ["B1","B2","B3","B4"]; ALL_C = ["C1","C2","C3","C4"];

if (scene == "hero") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","RING","FILTER","EPDM","FAN","BELL","DISC","LID","BOLTS","MAGS"])) P(n);
  P("V1"); P("V2");
}
else if (scene == "hero_novisor") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","RING","FILTER","EPDM","FAN","BELL","DISC","LID","BOLTS"])) P(n);
}
else if (scene == "s_vglue") {
  bench();
  translate([0,0,164.9]) rotate([180,0,0]) P("V1");
  translate([0,0,100]) translate([0,0,164.9]) rotate([180,0,0]) P("V2");
  translate([60, 100, 420]) rotate([180,0,0]) arrow(90);
}
else if (scene == "s_mags") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","FILTER","EPDM","BOLTS","MAGS"])) P(n);
}
else if (scene == "s_vfit") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","RING","FILTER","EPDM","FAN","BELL","DISC","LID","BOLTS","MAGS"])) P(n);
  translate([0,-140,0]) { P("V1"); P("V2"); }
  translate([0,-130,190]) rotate([-90,0,0]) arrow(90);
}
else if (scene == "exploded") {
  E = 1;
  for (i=[0:3]) { s = [[-1,1],[1,1],[1,-1],[-1,-1]][i]; translate([s[0]*55, 0, s[1]*55]) P(ALL_Q[i]); }
  for (i=[0:3]) { s = [[-1,1],[1,1],[1,-1],[-1,-1]][i]; translate([s[0]*45, 230, s[1]*45]) P(ALL_B[i]); }
  for (i=[0:3]) { s = [[-1,1],[1,1],[1,-1],[-1,-1]][i]; translate([s[0]*45, -300, s[1]*45]) P(ALL_C[i]); }
  translate([0,-190,0]) P("FILTER");
  translate([0,-95,0]) P("EPDM");
  translate([0,-420,0]) P("BOLTS");
  translate([0,-560,0]) { P("V1"); P("V2"); }
  translate([0,0,120]) P("SOCKET");
  translate([0,0,190]) P("RING");
  translate([0,0,260]) P("FAN");
  translate([0,0,350]) P("BELL");
  translate([0,0,420]) P("DISC");
  translate([0,0,480]) P("LID");
}
else if (scene == "s_q1") {          // Q2 on bench, Q1 lowered from above
  bench();
  flange_down() P("Q2");
  translate([0,0,150]) flange_down() P("Q1");
  translate([-80, -70, 540]) rotate([180,0,0]) arrow(110);
}
else if (scene == "s_q3") {
  bench();
  flange_down() { P("Q1"); P("Q2"); }
  translate([0,0,150]) flange_down() P("Q3");
  translate([80, 70, 540]) rotate([180,0,0]) arrow(110);
}
else if (scene == "s_q4") {
  bench();
  flange_down() { P("Q1"); P("Q2"); P("Q3"); }
  translate([0,0,150]) flange_down() P("Q4");
  translate([-80, 70, 540]) rotate([180,0,0]) arrow(110);
}
else if (scene == "s_tube") {
  bench();
  flange_down() for (n = ALL_Q) P(n);
}
else if (scene == "s_back") {
  bench();
  rear_down() { P("B1"); P("B2"); P("B3"); }
  translate([0,0,60]) rear_down() P("B4");
  translate([-90, -70, 150]) rotate([180,0,0]) arrow(70, 6);
}
else if (scene == "s_backjoin") {
  bench();
  rear_down() for (n = ALL_B) P(n);
  translate([0,0,120]) rear_down() for (n = ALL_Q) P(n);
  translate([0, 0, 470]) rotate([180,0,0]) arrow(100);
}
else if (scene == "s_socket") {
  for (n = concat(ALL_Q, ALL_B)) P(n);
  translate([0,0,90]) P("SOCKET");
  translate([0,113.5,330]) rotate([180,0,0]) arrow(80);
}
else if (scene == "s_dip") {
  for (n = concat(ALL_Q, ALL_B, ["SOCKET"])) P(n);
}
else if (scene == "s_clamp") {
  bench();
  face_down() { P("C1"); P("C2"); P("C3"); }
  translate([0,0,140]) face_down() P("C4");
  translate([-95, 80, 330]) rotate([180,0,0]) arrow(100);
}
else if (scene == "s_nuts") {
  for (n = concat(ALL_Q, ALL_B)) P(n);
}
else if (scene == "s_epdm") {
  for (n = concat(ALL_Q, ALL_B, ["SOCKET"])) P(n);
  translate([0,-60,0]) P("EPDM");
}
else if (scene == "s_filter") {
  for (n = concat(ALL_Q, ALL_B, ["SOCKET","EPDM"])) P(n);
  translate([0,-120,0]) P("FILTER");
  translate([0,-260,0]) for (n = ALL_C) P(n);
  translate([0,-380,0]) P("BOLTS");
}
else if (scene == "s_fan") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","FILTER","EPDM","BOLTS"])) P(n);
  translate([0,0,70]) P("RING");
  translate([0,0,160]) P("FAN");
}
else if (scene == "s_bell") {
  for (n = concat(ALL_Q, ALL_B, ALL_C, ["SOCKET","RING","FILTER","EPDM","BOLTS","FAN"])) P(n);
  translate([0,0,90]) P("BELL");
  translate([0,0,170]) P("DISC");
  translate([0,0,240]) P("LID");
}
// print-pose cards: one part on a 256 bed
else if (scene == "print_one") {
  // set -D part="Q1"
}
part = "Q1";
if (scene == "print_one") { bed(); translate([0,0,0]) centre_on_bed() color(col(part=="coupons" ? "RING" : part=="GAUGE2" ? "BELL" : part)) import(str("stl_print_c/", part, ".stl"), convexity=8); }
module centre_on_bed() children();
