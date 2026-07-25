# PX4 integration baseline

## Pinned baseline

- PX4 release: [`v1.17.0`](https://github.com/PX4/PX4-Autopilot/releases/tag/v1.17.0)
- Board target: [`boards/micoair/h743-aio`](https://github.com/PX4/PX4-Autopilot/tree/v1.17.0/boards/micoair/h743-aio)
- Firmware target: `micoair_h743-aio_default`
- Original board only: do not flash the `micoair_h743-v2` target without confirming the V2 hardware.

Build from the pinned tag:

```sh
git clone --recursive https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
git checkout v1.17.0
git submodule update --init --recursive
make micoair_h743-aio_default
```

The board source defaults include `BAT1_A_PER_V=14.14`, `BAT1_V_DIV=21.12`, four cells, 4.2 V charged voltage, and no magnetometer. The scale factors are starting values, not a substitute for instrument calibration.

## First parameter changes

Export the factory/current parameters before editing. In QGroundControl, set by parameter name rather than copying raw numeric enum values:

| Parameter | Initial value/action | Reason |
|---|---|---|
| `BAT1_N_CELLS` | 3 | One 3S pack |
| `BAT1_V_CHARGED` | 4.35 V | LiHV maximum per-cell voltage |
| `BAT1_V_DIV` | Start at 21.12, calibrate | Vendor board factor |
| `BAT1_A_PER_V` | Start at 14.14, calibrate | Vendor board factor |
| `SYS_HAS_MAG` | 1 only after MG-A01/QMC5883L is confirmed | Board default has no onboard magnetometer |

Do not change the board's battery defaults for a two-pack topology until that topology is electrically reviewed.

## CRSF receiver

PX4 v1.17 CRSF telemetry uses the dedicated CRSF RC driver. The MicoAir target also includes the generic `rc_input` driver; the PX4 CRSF guide requires removing that conflict in a custom build:

```sh
make micoair_h743-aio_default boardconfig
```

In board configuration, disable the generic `drivers/rc_input` selection and ensure `drivers/rc/crsf_rc` is enabled, then rebuild. Connect the Nexus1 to UART6/RC as full-duplex 3.3 V UART data with 5 V power. After flashing:

- Set `RC_CRSF_PRT_CFG` to the `RC` port.
- Enable `RC_CRSF_TEL_EN`.
- Reboot and verify with `crsf_rc status` and `listener input_rc`.
- Configure loss-of-link behavior and test it with motors disabled.

Ignore the Zerodrag manual's ArduPilot `SERIAL1_PROTOCOL=RCIN` screenshot; it is not a PX4 setting. If a custom CRSF build is not maintained, a control-only receiver output such as SBUS may be possible but forfeits the intended CRSF telemetry path.

## MG-A01 GNSS and compass

Connect GNSS UART to GPS1/UART3 and compass SDA/SCL to external I2C. Keep the module away from battery/motor wiring and orient its arrow consistently with the frame. Once the exact module is verified:

1. Confirm GNSS input with `listener sensor_gps`.
2. Set `SYS_HAS_MAG=1`, reboot, and inspect `qmc5883l status` and `listener sensor_mag`.
3. Set the external sensor orientation and perform compass calibration in the final installed layout.
4. Compare compass field magnitude and motor-induced offsets during a restrained current sweep.

## MTF-01 optical flow and range

Use MicoAssistant to select the sensor's `Mavlink_PX4` protocol and 115200 baud. On TELEM3/UART4:

- Set an unused MAVLink instance, for example `MAV_2_CONFIG`, to `TELEM3`.
- Set that instance's mode to `Normal`.
- Set the TELEM3 serial baud selector to 115200 8N1.
- For PX4 1.17, set `MAV_PROTO_VER=1` as required by MicoAir. This setting is global; verify that the companion link still negotiates/operates as intended.
- Enable optical-flow and range-aid fusion using `EKF2_OF_CTRL` and `EKF2_RNG_CTRL` after raw data is valid.
- Set `SENS_FLOW_ROT` to the measured installation rotation.

Use `listener vehicle_optical_flow` and `listener distance_sensor` while moving the unarmed vehicle over textured, well-lit surfaces at known heights. Selecting `EKF2_HGT_REF=Range sensor` is appropriate only after controlled low-altitude indoor testing; it is not a universal outdoor configuration.

## Companion link: choose one service per port

Use TELEM2/UART2 for exactly one primary service:

- **MAVLink:** configure a MAVLink instance on TELEM2 in `Onboard` mode and choose a baud rate proven reliable by wiring tests.
- **ROS 2/uXRCE-DDS:** disable the competing MAVLink instance on TELEM2 and set `UXRCE_DDS_CFG` to TELEM2.

Cross Pi and FC TX/RX, share signal ground, use 3.3 V UART logic, and power the Pi separately. Follow the official [PX4 Raspberry Pi companion guide](https://docs.px4.io/v1.17/en/companion_computer/pixhawk_rpi).

## ESC and motor output

Start with DShot300. The original AIO's AM32 ESC supports DShot, but PX4 does not provide the vendor's ESC passthrough workflow and the vendor says PX4 does not support bidirectional DShot on this hardware path. Configure/update AM32 through a supported Betaflight or INAV procedure only after backing up settings and verifying the exact ESC revision.

With propellers removed, verify motor numbering, rotation, disarm behavior, and output mapping. The board groups PWM outputs 1–4, 5–6, and 7–8; do not assume an individual update rate inside a group.

## Logging and reproducibility

Archive the PX4 tag/commit, custom board diff, `.px4` artifact checksum, parameter export, QGroundControl version, ESC firmware/settings, ELRS versions, boot log, and a short ULog from each acceptance stage. Never publish Wi-Fi credentials, ELRS binding phrases, or precise home coordinates.
