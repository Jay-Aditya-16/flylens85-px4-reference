# MicoAir MG-A01 GNSS and compass

- **Supplied name:** Mico Air AG01
- **Sourced identity:** MicoAir MG-A01

## Manufacturer specifications

| Item | Published value |
|---|---|
| GNSS | u-blox M10 `M10050` “Ultra” as named by MicoAir |
| Compass | QMC5883L |
| Signals/constellations | GPS, GLONASS, BeiDou, Galileo, QZSS, SBAS on L1 |
| Concurrent reception | 3 constellations by default |
| Maximum navigation update | 10 Hz |
| Maximum satellites | 32 |
| GNSS output | 3.3 V LVTTL UART, 115200 default, UBX-PVT default |
| Compass output | I2C |
| Supply | 5 V, 30 mA |
| Antenna | 25 × 25 × 4 mm patch |
| Module dimensions/mass | 25 × 25 × 7.8 mm; 12 g |
| Connector | SH1.0-6P, 1 mm pitch |
| Vendor PX4 statement | PX4 1.14 or later |

The linked u-blox M10 SPG 5.10 interface description defines the UBX protocol family. The MicoAir product page is the source for the assembled MG-A01 module defaults.

## Primary sources

- [MicoAir MG-A01 product page](https://micoair.com/gps_mg-a01/)
- [u-blox M10 SPG 5.10 Interface Description, UBX-21035062 R03](https://content.u-blox.com/sites/default/files/u-blox-M10-SPG-5.10_InterfaceDescription_UBX-21035062.pdf)
- [PX4 QMC5883L driver reference](https://docs.px4.io/v1.17/en/modules/modules_driver_magnetometer#qmc5883l)
- [PX4 magnetometer setup](https://docs.px4.io/v1.17/en/gps_compass/magnetometer)
- [PX4 compass calibration](https://docs.px4.io/v1.17/en/config/compass)

Sources accessed 2026-07-25.
