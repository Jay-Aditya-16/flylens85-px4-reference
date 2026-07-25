# MicoAir743-AIO-35A flight controller and ESC

- **Provisional identity:** original/discontinued MicoAir743-AIO-35A, not V2. Confirm silkscreen before flashing or wiring.
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

UART mapping is captured in [interfaces and wiring](../docs/interfaces-and-wiring.md). UART2/TELEM2 shares the VTX-HD connector, whose pin 1 is marked 12 V by the vendor.

## Integrated ESC specifications

| Item | Original AIO value |
|---|---|
| Input | 3–6S, 10–27 V |
| Continuous rating | 35 A × 4, vendor headline value |
| Firmware/target | AM32; `AM32_MICOAIR_743_AIO_F421_2.17` listed by vendor |
| PWM protocols | PWM, DShot300, DShot600 |
| Bidirectional DShot | Hardware/vendor listing says supported, but vendor notes PX4/INAV do not currently support it in this workflow |
| Voltage/current scale factors | 21.12 / 14.14 |

PX4 does not provide the vendor's AM32 passthrough workflow. MicoAir directs users to Betaflight or INAV for configuration. Back up settings and identify the ESC revision before any update.

## V1 versus V2 warning

The V2 product uses a different PX4 target, `micoair_h743-v2`, and lists different hardware such as an SPL06 barometer and Bluejay ESC firmware. Flashing or documenting one revision as the other can produce incorrect peripheral mappings or firmware. Photos of both PCB sides and the boot/USB identity are required.

## Primary sources

- [Original MicoAir743-AIO-35A product page](https://micoair.com/flightcontroller_micoair743_aio_35a/)
- [MicoAir743V2-AIO-35A comparison page](https://micoair.com/flightcontroller_micoair743v2_aio_35a/)
- [MicoAir firmware-loading guide](https://micoair.com/docs/loading-firmware-micoair743/)
- [MicoAir DFU-mode guide](https://micoair.com/docs/enter_dfu_mode_on_flight_controller/)
- [MicoAir AM32 configuration guide](https://micoair.com/docs/how-to-configure-and-update-am32-esc-on-micoair743-aio/)
- [PX4 v1.17.0 board target source](https://github.com/PX4/PX4-Autopilot/tree/v1.17.0/boards/micoair/h743-aio)

Sources accessed 2026-07-25.
