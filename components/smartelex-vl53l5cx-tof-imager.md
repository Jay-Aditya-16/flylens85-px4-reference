# SmartElex ToF Imager - VL53L5CX forward multi-zone ToF sensor

**Sourced identity:** SmartElex ToF Imager - VL53L5CX, built around the STMicroelectronics VL53L5CX 8x8 multi-zone ToF ranging sensor.

## Mission fit

This component is the forward edge-case sensor candidate described in `09_hw_req_forward_tof.md`: an active infrared multi-zone ToF sensor for detecting transparent, reflective, and low-texture obstacles that can confuse camera-only VSLAM/depth pipelines.

The module is a reasonable integration candidate for close indoor obstacle detection, but it should not be treated as a final 5 m glass-detection answer without bench testing. Published VL53L5CX-class range is 4 m, below the brief's 5 m comparison goal and 4-8 m desired effective range.

## Published specifications

| Item | Published value |
|---|---|
| Sensor IC | STMicroelectronics VL53L5CX |
| Sensor type | Direct Time-of-Flight, multi-zone / flash-style ranging |
| Zone output | 4x4 or 8x8 separate zones |
| Maximum ranging distance | Up to 400 cm / 4000 mm per zone |
| Field of view | SmartElex board text: 63 degree diagonal square FoV; ST product page: 65 degree diagonal FoV |
| Frame-rate note | VL53L5CX device capability is published as up to 60 Hz; verify the selected resolution and driver mode because 8x8/64-zone output may run lower than 60 Hz |
| Interface | I2C |
| I2C addressing | SmartElex/Robu list 0x52; VL53L5CX documentation also describes 7-bit 0x29 with 8-bit write/read values 0x52/0x53 |
| Operating voltage | 3.3 V board operation; SmartElex manual text lists 2.7-3.3 V input when powering the board directly |
| Emitter | 940 nm invisible VCSEL |
| Cover-glass behavior | ST histogram algorithms are published as reducing cover-glass crosstalk, with immunity beyond 60 cm |
| Board mass | Not found in the checked Robu/SmartElex/ST sources; weigh the exact module before committing to the sub-250 g airframe budget |

## Requirement check against forward ToF brief

| Requirement from brief | Fit |
|---|---|
| Multi-zone ToF grid | Meets: 4x4 / 8x8 zones |
| Weight under 2-3 g | Unknown: module mass not published in checked sources |
| Effective range 4-8 m | Partial: published maximum is 4 m, not 5-8 m |
| FOV about 45-65 degrees | Meets: 63-65 degree diagonal FoV |
| Refresh at least 30 Hz, ideally 60 Hz | Conditional: 60 Hz device capability is published, but verify actual resolution/rate mode in the intended driver |
| I2C or SPI | Meets: I2C |
| Power below 200 mW | Unknown at board level from checked sources |

## Integration notes

- This sensor is best documented as a forward edge-case sensor for AI depth completion and obstacle confirmation, not as the primary estimator rangefinder already covered by the MicoAir MTF-01.
- The VL53L5CX loads firmware over I2C at power-up; reserve host-side storage and initialization time in the Raspberry Pi / production SoC integration plan.
- Use the 4x4 high-rate mode first for collision gating if frame rate is more important than angular detail; evaluate 8x8 mode for depth-completion anchors if latency is acceptable.
- Treat 5 m transparent-surface detection as unproven for this module. Bench-test glass, mirrors, glossy floors, and white walls at 1-5 m under indoor lighting before selecting it as the final sensor.

## Primary sources

- [Robu SmartElex ToF Imager - VL53L5CX product page](https://robu.in/product/smartelex-tof-imager-vl53l5cx/)
- [Robu SmartElex brand listing](https://robu.in/brand/smartelex/)
- [STMicroelectronics VL53L5CX product page](https://www.st.com/en/imaging-and-photonics-solutions/vl53l5cx)
- [SmartElex ToF Imager - VL53L5CX manual mirror](https://manuals.plus/m/4bbef5fc7654387c24c3a8923842859f49a98e3399c46040f8cb133383db5885)
- [STMicroelectronics VL53L5CX user manual mirror](https://manuals.plus/m/b129e47f9c61b433dc1a1fc1c2dfb4b29421ed8b983e54fafc1dbda3d7415f8a)

Sources accessed 2026-07-26.
