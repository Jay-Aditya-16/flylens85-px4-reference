# MicoAir MTF-01 optical-flow and range sensor

**Identity confidence:** high.

## Manufacturer specifications

| Item | Published value |
|---|---|
| Interface | 3.3 V LVTTL UART, 115200 baud |
| Protocols | MicoLink, MAVLink, MSP; includes `Mavlink_PX4` mode |
| Output rate | 100 Hz |
| Supply / power | 5 V / 500 mW |
| Dimensions / mass | 29.3 × 17 × 14.5 mm / 4.5 g |
| Mounting | 24.3 × 12 mm, 2.5 mm holes |
| ToF wavelength / beam | 850 nm / 3° half angle |
| ToF dead zone | 2 cm |
| ToF range | 8 m at 90% reflectivity and 600 lux; 5 m at 90% and 60 klux |
| ToF accuracy | 4 cm below 2 m at 90% reflectivity; 2% above 2 m |
| Optical-flow field of view | 42° |
| Optical-flow speed | Up to 7 m/s at 1 m height |
| Flow environmental guidance | More than 60 lux and more than 8 cm working distance |

Range and flow performance depend strongly on surface reflectivity/texture, illumination, height, vibration, lens cleanliness, rotation, and motion. The headline limits are not guaranteed over all combinations.

## PX4 v1.17 setup

MicoAir's product page says PX4 1.14+ is supported and adds a PX4 1.17+ instruction to set `MAV_PROTO_VER=1`. Configure the sensor itself for `Mavlink_PX4` at 115200, allocate TELEM3, and follow [PX4 integration](../docs/px4-integration.md). Since `MAV_PROTO_VER` is global, test the companion link after changing it.

Before enabling estimator fusion, confirm:

- Range against traceable distances over representative light/surface conditions.
- Optical-flow sign, rotation, scale, quality, and update rate using `vehicle_optical_flow`.
- No clipping, vibration artifact, prop/landing-gear obstruction, or camera/gimbal interference.
- Valid range/flow during Pi, ESC, lighting, and camera activity.

Use range as the estimator height reference only for a tested low-altitude operating envelope. Optical flow is an aid, not a substitute for a complete failsafe and position-source strategy.

## Primary sources

- [MicoAir MTF-01 product/manual page](https://micoair.com/optical_range_sensor_mtf-01/)
- [MicoAir MTF-01 user-manual repository](https://github.com/micoair/MTF-01_USER_MANUAL)
- [MicoAssistant configuration tool](https://micoair.com/assistant/)
- [MicoLink decoding specification/example](https://micoair.com/docs/decoding-micolink-messages-from-mtf-01/)
- [PX4 optical-flow documentation](https://docs.px4.io/v1.17/en/sensor/optical_flow)
- [PX4 rangefinder documentation](https://docs.px4.io/v1.17/en/sensor/rangefinders)
- [PX4 EKF2 tuning guide](https://docs.px4.io/v1.17/en/advanced_config/tuning_the_ecl_ekf)

Sources accessed 2026-07-25.
