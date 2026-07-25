# Power and mass budget

## Verified mass entries

| Component | Quantity | Published mass | Extended mass |
|---|---:|---:|---:|
| FlyLens 85 frame | 1 | 25.5–27 g, variant-dependent | 25.5–27 g |
| MicoAir743-AIO-35A | 1 | 10 g | 10 g |
| QPT 1404.5 motors | 4 | 10 g including wire | 40 g |
| SkyDroid C10 Pro | 1 | 61 g, provisional secondary C10 Pro source | 61 g |
| MG-A01 | 1 | 12 g | 12 g |
| MTF-01 | 1 | 4.5 g | 4.5 g |
| Nexus1 plus T antenna | 1 | 1.2 + 2.29 g | 3.49 g |
| LAVA 3S 450 mAh | 1 or 2 | 37.8 g each | 37.8 or 75.6 g |

- Known dry subtotal without battery: **156.49–157.99 g**.
- Known subtotal with one battery: **194.29–195.79 g**.
- Known subtotal carrying two batteries: **232.09–233.59 g**.

The totals exclude the Pi, propellers, regulators, camera transport hardware, mounts, cooling, storage, harnesses, fasteners, adhesives, and guards. Carrying both packs leaves only 16.41–17.91 g below 250 g; the omitted required parts necessarily exceed that margin. Record the complete aircraft mass and center of gravity on calibrated scales after every layout revision.

## Battery scenarios

| Topology | Nominal / full voltage | Capacity | Nominal energy | Mass | Disposition |
|---|---:|---:|---:|---:|---|
| One pack at a time | 11.4 / 13.05 V | 450 mAh | 5.13 Wh | 37.8 g | Initial bench and propulsion-test baseline |
| Two matched packs in parallel | 11.4 / 13.05 V | 900 mAh | 10.26 Wh | 75.6 g plus harness | Only after a reviewed parallel-power design; packs must be matched and at equal voltage |
| Two packs in series | 22.8 / 26.1 V | 450 mAh | 10.26 Wh | 75.6 g plus harness | **Rejected:** exceeds the motor's documented 3S/4S application |

The AIO board default assumes four 4.2 V/cell cells. For a single 3S LiHV pack, set three cells and 4.35 V/cell, then calibrate voltage and current against instruments. Do not discharge below 3.0 V/cell under load; select a more conservative operational threshold from measured sag and battery temperature.

## Known electrical limits

| Device | Published input/consumption | Integration conclusion |
|---|---|---|
| Original AIO | 3–6S, 10–27 V; 5 V/2 A and 12 V/2 A BECs | One 3S LiHV pack is within input range; BEC ratings require total-load and thermal validation |
| Raspberry Pi 4 | Official recommended supply capacity 5 V/3 A | Needs dedicated regulator and brownout testing |
| Raspberry Pi 5 | Official recommended supply capacity 5 V/5 A | Needs dedicated regulator; materially harder power/thermal load |
| MG-A01 | 5 V, 30 mA | About 0.15 W nominal |
| MTF-01 | 5 V, 500 mW | About 100 mA nominal |
| C10 Pro | 7.2–12 V, 210 mA in provisional C10 Pro material | Blocked until exact variant is verified; 13.05 V battery can exceed 12 V |
| QPT motor | 14.5 A / 240 W headline maximum per motor | Conditions not published; use measurements, not multiplication, for design |

## Required power-budget measurements

- Regulator efficiency and case temperature from minimum loaded pack voltage through full charge.
- Pi boot, CPU/GPU load, USB/peripheral, and camera-stream current transients.
- AIO 5 V rail current with GNSS, receiver, MTF-01, and any LEDs/buzzer.
- Single-motor and four-motor bus current with the exact propeller.
- Battery sag, connector temperature, cell balance, and delivered capacity.
- Conducted/radiated noise effects on GNSS, compass, RC link, optical flow, and video.
