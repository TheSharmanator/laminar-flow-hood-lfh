# Manual feedback from Joe — APPLIED 31 Oct 2026 19:28 (artifact v1793474887-e29b, PDF 26 pp)
1. Bench kit / manifest says "16 magnets" — must state size: 16 × magnets Ø6 × 3 mm (N42+). Check every mention, not just the hardware table.
2. Restructure: merge section 7 (Hardware) and the section 5 "Kit for the bench" into ONE full manifest, placed at the TOP of the manual (before printing/assembly). Manifest includes filament (PLA, clear PLA, TPU) + all hardware with sizes. "Kit for the bench" (tools/consumables) sits at the bottom of that manifest. Remove the separate kit callout from section 5 and the separate section 7.
3. Manifest gets IMAGES, and must include the HEPA filter and the fan as line items. Joe will send images + names next (use his photos/names, not renders).
   - FAN: image manifest_img/fan.png | name: "150mm Inline Duct Fan 500m3/h or greater" | qty 1
   - HEPA: image manifest_img/hepa.png | name: "Replacement Filter set True HEPA For Levoit LV-PUR131 Air Purifier LV-PUR131S UK" | qty 1 (HEPA used on the box; carbon panel in the set not used on the front)
   - PRE-FILTER: image manifest_img/floss.png | name: "1cm thick aquarium floss" | qty 1 sheet (50x50 cm = 4 discs of 224 mm)
   - MAGNETS: image manifest_img/magnets.png | name: "Magnets, Ø6 x 3 mm disc (N42 or stronger)" | qty 16
   - GASKET: image manifest_img/epdm.png | name: "Neoprene Self Adhesive Foam Sponge Strip Roll Tape Door Seal EPDM Weather Strips" — 10 mm wide x 8 mm thick | qty ~1.4 m (solid sponge confirmed, not hollow D)
   - SUPERGLUE: NO image | entry: "Thin cyanoacrylate (superglue)" with search term shown: "thin Cyanoacrylate" | qty 1 bottle
   - PLASTI DIP: image manifest_img/plastidip.png | name: "Plasti Dip" (Performix multi-purpose rubber coating, 250 ml tin) | qty 1 tin
   - BOLTS: image manifest_img/bolts.png | name: "M4 socket cap bolts" — M4 x 40 mm | qty 12
   - NUTS: image manifest_img/nuts.png | name: "M4 hex nuts" — 7 mm across flats, 3.2 mm thick (Joe labelled the msg "bolts"; it is the nut) | qty 12
   - SILICONE: NO image | entry: "Silicone sealant, neutral-cure, low-odour" with search term shown: "neutral cure silicone" | qty 1 small tube
4. Policy for remaining manifest items: Joe supplies images + names where wanted; where he says no image, give the item name + a search term instead.
5. Plasti Dip is the BRUSH-ON tin (250 ml), not spray. Change every mention:
   - build_site.py:63 step text "Spray 2–3 light coats…" → brush 2–3 thin coats inside, through the front opening
   - build_site.py:415 kit callout (being merged into manifest anyway)
   - build_site.py:450 hardware table "Spray / 1 can" → "Brush-on / 1 tin (250 ml)"
   - spec .md:479 BOM "Plasti Dip (spray) | 1 can" → "Plasti Dip (brush-on) | 1 tin, 250 ml"
6. SPEED CONTROLLER added after first apply: image manifest_img/speed.png | name: "Plug In Variable Fan Speed Controller Dimmer" | qty 1. Step 19 wording now names it.
