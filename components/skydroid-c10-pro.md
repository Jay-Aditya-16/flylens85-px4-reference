# SkyDroid C10 Pro camera/gimbal

- **Identity confidence:** low until the label, firmware, connectors, and included manual are captured.
- **Integration state:** blocked; do not apply battery voltage based on the similar C10 product.

## What is established

SkyDroid's current support page names C10Pro as compatible with its RCSDK. It also says third-party remote controllers cannot directly control SkyDroid gimbals and directs users to the SkyDroid app's on-screen controls. Therefore the RadioMaster Pocket/ELRS path cannot be assumed to command this gimbal.

An official SkyDroid FPV player demo shows network playback and an example RTSP address, `rtsp://192.168.144.108:554/stream=0`. That example depends on a compatible SkyDroid network path. The BOM does not include a SkyDroid air receiver, and no reviewed primary source proves that this specific C10 Pro exposes RTSP or control directly to the Pi.

## Provisional C10 Pro values

A secondary C10 Pro manual mirror reports the following. These are identification leads, not verified design inputs:

| Item | Provisional C10 Pro value |
|---|---|
| Input | 7.2–12 V DC |
| Current | 210 mA |
| Operating temperature | −10 to 60 °C |
| Mass | 61 g |
| Dimensions | 51 × 43.3 × 61.7 mm |
| Gimbal range | Pitch −90 to +10°; yaw/pointing −90 to +90°; roll 45° |
| Sensor/video | 2 MP effective; 1080p transmission; 2K recording; H.265 RTSP; H.264 recording |
| Storage | Stated up to 32 GB |

## Why the values cannot be borrowed from C10

SkyDroid's official S1PRO instruction PDF contains a table for **C10**, not C10 Pro. It lists the same nominal mass and envelope but 7.2–72 V input, 4 MP, and different storage guidance. Those conflicts are material: a fully charged 3S LiHV pack reaches 13.05 V, above the provisional C10 Pro 12 V maximum but far below the C10 value. Use a current-limited, separately regulated source only after an exact C10 Pro pinout and rating are obtained.

## Required proof before integration

- Exact model/serial label, firmware, official manual, connector pinout, polarity, and input range.
- Whether an air unit is required and which network interface/IP settings apply.
- Supported video codec, resolution, latency, recording media/filesystem, and simultaneous stream/record behavior.
- Documented SDK/API functions for pitch/yaw, mode, zoom, recording, telemetry, and error reporting.
- A proven adapter between the desired pilot/companion commands and SkyDroid's SDK; there is no verified native MAVLink Camera/Gimbal Protocol support.
- Mount strength, field of view, gimbal clearance, vibration performance, and EMI effects.

## Sources

Primary:

- [SkyDroid support page](https://skydroidglobal.com/pages/skydroid-support)
- [SkyDroid download center](https://skydroidglobal.com/pages/download-center)
- [SkyDroid RCSDK releases](https://gitee.com/skydroid/rcsdk-demo/releases)
- [SkyDroid FPV player demo](https://gitee.com/skydroid/fpv-player-demo/blob/dev/README.md)
- [Official S1PRO instructions containing C10 data](https://file.skydroid.xin/shuomingshu/S1PRO-Instructions.pdf)

Secondary, provisional only:

- [C10 Pro manual mirror](https://manuals.plus/ae/1005007476644987)

Sources accessed 2026-07-25.
