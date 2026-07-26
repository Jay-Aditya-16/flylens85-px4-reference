# Datasheet, manual, and source register

This register is the entry point for upstream technical information. Vendor files are linked rather than copied so their copyright and update history remain with the publisher.

- **Snapshot date:** 2026-07-26
- **Quality labels:** Primary = manufacturer, protocol owner, or upstream project. Secondary = unaffiliated mirror or reseller.

## Airframe and propulsion

| Component | Document | Quality | Notes |
|---|---|---:|---|
| FlyLens 85 | [Frame kit](https://flywoo.net/products/flylens-85-frame-kit) | Primary | Materials, mounting, mass; current motor-hole statement |
| FlyLens 85 | [2S kit](https://www.flywoo.net/products/flylens-85-2s-drone-kit-brushless-whoop) | Primary | Reference configuration and V1.3 frame change log |
| FlyLens 85 | [Download center](https://flywoo.net/page/flylens-85-drone-download-center) | Primary | Firmware/manual hub |
| FlyLens 85 | [Quick-start manual PDF](https://cdn-files.myshopline.com/file/store/1673593876355/FLYLENS85.pdf) | Primary | Assembly and product overview |
| FlyLens 85 | [Frame-parts collection](https://flywoo.net/products/flylens-85-frame-parts-collection) | Primary | Stock mount options |
| QPT 1404.5 | [Product/specification page](https://quanteonworld.com/product/qpt-1404-5-fpv-drone-motor/) | Primary | Ratings and intended prop/battery class |
| QPT 1404.5 | [Dimension drawing](https://quanteonworld.com/wp-content/uploads/2025/12/Screenshot-2026-01-07-222049.png) | Primary | Inspect at original resolution |
| QPT 1404.5 | [Performance image](https://quanteonworld.com/wp-content/uploads/2025/12/Screenshot-2026-01-07-222307.png) | Primary | Headline performance image |
| LAVA battery | [3S 450 mAh product page](https://betafpv.com/products/lava-2s-3s-4s-450mah-75c-battery-2pcs) | Primary | Electrical, dimensional, connector, and care data |

## Flight controller, navigation, and sensing

| Component | Document | Quality | Notes |
|---|---|---:|---|
| Original AIO | [MicoAir743-AIO-35A page](https://micoair.com/flightcontroller_micoair743_aio_35a/) | Primary | Discontinued original revision; full specification and PX4 mapping |
| V2 AIO | [MicoAir743V2-AIO-35A page](https://micoair.com/flightcontroller_micoair743v2_aio_35a/) | Primary | Revision comparison data |
| AIO | [Firmware loading](https://micoair.com/docs/loading-firmware-micoair743/) | Primary | Vendor update procedure |
| AIO | [DFU mode](https://micoair.com/docs/enter_dfu_mode_on_flight_controller/) | Primary | Recovery/boot procedure |
| AIO/ESC | [AM32 setup/update](https://micoair.com/docs/how-to-configure-and-update-am32-esc-on-micoair743-aio/) | Primary | ESC configuration/update procedure |
| PX4 target | [Board directory at v1.17.0](https://github.com/PX4/PX4-Autopilot/tree/v1.17.0/boards/micoair/h743-aio) | Primary | Pin, build, module, and default configuration |
| PX4 target | [`default.px4board`](https://github.com/PX4/PX4-Autopilot/blob/v1.17.0/boards/micoair/h743-aio/default.px4board) | Primary | Built drivers/services |
| PX4 target | [`rc.board_defaults`](https://github.com/PX4/PX4-Autopilot/blob/v1.17.0/boards/micoair/h743-aio/init/rc.board_defaults) | Primary | Battery and magnetometer defaults |
| MG-A01 | [MicoAir product page](https://micoair.com/gps_mg-a01/) | Primary | Assembled module specification and defaults |
| u-blox M10 | [SPG 5.10 Interface Description R03](https://content.u-blox.com/sites/default/files/u-blox-M10-SPG-5.10_InterfaceDescription_UBX-21035062.pdf) | Primary | UBX protocol reference; not a substitute for exact module identity |
| MTF-01 | [Product/manual page](https://micoair.com/optical_range_sensor_mtf-01/) | Primary | Electrical, optical, protocol, and PX4 data |
| MTF-01 | [User-manual repository](https://github.com/micoair/MTF-01_USER_MANUAL) | Primary | Manufacturer's versioned manual source |
| MTF-01 | [MicoAssistant](https://micoair.com/assistant/) | Primary | Browser configuration tool |
| MTF-01 | [MicoLink decoder](https://micoair.com/docs/decoding-micolink-messages-from-mtf-01/) | Primary | Packet description/example |
| SmartElex VL53L5CX | [Robu product page](https://robu.in/product/smartelex-tof-imager-vl53l5cx/) | Secondary | Reseller page supplied for forward edge-case ToF sensor |
| SmartElex VL53L5CX | [Robu SmartElex brand listing](https://robu.in/brand/smartelex/) | Secondary | SKU, operating-voltage, address, frame-rate listing |
| SmartElex VL53L5CX | [SmartElex module manual mirror](https://manuals.plus/m/4bbef5fc7654387c24c3a8923842859f49a98e3399c46040f8cb133383db5885) | Secondary | Board overview, power, I2C, firmware-load notes |
| VL53L5CX | [ST product page](https://www.st.com/en/imaging-and-photonics-solutions/vl53l5cx) | Primary | Sensor IC range, zones, FoV, frame-rate, cover-glass data |
| VL53L5CX | [ST user manual mirror](https://manuals.plus/m/b129e47f9c61b433dc1a1fc1c2dfb4b29421ed8b983e54fafc1dbda3d7415f8a) | Secondary | Ultra lite driver behavior and output data guidance |

## Command, control, camera, and companion

| Component | Document | Quality | Notes |
|---|---|---:|---|
| Nexus1 | [Product page](https://zerodrag.in/products/express-lrs-receiver-2-4ghz-made-in-india) | Primary | Product identity/specification |
| Nexus1 | [User Manual v1.1 PDF](https://cdn.shopify.com/s/files/1/0567/9038/4729/files/Zerodrag_Nexus1_User_Manual_Version_1.1.pdf?v=1712646205) | Primary | Pinout and specifications |
| ExpressLRS | [Receiver wiring](https://www.expresslrs.org/quick-start/receivers/wiring-up/) | Primary | CRSF data wiring |
| ExpressLRS | [Firmware versioning](https://www.expresslrs.org/quick-start/receivers/firmware-version/) | Primary | Firmware version data |
| ExpressLRS | [Firmware options](https://www.expresslrs.org/quick-start/firmware-options/) | Primary | Regulatory domain and binding options |
| RadioMaster Pocket | [Product page](https://radiomasterrc.com/products/pocket-radio-controller-m2) | Primary | Variant and hardware specifications |
| RadioMaster Pocket | [User manual PDF](https://cdn.shopify.com/s/files/1/0701/8066/7584/files/Pocket_A1.8.pdf?v=1770617495) | Primary | Setup, power, and RF guidance |
| Pi 4 | [Product specification](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/?variant=raspberry-pi-4-model-b-8gb) | Primary | Candidate only until board identity is known |
| Pi 4 | [Datasheet PDF](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf) | Primary | Interfaces and mechanical information |
| Pi 5 | [Product page](https://www.raspberrypi.com/products/raspberry-pi-5/) | Primary | Candidate only until board identity is known |
| Pi 5 | [Product brief PDF](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf) | Primary | Interfaces and mechanical information |
| Pi power | [Official power documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply) | Primary | Recommended supply capacity and typical current |
| C10 Pro | [SkyDroid support](https://skydroidglobal.com/pages/skydroid-support) | Primary | C10Pro SDK material and app-control data |
| SkyDroid | [Download center](https://skydroidglobal.com/pages/download-center) | Primary | Current official downloads |
| C10 Pro | [RCSDK releases](https://gitee.com/skydroid/rcsdk-demo/releases) | Primary | Includes C10Pro-specific release material |
| SkyDroid video | [FPV player demo](https://gitee.com/skydroid/fpv-player-demo/blob/dev/README.md) | Primary | RTSP example in a SkyDroid network |
| C10, not Pro | [S1PRO instructions PDF](https://file.skydroid.xin/shuomingshu/S1PRO-Instructions.pdf) | Primary | Similar-product comparison only |
| C10 Pro | [Manual mirror](https://manuals.plus/ae/1005007476644987) | Secondary | C10 Pro values from mirror source |

## PX4 and protocol references

| Topic | Document | Notes |
|---|---|---|
| Release | [PX4 v1.17.0](https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0) | PX4 release page |
| CRSF | [CRSF telemetry](https://docs.px4.io/v1.17/en/telemetry/crsf_telemetry) | CRSF telemetry documentation |
| Companion | [Raspberry Pi companion guide](https://docs.px4.io/v1.17/en/companion_computer/pixhawk_rpi) | Raspberry Pi companion documentation |
| Optical flow | [Optical-flow setup](https://docs.px4.io/v1.17/en/sensor/optical_flow) | Optical-flow documentation |
| Range | [Rangefinders](https://docs.px4.io/v1.17/en/sensor/rangefinders) | Range-sensor documentation |
| Estimator | [EKF2 tuning guide](https://docs.px4.io/v1.17/en/advanced_config/tuning_the_ecl_ekf) | EKF2 documentation |
| Magnetometer | [Magnetometer setup](https://docs.px4.io/v1.17/en/gps_compass/magnetometer) | Magnetometer documentation |
| QMC5883L | [Driver reference](https://docs.px4.io/v1.17/en/modules/modules_driver_magnetometer#qmc5883l) | Driver commands |
