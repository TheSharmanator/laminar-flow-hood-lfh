// =====================================================================
// LFH v1 — REFERENCE IMPLEMENTATION of "LFH-v1_OpenSCAD_build_spec.md"
// FINAL: measured parts, 31 Oct 2026. Verified at these dimensions: bed fit,
// zero interference, slide-together path, wrong-swap blocking, bayonet path,
// visor fit + pull-off. The SPEC is authoritative where they differ.
// Export one part:  set part="Q1" and pose="print" (OpenSCAD MCP), or CLI:
//   openscad -o P01_Q1.stl -D 'part="Q1"' -D 'pose="print"' lfh_v1_reference.scad
// part names: coupons GAUGE2 Q1..Q4 B1..B4 C1..C4 SOCKET RING BELL LID V1 V2  (assembly: part="assembly")
// File-name map: coupons=P00, GAUGE2=P00b, Q1..Q4=P01..P04, B1..B4=P05..P08,
//                C1..C4=P09..P12, SOCKET=P13, RING=P14 (TPU), BELL=P15, LID=P16, V1=P17, V2=P18 (clear PLA)
// Print-pose exports are not centred on the bed; let the slicer centre them.
// Assembly frame: X = right (viewed from the front), Y = depth (0 = gasket
// face of the front flange, +Y towards the back), Z = up. Origin = centre
// of the filter opening on the gasket face. All units mm.
// =====================================================================

/* ---------- selectors (set from the command line) ---------- */
part    = "assembly";   // assembly | coupons | GAUGE2 | Q1..Q4 | B1..B4 | C1..C4 | SOCKET | RING | BELL | LID | V1 | V2
pose    = "assembly";   // assembly | print
step    = 99;           // assembly-step renders (99 = finished)
explode = 0;            // 0..1 exploded view factor
ghosts  = true;         // show filter / fan / EPDM / bolts
labels  = true;         // debossed part numbers
$fn     = 72;

/* ---------- MEASURED 2026-10-31 (Joe's parts) ---------- */
FILTER_W = 339;     FILTER_H = 291;     FILTER_FOAM = 2;     // cardboard frame face; edge foam each side (over foam: 343 x 295)
FILTER_T = 22;      FILTER_T_MAX = 25;  FILTER_BORDER = 10.8; // frame varies 22-25: design at the thin end
FAN_OD = 148.1;     FAN_END_OD = 148.1; FAN_LEN = 150;
GLAND_FROM_INTAKE = 52;  GLAND_D = 11.5;                    // 98 from the outlet end

/* ---------- fixed design parameters ---------- */
DEPTH = 230;  WALL = 3;  BACK_T = 3;  FLANGE_T = 6;  FLANGE_EXT = 15;  FILTER_TOL = 0.5;   // FLANGE_EXT / FILTER_TOL measured from the OUTER (foam) edge
CLAMP_PLATE = 4;
GASKET_W = 10;  GASKET_T = 8;  GASKET_C = 5.5;  CH_D = 0;  CH_W = GASKET_W + 0.5;  CH_R = 8;   // EPDM 10 wide x 8 thick on a FLAT flange face (no groove: it printed as a 10.5 mm roof); 5.5 at FILTER_T, 2.5 at FILTER_T_MAX
GUIDE_W = 0.6;  GUIDE_D = 0.2;   // hairline on the flange face marking the strip's outer edge (= cardboard edge); one first layer deep
RIB_D = 7;  RIB_HW = 6;  RIB_STOP = 10;
BOSS_D = 12;  BOSS_H = 6;  BOLT_HOLE = 4.4;  NUT_AF = 7.3;  NUT_DEPTH = 3.7;  CB_D = 7.6;  CB_DEPTH = 3;
CLR = 0.15;                                     // joint clearance per face
RIDGE_T = 2.5;  RIDGE_H = 6;  RIDGE_CLR = 0.2;  // back-plate U-channel
SOCK_CLEAR = 0.5;  SOCK_WALL = 3;  SOCK_H = 40;  SOCK_FL_D = 210;  SOCK_FL_T = 4;
RING_T = 2;
FOOT_W = 30;  FOOT_L = 40;  FOOT_INSET = 20;
BELL_MOUTH_ID = 220;  BELL_WALL = 2.5;  BAND_H = 12;  CONE_H = 40;  SLEEVE_L = 30;  STOP_ID = FAN_OD - 4;
GRID_PITCH = 15;  GRID_BAR = 2;  GRID_T = 2;
LID_CLR = 0.3;  LID_WALL = 2.4;  LID_PLATE = 2.4;  PRESS_H = 7;  DISC_CLAMP = 3;  SKIRT_DOWN = 8;   // PRESS_H 7: 10 mm floss stays lofty in the field
/* visor (detachable hood, clear PLA, magnets) */
VISOR_REACH = 150;  VISOR_T = 2.4;  VISOR_LIP = 20;  WING_END_Z = 0;  STRIP_T = 4.2;  FRONT_RIB_H = 10;
MAG_D = 6;  MAG_T = 3;  MAG_POCKET_D = 6.3;  MAG_POCKET_DEPTH = 3.1;  HEAD_H = 4.0;  HEAD_CLR_D = 8.6;  HEAD_CLR_DEPTH = 1.4;
LUG_W = 8;  LUG_R = 1.5;  LUG_H = 2.5;  SLOT_W = 9;  SLOT_DEPTH = 1.8;  ENTRY_H = 6;  RUN_ANG = 20;

/* ---------- derived ---------- */
FILTER_WO = FILTER_W + 2*FILTER_FOAM;  FILTER_HO = FILTER_H + 2*FILTER_FOAM;   // over the edge foam
W_i = FILTER_W - 2*FILTER_BORDER;     H_i = FILTER_H - 2*FILTER_BORDER;
W_o = W_i + 2*WALL;                   H_o = H_i + 2*WALL;
FL_W = FILTER_WO + 2*FLANGE_EXT;      FL_H = FILTER_HO + 2*FLANGE_EXT;
TUBE_L = DEPTH - BACK_T;
FILTER_BACK_Y = -(GASKET_C - CH_D);
CLAMP_DEPTH = CLAMP_PLATE + FILTER_T + (GASKET_C - CH_D);
CLAMP_WALL = FLANGE_EXT - FILTER_TOL;
BX = FILTER_WO/2 + FILTER_TOL + CLAMP_WALL/2;
BZ = FILTER_HO/2 + FILTER_TOL + CLAMP_WALL/2;
GC_X = FILTER_W/2 - GASKET_W/2;  GC_Z = FILTER_H/2 - GASKET_W/2;   // strip's outer edge flush with the cardboard edge
Y_F = TUBE_L/2;
FAN_HOLE_D = FAN_END_OD - 4;
SOCK_ID = FAN_OD + SOCK_CLEAR;        LEDGE_W = 4;  LEDGE_ID = FAN_END_OD - 2*LEDGE_W;
FOOT_H = FL_H/2 - H_o/2;  FOOT_END = TUBE_L - RIDGE_H - 1;
W_b = W_o + 2*(RIDGE_CLR + RIDGE_T);  H_b = H_o + 2*(RIDGE_CLR + RIDGE_T);
BAND_W = WALL + RIB_D;                 // seam band thickness (wall + rib)
SLEEVE_ID = FAN_OD + 0.4;
BELL_RIM_OD = BELL_MOUTH_ID + 2*3;
LID_SKIRT_ID = BELL_RIM_OD + 2*LID_CLR;
LID_OD = LID_SKIRT_ID + 2*LID_WALL;
DISC_D = BELL_RIM_OD - 2;

WIN_W = FILTER_W - 2*(FILTER_BORDER - 2);  WIN_H = FILTER_H - 2*(FILTER_BORDER - 2);
Y_CF = -CLAMP_DEPTH;                       // clamp front face
MAGNETS = [[-BX*2/3, BZ],[-BX/6, BZ],[BX/6, BZ],[BX*2/3, BZ],[-BX, BZ*2/3],[-BX, BZ/6],[BX, BZ*2/3],[BX, BZ/6]];
VKNOBS_Y = [Y_CF - 30, Y_CF - 80, Y_CF - 130];
BOLTS = [[-BX, BZ],[-BX/3, BZ],[BX/3, BZ],[BX, BZ],[BX, BZ/3],[BX,-BZ/3],
         [BX,-BZ],[BX/3,-BZ],[-BX/3,-BZ],[-BX,-BZ],[-BX,-BZ/3],[-BX, BZ/3]];

/* dovetail sizes [neck, head, length] */
DT_WALL  = [[3.0,5.0,4],[4.0,6.0,4]];  // S, L  (box wall seams)
DT_FLNG  = [[4.0,6.0,4],[5.0,7.5,4]];  // S, L  (box flange + clamp wall seams)
KNOB     = [[6,9,3],[8,12,3]];         // S, L  jigsaw knob [neck, head dia, neck len] (back)

echo(str("W_i=",W_i," H_i=",H_i," W_o=",W_o," H_o=",H_o," FL=",FL_W,"x",FL_H,
         " TUBE_L=",TUBE_L," CLAMP_DEPTH=",CLAMP_DEPTH," BX=",BX," BZ=",BZ,
         " W_b=",W_b," H_b=",H_b," FOOT_H=",FOOT_H," LEDGE_ID=",LEDGE_ID,
         " FILTER_BACK_Y=",FILTER_BACK_Y, " DISC_D=",DISC_D, " LID_OD=",LID_OD,
         " SOCK_ID=",SOCK_ID, " FAN_HOLE_D=",FAN_HOLE_D, " SLEEVE_ID=",SLEEVE_ID, " STOP_ID=",STOP_ID,
         " GC=",GC_X,"/",GC_Z, " WIN=",WIN_W,"x",WIN_H, " CLAMP_WALL=",CLAMP_WALL, " Y_F=",Y_F));
assert(GASKET_W <= FILTER_BORDER - 0.5, "Gasket wider than filter frame border");
assert(GASKET_C - (FILTER_T_MAX - FILTER_T) >= 2.5, "Gasket over-squeezed at the thickest point");
assert(GC_X - GASKET_W/2 >= W_i/2, "Gasket strip overhangs the box opening");

/* =============================== helpers =============================== */
// 2D (u,v) -> assembly (x=u, z=v), extruded along +Y from y0 to y1
module yprism(y0, y1) { translate([0,y0,0]) rotate([-90,0,0]) linear_extrude(y1-y0, convexity=10) mirror([0,1,0]) children(); }   // convexity: hollow profiles need it for a correct F5 preview
module rrect(w, h, r) { offset(r) square([w-2*r, h-2*r], center=true); }
module dt2d(d) { polygon([[0,-d[0]/2],[d[2],-d[1]/2],[d[2],d[1]/2],[0,d[0]/2]]); }      // protrudes +u
module knob2d(k) { translate([-0.01,-k[0]/2]) square([k[2]+0.01, k[0]]); translate([k[2]+k[1]/2-0.5,0]) circle(d=k[1]); }
// place a 2D joint shape at seam point p=[u,v], pointing along angle a (deg)
module at2d(p, a) { translate(p) rotate(a) children(); }
module hexagon(af) { circle(d = af/cos(30), $fn=6); }

/* quadrant clip: 1=TL 2=TR 3=BR 4=BL (viewed from the front) */
function qsign(i) = [[-1,1],[1,1],[1,-1],[-1,-1]][i-1];
module quad(i, big=2000) { s = qsign(i); translate([s[0]*big/2, 0, s[1]*big/2]) cube([big, big*2, big], center=true); }

/* seams: [owner of tongue, receiver, 2D seam point, pointing angle, size 0=S 1=L, band] */
// box wall seams (band = wall + rib), centred mid-band
ZC = H_o/2 - BAND_W/2;   XC = W_o/2 - BAND_W/2;
WALL_SEAMS = [ [1,2,[0, ZC],   0, 0],    // top    Q1 -> Q2  S
               [2,3,[XC,0],  -90, 0],    // right  Q2 -> Q3  S
               [3,4,[0,-ZC], 180, 1],    // bottom Q3 -> Q4  L
               [4,1,[-XC,0],  90, 1] ];  // left   Q4 -> Q1  L
FZ = FL_H/2 - 7;  FX = FL_W/2 - 7;
FLANGE_SEAMS = [ [1,2,[0, FZ],   0, 0], [2,3,[FX,0], -90, 0],
                 [3,4,[0,-FZ], 180, 1], [4,1,[-FX,0],  90, 1] ];
CZ = BZ;  CX = BX;   // clamp wall centreline
CLAMP_SEAMS  = [ [1,2,[0, CZ],   0, 0], [2,3,[CX,0], -90, 0],
                 [3,4,[0,-CZ], 180, 1], [4,1,[-CX,0],  90, 1] ];
// back plate knobs: 2 per seam segment
BACK_SEAMS = [ [1,2,[0, 47],0,0],[1,2,[0, 94],0,0],
               [2,3,[ 55,0],-90,0],[2,3,[110,0],-90,0],
               [3,4,[0,-47],180,1],[3,4,[0,-94],180,1],
               [4,1,[-55,0],90,1],[4,1,[-110,0],90,1] ];

/* ============================ BOX (tube) ============================ */
module tube_raw() {
  // walls
  yprism(0, TUBE_L) difference() { square([W_o, H_o], center=true); square([W_i, H_i], center=true); }
  // front flange
  yprism(0, FLANGE_T) difference() { square([FL_W, FL_H], center=true); square([W_i, H_i], center=true); }
  // seam ribs (inside)
  yprism(0, TUBE_L - RIB_STOP) {
    translate([-RIB_HW,  H_i/2 - RIB_D]) square([2*RIB_HW, RIB_D]);
    translate([-RIB_HW, -H_i/2])         square([2*RIB_HW, RIB_D]);
    translate([ W_i/2 - RIB_D, -RIB_HW]) square([RIB_D, 2*RIB_HW]);
    translate([-W_i/2,         -RIB_HW]) square([RIB_D, 2*RIB_HW]);
  }
  // bolt bosses on flange rear
  for (b = BOLTS) translate([b[0], FLANGE_T, b[1]]) rotate([-90,0,0]) cylinder(d=BOSS_D, h=BOSS_H);
  // rear feet (bottom)
  for (sx = [-1,1]) translate([sx*(W_o/2 - FOOT_INSET - FOOT_W/2) - FOOT_W/2, 0, 0])
    rotate([90,0,90]) linear_extrude(FOOT_W, convexity=10) polygon([
      [FOOT_END - FOOT_L - FOOT_H, -H_o/2 + 0.01], [FOOT_END, -H_o/2 + 0.01],
      [FOOT_END, -FL_H/2], [FOOT_END - FOOT_L, -FL_H/2]]);
}
module tube_cuts() {
  // gasket guide: hairline on the flange face along the strip's OUTER edge (flat face otherwise)
  translate([0,-0.01,0]) yprism(0, GUIDE_D + 0.01) difference() {
    rrect(2*(GC_X + GASKET_W/2) + GUIDE_W, 2*(GC_Z + GASKET_W/2) + GUIDE_W, CH_R + GASKET_W/2 + GUIDE_W/2);
    rrect(2*(GC_X + GASKET_W/2) - GUIDE_W, 2*(GC_Z + GASKET_W/2) - GUIDE_W, CH_R + GASKET_W/2 - GUIDE_W/2); }
  // bolt holes + nut pockets
  for (b = BOLTS) {
    translate([b[0], -1, b[1]]) rotate([-90,0,0]) cylinder(d=BOLT_HOLE, h=FLANGE_T + BOSS_H + 2, $fn=24);
    translate([b[0], FLANGE_T + BOSS_H - NUT_DEPTH, b[1]]) rotate([-90,0,0])
      linear_extrude(NUT_DEPTH + 1, convexity=10) rotate(90) hexagon(NUT_AF);
  }
  // fan hole through top wall + rib
  translate([0, Y_F, H_o/2 - BAND_W - 1]) cylinder(d=FAN_HOLE_D, h=BAND_W + 2);
  // socket placement guide (engraved circle on the top face)
  translate([0, Y_F, H_o/2 - 0.6]) difference() { cylinder(d=SOCK_FL_D + 2, h=1); cylinder(d=SOCK_FL_D, h=1); }
}
module box_quarter(i) {
  difference() {
    union() {
      intersection() { tube_raw(); quad(i); }
      for (s = WALL_SEAMS)   if (s[0]==i) yprism(0, TUBE_L - RIB_STOP) at2d(s[2], s[3]) dt2d(DT_WALL[s[4]]);
      for (s = FLANGE_SEAMS) if (s[0]==i) yprism(0, FLANGE_T)          at2d(s[2], s[3]) dt2d(DT_FLNG[s[4]]);
    }
    tube_cuts();
    for (s = WALL_SEAMS)   if (s[1]==i) yprism(-1, TUBE_L + 1) at2d(s[2], s[3]) offset(delta=CLR) dt2d(DT_WALL[s[4]]);
    for (s = FLANGE_SEAMS) if (s[1]==i) yprism(-1, FLANGE_T + 0.01)          at2d(s[2], s[3]) offset(delta=CLR) dt2d(DT_FLNG[s[4]]);
    if (labels) box_label(i);
  }
}
module box_label(i) {
  s = qsign(i);
  // label on inner face of the side wall, mid-depth, 0.6 deep
  translate([s[0]*(W_i/2 - 0.01) , TUBE_L*0.55, s[1]*H_i/4])
    rotate([0, 0, s[0] > 0 ? -90 : 90]) rotate([90,0,0])
      linear_extrude(0.6*2, center=true, convexity=10) text(str("Q", i, "  FRONT"), size=9, halign="center", valign="center", font="DejaVu Sans:style=Bold");
}

/* ============================ BACK ============================ */
module back_raw() {
  yprism(TUBE_L, DEPTH) square([W_b, H_b], center=true);
  yprism(TUBE_L - RIDGE_H, TUBE_L + 0.01) difference() {
    square([W_b, H_b], center=true);
    square([W_o + 2*RIDGE_CLR, H_o + 2*RIDGE_CLR], center=true); }
  yprism(TUBE_L - RIDGE_H, TUBE_L + 0.01) difference() {
    square([W_i - 2*RIDGE_CLR, H_i - 2*RIDGE_CLR], center=true);
    square([W_i - 2*RIDGE_CLR - 2*RIDGE_T, H_i - 2*RIDGE_CLR - 2*RIDGE_T], center=true); }
}
module back_quarter(i) {
  difference() {
    union() {
      intersection() { back_raw(); quad(i); }
      for (s = BACK_SEAMS) if (s[0]==i) yprism(TUBE_L, DEPTH) at2d(s[2], s[3]) knob2d(KNOB[s[4]]);
    }
    for (s = BACK_SEAMS) if (s[1]==i) yprism(TUBE_L - 1, DEPTH + 1) at2d(s[2], s[3]) offset(delta=0.2) knob2d(KNOB[s[4]]);
    if (labels) { q = qsign(i);
      translate([q[0]*W_b/4, TUBE_L - 0.01, q[1]*H_b/4]) rotate([90,0,0])
        linear_extrude(1.2, center=true, convexity=10) text(str("B", i), size=14, halign="center", valign="center", font="DejaVu Sans:style=Bold"); }
  }
}

/* ============================ CLAMP FRAME ============================ */
module clamp_raw() {
  yprism(-CLAMP_DEPTH, -CLAMP_DEPTH + CLAMP_PLATE) difference() {
    square([FL_W, FL_H], center=true);
    square([FILTER_W - 2*(FILTER_BORDER - 2), FILTER_H - 2*(FILTER_BORDER - 2)], center=true); }
  yprism(-CLAMP_DEPTH, 0) difference() {
    square([FL_W, FL_H], center=true);
    square([FILTER_WO + 2*FILTER_TOL, FILTER_HO + 2*FILTER_TOL], center=true); }
}
module clamp_quarter(i) {
  difference() {
    union() {
      intersection() { clamp_raw(); quad(i); }
      for (s = CLAMP_SEAMS) if (s[0]==i) yprism(-CLAMP_DEPTH, 0) at2d(s[2], s[3]) dt2d(DT_FLNG[s[4]]);
    }
    for (s = CLAMP_SEAMS) if (s[1]==i) yprism(-CLAMP_DEPTH - 1, 1) at2d(s[2], s[3]) offset(delta=CLR) dt2d(DT_FLNG[s[4]]);
    for (b = BOLTS) {
      translate([b[0], -CLAMP_DEPTH - 1, b[1]]) rotate([-90,0,0]) cylinder(d=BOLT_HOLE, h=CLAMP_DEPTH + 2, $fn=24);
      translate([b[0], -CLAMP_DEPTH - 1, b[1]]) rotate([-90,0,0]) cylinder(d=CB_D, h=CB_DEPTH + 1, $fn=32);
    }
    for (m = MAGNETS) translate([m[0], -CLAMP_DEPTH - 1, m[1]]) rotate([-90,0,0]) cylinder(d=MAG_POCKET_D, h=MAG_POCKET_DEPTH + 1, $fn=32);
    if (labels) { q = qsign(i);
      // on the outer side face of the clamp wall
      translate([q[0]*FL_W/2, -CLAMP_DEPTH/2 - 2, q[1]*FL_H/4]) rotate([0,0, q[0]>0 ? 90 : -90]) rotate([90,0,0])
        linear_extrude(1.2, center=true, convexity=10) text(str("C", i), size=9, halign="center", valign="center", font="DejaVu Sans:style=Bold"); }
  }
}

/* ============================ FAN SOCKET + RING ============================ */
GLAND_Z_SOCKET = FAN_LEN - GLAND_FROM_INTAKE;   // gland centre above socket ledge
module socket() {   // local frame: base flange bottom at z=0, axis = z
  difference() {
    union() {
      cylinder(d=SOCK_FL_D, h=SOCK_FL_T);
      cylinder(d=SOCK_ID + 2*SOCK_WALL, h=SOCK_H);
    }
    translate([0,0,-1]) cylinder(d=LEDGE_ID, h=SOCK_H + 2);
    translate([0,0,SOCK_FL_T]) cylinder(d=SOCK_ID, h=SOCK_H);
    // gland notch (towards +Y = back) only if the gland sits inside the socket
    if (SOCK_FL_T + RING_T + GLAND_Z_SOCKET - GLAND_D/2 < SOCK_H)
      translate([-(GLAND_D+4)/2, 0, SOCK_FL_T + RING_T + GLAND_Z_SOCKET - GLAND_D/2 - 2]) cube([GLAND_D+4, SOCK_FL_D, SOCK_H]);
  }
}
module ring() { difference() { cylinder(d=SOCK_ID - 0.4, h=RING_T); translate([0,0,-1]) cylinder(d=LEDGE_ID, h=RING_T+2); } }

/* ============================ INTAKE BELL + LID ============================ */
// bell local frame (PRINT pose): mouth on bed at z=0, sleeve on top.
module bell() {
  r_m = BELL_MOUTH_ID/2;  r_s = STOP_ID/2;
  difference() {
    union() {
      cylinder(d=BELL_RIM_OD, h=BAND_H);                                    // rim band
      translate([0,0,BAND_H]) cylinder(r1=r_m + BELL_WALL*1.4, r2=r_s + BELL_WALL*1.4, h=CONE_H);  // cone
      translate([0,0,BAND_H + CONE_H - 0.01]) cylinder(d=SLEEVE_ID + 2*BELL_WALL, h=SLEEVE_L);      // sleeve
    }
    translate([0,0,-0.01]) cylinder(d=BELL_MOUTH_ID, h=BAND_H + 0.02);
    translate([0,0,BAND_H - 0.01]) cylinder(r1=r_m, r2=r_s, h=CONE_H + 0.02);
    translate([0,0,BAND_H + CONE_H + 0.0]) difference() {
      cylinder(d=SLEEVE_ID, h=SLEEVE_L + 1);
      for (a=[0,120,240]) rotate(a) translate([SLEEVE_ID/2 - 0.3, -0.75, -1]) cube([1, 1.5, SLEEVE_L + 3]);   // grip ribs
    }
    // bayonet: entry slots + horizontal runs on the outer rim band
    for (a=[0,120,240]) rotate(a) {
      rotate(-SLOT_W/(PI*BELL_RIM_OD)*180) rotate_extrude(convexity=10, angle=SLOT_W/(PI*BELL_RIM_OD)*360) translate([BELL_RIM_OD/2 - SLOT_DEPTH, -1]) square([SLOT_DEPTH + 1, ENTRY_H + 1]);
      rotate_extrude(convexity=10, angle=RUN_ANG) translate([BELL_RIM_OD/2 - SLOT_DEPTH, ENTRY_H - 3]) square([SLOT_DEPTH + 1, 3]);
    }
    // gland notch at the sleeve end (towards +Y)
    gz = BAND_H + CONE_H + GLAND_FROM_INTAKE;    // gland height in print pose (stop lip at BAND_H + CONE_H)
    if (GLAND_FROM_INTAKE - GLAND_D/2 < SLEEVE_L)
      translate([-(GLAND_D+4)/2, 0, gz - GLAND_D/2 - 2]) cube([GLAND_D+4, SLEEVE_ID, SLEEVE_L + 10]);
  }
  // support grid in the mouth (prints first, on the bed)
  intersection() {
    cylinder(d=BELL_MOUTH_ID + 0.5, h=GRID_T);
    union() {
      for (k = [-8:8]) translate([k*GRID_PITCH - GRID_BAR/2, -BELL_MOUTH_ID/2, 0]) cube([GRID_BAR, BELL_MOUTH_ID, GRID_T]);
      for (k = [-8:8]) translate([-BELL_MOUTH_ID/2, k*GRID_PITCH - GRID_BAR/2, 0]) cube([BELL_MOUTH_ID, GRID_BAR, GRID_T]);
    }
  }
}
// lid local frame (PRINT pose): top face on bed at z=0
module lid() {
  skirt_h = PRESS_H + DISC_CLAMP + SKIRT_DOWN;    // below plate underside
  difference() {
    union() {
      cylinder(d=LID_OD, h=LID_PLATE + skirt_h);
    }
    translate([0,0,LID_PLATE]) cylinder(d=LID_SKIRT_ID, h=skirt_h + 1);
    // grille holes
    intersection() {
      translate([0,0,-1]) cylinder(d=BELL_MOUTH_ID - 6, h=LID_PLATE + 2);
      for (i=[-8:8], j=[-8:8]) translate([i*GRID_PITCH, j*GRID_PITCH, -1]) linear_extrude(LID_PLATE + 2, convexity=10) square(GRID_PITCH - 2.4, center=true);
    }
  }
  // pressing ring over the bell rim
  translate([0,0,LID_PLATE]) difference() { cylinder(d=BELL_RIM_OD, h=PRESS_H); translate([0,0,-1]) cylinder(d=BELL_MOUTH_ID, h=PRESS_H+2); }
  // bayonet lugs (inward), 45-degree chamfer on the plate side
  lug_z = LID_PLATE + PRESS_H + DISC_CLAMP + (ENTRY_H - 3) + 0.25;
  for (a=[0,120,240]) rotate(a + RUN_ANG - 2.5) translate([LID_SKIRT_ID/2, 0, lug_z])   // locked = lug against the end stop of the run
    hull() { translate([-LUG_R, -LUG_W/2, LUG_R]) cube([LUG_R + 0.1, LUG_W, LUG_H - LUG_R]); translate([-0.01,-LUG_W/2, 0]) cube([0.11, LUG_W, LUG_H]); }
}

/* ============================ coupons ============================ */
module coupons() {
  // fan gauge ring G1 (socket fit) with the joint/fastener coupons inside it
  difference() { cylinder(d=SOCK_ID + 2*SOCK_WALL, h=10); translate([0,0,-1]) cylinder(d=SOCK_ID, h=12); }
  // wall dovetail: S slot block, S tongue, L tongue (L must NOT enter the S slot)
  translate([-48,-10,0]) difference() { cube([20,24,20]); translate([0,12,-1]) linear_extrude(22, convexity=10) offset(delta=CLR) dt2d(DT_WALL[0]); }
  translate([-24,-10,0]) { cube([20,24,20]); translate([20,12,0]) linear_extrude(20, convexity=10) dt2d(DT_WALL[0]); }
  translate([  4,-10,0]) { cube([20,24,20]); translate([20,12,0]) linear_extrude(20, convexity=10) dt2d(DT_WALL[1]); }
  // jigsaw knob pair (back plate, S)
  translate([-45, 20, 0]) { cube([20,25,3]); translate([20,12.5,0]) linear_extrude(3, convexity=10) knob2d(KNOB[0]); }
  translate([ -8, 20, 0]) difference() { cube([20,25,3]); translate([0,12.5,-1]) linear_extrude(5, convexity=10) offset(delta=0.2) knob2d(KNOB[0]); }
  // fastener block: bolt hole, counterbore (bottom), hex nut pocket (top)
  translate([34, 32, 0]) difference() { translate([-14,-14,0]) cube([28,28,FLANGE_T + BOSS_H]);
      translate([0,0,-1]) cylinder(d=BOLT_HOLE, h=20, $fn=24);
      translate([0,0,FLANGE_T + BOSS_H - NUT_DEPTH]) linear_extrude(5, convexity=10) rotate(90) hexagon(NUT_AF);
      translate([0,0,-1]) cylinder(d=CB_D, h=CB_DEPTH+1, $fn=32); }
}
module gauge2() {   // sleeve gauge G2 (bell sleeve fit incl. grip ribs)
  difference() { cylinder(d=SLEEVE_ID + 2*BELL_WALL, h=10); translate([0,0,-1]) difference() { cylinder(d=SLEEVE_ID, h=12);
      for (a=[0,120,240]) rotate(a) translate([SLEEVE_ID/2 - 0.3, -0.75, -1]) cube([1, 1.5, 14]); } }
}

/* ============================ VISOR (V1 left, V2 right) ============================ */
module visor_raw() {
  top = FL_H/2;
  // mounting strip (inverted U) against the clamp front face
  yprism(Y_CF - STRIP_T, Y_CF) difference() {
    translate([-FL_W/2, WING_END_Z]) square([FL_W, top - WING_END_Z]);
    translate([-WIN_W/2, WING_END_Z - 1]) square([WIN_W, WIN_H/2 - WING_END_Z + 1]);
  }
  // canopy, incl. the rear lip that rests on the clamp top
  translate([-FL_W/2, Y_CF - VISOR_REACH, top]) cube([FL_W, VISOR_REACH + VISOR_LIP, VISOR_T]);
  // tapered side wings
  for (sx = [-1, 1]) translate([sx > 0 ? FL_W/2 - VISOR_T : -FL_W/2, 0, 0])
    rotate([90,0,90]) linear_extrude(VISOR_T, convexity=10) polygon([[Y_CF, top + VISOR_T], [Y_CF - VISOR_REACH, top + VISOR_T], [Y_CF, WING_END_Z]]);
  // front stiffening rib under the canopy edge
  translate([-FL_W/2, Y_CF - VISOR_REACH, top - FRONT_RIB_H]) cube([FL_W, VISOR_T, FRONT_RIB_H + 0.01]);
}
module visor_cuts() {
  for (m = MAGNETS) if (m[1] >= WING_END_Z)
    translate([m[0], Y_CF + 1, m[1]]) rotate([90,0,0]) cylinder(d=MAG_POCKET_D, h=MAG_POCKET_DEPTH + 1, $fn=32);
  for (b = BOLTS) if (b[1] > WING_END_Z)
    translate([b[0], Y_CF + 1, b[1]]) rotate([90,0,0]) cylinder(d=HEAD_CLR_D, h=HEAD_CLR_DEPTH + 1, $fn=32);
}
module vprism_canopy() { translate([0,0,FL_H/2]) linear_extrude(VISOR_T, convexity=10) children(); }   // 2D (x,y) in the canopy plane
module visor_half(i) {   // 1 = left (x<0), owns the canopy knobs; 2 = right
  difference() {
    union() {
      intersection() { visor_raw(); translate([i==1 ? -1000 : 0, -1000, -1000]) cube([1000, 2000, 2000]); }
      if (i==1) for (y = VKNOBS_Y) vprism_canopy() translate([0, y]) knob2d(KNOB[0]);
    }
    visor_cuts();
    if (i==2) for (y = VKNOBS_Y) translate([0, 0, FL_H/2 - 0.5]) linear_extrude(VISOR_T + 1, convexity=10) translate([0, y]) offset(delta=0.2) knob2d(KNOB[0]);
  }
}
module mag_ghosts() { color([0.75,0.75,0.8]) for (m = MAGNETS) { translate([m[0], Y_CF - MAG_POCKET_DEPTH, m[1]]) rotate([-90,0,0]) cylinder(d=MAG_D, h=MAG_T, $fn=24);
  translate([m[0], Y_CF + MAG_POCKET_DEPTH - MAG_T, m[1]]) rotate([-90,0,0]) cylinder(d=MAG_D, h=MAG_T, $fn=24); } }

/* ============================ ghosts ============================ */
module filter_ghost() {
  color([0.95,0.95,0.95]) translate([0, FILTER_BACK_Y - FILTER_T, 0]) yprism(0, FILTER_T) difference() {
    square([FILTER_WO, FILTER_HO], center=true); square([FILTER_W - 2*FILTER_BORDER, FILTER_H - 2*FILTER_BORDER], center=true); }
  color([0.88,0.90,0.92]) translate([0, FILTER_BACK_Y - FILTER_T + 3, 0]) yprism(0, FILTER_T - 6)
    square([FILTER_W - 2*FILTER_BORDER, FILTER_H - 2*FILTER_BORDER], center=true);
}
module epdm_ghost() { color([0.12,0.12,0.12]) translate([0, FILTER_BACK_Y, 0]) yprism(0, CH_D - FILTER_BACK_Y) difference() {
    rrect(2*GC_X + GASKET_W, 2*GC_Z + GASKET_W, CH_R + GASKET_W/2); rrect(2*GC_X - GASKET_W, 2*GC_Z - GASKET_W, CH_R - GASKET_W/2); } }
module fan_ghost() { color([0.2,0.2,0.22]) difference() { cylinder(d=FAN_OD, h=FAN_LEN); translate([0,0,-1]) cylinder(d=FAN_OD-2, h=FAN_LEN+2); }
  color([0.75,0.75,0.78]) translate([0,0,FAN_LEN*0.6]) for (a=[0:360/7:359]) rotate(a) rotate([0,25,0]) translate([0,-12,0]) cube([FAN_OD/2-3, 24, 1.5]);
  color([0.3,0.3,0.3]) translate([0,0,FAN_LEN*0.4]) cylinder(d=45, h=FAN_LEN*0.35);
  color([0.1,0.1,0.1]) translate([0, FAN_OD/2, FAN_LEN - GLAND_FROM_INTAKE]) rotate([-90,0,0]) cylinder(d=GLAND_D, h=8); }
module bolt_ghost(b, y0) { color([0.6,0.6,0.62]) translate([b[0], y0, b[1]]) rotate([-90,0,0]) { cylinder(d=7, h=4, $fn=6); cylinder(d=4, h=40, $fn=12); } }
module disc_ghost() { color([0.15,0.15,0.15]) cylinder(d=DISC_D, h=1.5); color([0.92,0.92,0.85]) translate([0,0,1.5]) cylinder(d=DISC_D, h=1.5); }

/* ============================ placement in assembly ============================ */
FAN_BOTTOM_Z = H_o/2 + SOCK_FL_T + RING_T;
BELL_MOUTH_Z = FAN_BOTTOM_Z + FAN_LEN + CONE_H + BAND_H;     // stop-lip rests on fan top
COLS = ["#4F6D8C","#6A8DB0","#4F6D8C","#6A8DB0"];
CCOLS = ["#C2612A","#D9803F","#C2612A","#D9803F"];
module place_socket() { translate([0, Y_F, H_o/2]) rotate(0) children(); }
module bell_in_use() { translate([0, Y_F, BELL_MOUTH_Z]) rotate([180,0,0]) children(); }
module lid_in_use()  { translate([0, Y_F, BELL_MOUTH_Z + LID_PLATE + PRESS_H + DISC_CLAMP]) rotate([180,0,0]) children(); }

// exploded offsets
function ex(v) = v*explode;

module assembly() {
  for (i=[1:4]) { s = qsign(i); translate([ex(s[0]*60), 0, ex(s[1]*60)]) color(COLS[i-1]) box_quarter(i); }
  for (i=[1:4]) { s = qsign(i); translate([ex(s[0]*40), ex(260), ex(s[1]*40)]) color(i%2 ? "#8FA7BD" : "#A3B8CB") back_quarter(i); }
  for (i=[1:4]) { s = qsign(i); translate([ex(s[0]*40), ex(-260), ex(s[1]*40)]) color(CCOLS[i-1]) clamp_quarter(i); }
  translate([0,0,ex(150)]) place_socket() color("#3E8E6E") socket();
  translate([0,0,ex(240)]) place_socket() translate([0,0,SOCK_FL_T]) color("#B23A48") ring();
  if (ghosts) {
    translate([0, ex(-140), 0]) filter_ghost();
    translate([0, ex(-70), 0]) epdm_ghost();
    translate([0,0,ex(330)]) translate([0, Y_F, FAN_BOTTOM_Z]) rotate(180) fan_ghost();
    for (b = BOLTS) translate([0, ex(-330), 0]) bolt_ghost(b, -CLAMP_DEPTH + CB_DEPTH - HEAD_H);
    translate([0,0,ex(560)]) translate([0, Y_F, BELL_MOUTH_Z]) disc_ghost();
  }
  translate([0,0,ex(470)]) bell_in_use() color("#D9A441") bell();
  translate([0,0,ex(640)]) lid_in_use() color("#E6C46A") lid();
  translate([0, ex(-560), 0]) color([0.62,0.83,0.93,0.6]) { visor_half(1); visor_half(2); }
}

/* ============================ print poses ============================ */
// box quarters: flange on bed (assembly +Y -> print +Z)
module print_pose(p) {
  if (p=="Q1"||p=="Q2"||p=="Q3"||p=="Q4") rotate([90,0,0]) box_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="B1"||p=="B2"||p=="B3"||p=="B4") translate([0,0,DEPTH]) rotate([-90,0,0]) back_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="C1"||p=="C2"||p=="C3"||p=="C4") translate([0,0,CLAMP_DEPTH]) rotate([90,0,0]) clamp_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="SOCKET") socket();
  else if (p=="RING") ring();
  else if (p=="BELL") bell();
  else if (p=="LID") lid();
  else if (p=="coupons") coupons();
  else if (p=="GAUGE2") gauge2();
  else if (p=="V1"||p=="V2") translate([0,0,FL_H/2 + VISOR_T]) rotate([180,0,0]) visor_half(p=="V1" ? 1 : 2);
}

module asm_pose(p) {
  if (p=="Q1"||p=="Q2"||p=="Q3"||p=="Q4") box_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="B1"||p=="B2"||p=="B3"||p=="B4") back_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="C1"||p=="C2"||p=="C3"||p=="C4") clamp_quarter(search(p[1], "1234")[0] + 1);
  else if (p=="SOCKET") place_socket() socket();
  else if (p=="RING") place_socket() translate([0,0,SOCK_FL_T]) ring();
  else if (p=="BELL") bell_in_use() bell();
  else if (p=="LID") lid_in_use() lid();
  else if (p=="FILTER") filter_ghost();
  else if (p=="EPDM") epdm_ghost();
  else if (p=="FAN") translate([0, Y_F, FAN_BOTTOM_Z]) rotate(180) fan_ghost();
  else if (p=="DISC") translate([0, Y_F, BELL_MOUTH_Z]) disc_ghost();
  else if (p=="BOLTS") for (b = BOLTS) bolt_ghost(b, -CLAMP_DEPTH + CB_DEPTH - HEAD_H);
  else if (p=="V1"||p=="V2") visor_half(p=="V1" ? 1 : 2);
  else if (p=="MAGS") mag_ghosts();
}
if (part == "assembly") assembly();
else if (pose == "print") print_pose(part);
else asm_pose(part);
