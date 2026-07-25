# MicoAir743-AIO-35A flight controller and ESC

- **Sourced identity:** original/discontinued MicoAir743-AIO-35A
- **PX4 target:** `micoair_h743-aio_default`

## Flight-controller specifications

| Item | Original AIO value |
|---|---|
| MCU | STM32H743VIH6, 480 MHz, 2 MB flash |
| IMUs | BMI088 and BMI270 |
| Barometer | DPS310 |
| Storage | TF/microSD card slot |
| Interfaces | 7 UART, 8 PWM, I2C, SWD, ADC, LED, beeper, USB-C |
| Magnetometer / analog OSD | None onboard / none |
| BECs | 5 V/2 A and 12 V/2 A |
| Mounting / envelope | 25.5 × 25.5 mm, 3 mm holes; 36 × 36 × 8 mm |
| Mass | 10 g |
| PX4 support | Manufacturer states PX4 1.16.0 and later |

## Published UART map

| PX4 device | MCU UART | Manufacturer board function |
|---|---:|---|
| `ttyS0` / TELEM1 | UART1 | Telemetry |
| `ttyS1` / TELEM2 | UART2 | Telemetry, shared with VTX-HD connector |
| `ttyS2` / GPS1 | UART3 | GPS |
| `ttyS3` / TELEM3 | UART4 | Telemetry |
| `ttyS4` / RC | UART6 | Receiver |
| `ttyS5` / ESC | UART7 | ESC |
| `ttyS6` / TELEM4 | UART8 | Telemetry |
| I2C1 | I2C | External I2C |

The VTX-HD connector marks pin 1 as 12 V in the vendor diagram.

## Integrated ESC specifications

| Item | Original AIO value |
|---|---|
| Input | 3–6S, 10–27 V |
| Continuous rating | 35 A × 4, vendor headline value |
| Firmware/target | AM32; `AM32_MICOAIR_743_AIO_F421_2.17` listed by vendor |
| PWM protocols | PWM, DShot300, DShot600 |
| Bidirectional DShot | Hardware/vendor listing says supported; MicoAir's AM32 guide documents configuration through Betaflight or INAV |
| Voltage/current scale factors | 21.12 / 14.14 |

## Original and V2 product differences

| Item | Original MicoAir743-AIO-35A | MicoAir743V2-AIO-35A |
|---|---|---|
| PX4 target | `micoair_h743-aio_default` | `micoair_h743-v2_default` |
| Barometer | DPS310 | SPL06 |
| ESC firmware family | AM32 | Bluejay, per V2 product page |

## Primary sources

- [Original MicoAir743-AIO-35A product page](https://micoair.com/flightcontroller_micoair743_aio_35a/)
- [MicoAir743V2-AIO-35A comparison page](https://micoair.com/flightcontroller_micoair743v2_aio_35a/)
- [MicoAir firmware-loading guide](https://micoair.com/docs/loading-firmware-micoair743/)
- [MicoAir DFU-mode guide](https://micoair.com/docs/enter_dfu_mode_on_flight_controller/)
- [MicoAir AM32 configuration guide](https://micoair.com/docs/how-to-configure-and-update-am32-esc-on-micoair743-aio/)
- [PX4 v1.17.0 board target source](https://github.com/PX4/PX4-Autopilot/tree/v1.17.0/boards/micoair/h743-aio)

Sources accessed 2026-07-25.
