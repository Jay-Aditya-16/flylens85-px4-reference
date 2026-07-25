# Interfaces and wiring allocation

## Proposed AIO port map

The original MicoAir743-AIO-35A exposes seven UARTs. The manufacturer maps them as follows:

| PX4 device | MCU UART | Proposed use | Electrical/protocol notes |
|---|---:|---|---|
| `ttyS0` / TELEM1 | UART1 | Spare bench telemetry | 3.3 V UART; do not connect USB-level RS-232 |
| `ttyS1` / TELEM2 | UART2 | Raspberry Pi | Shares the VTX-HD connector; allocate it to only one service/device |
| `ttyS2` / GPS1 | UART3 | MG-A01 GNSS | 3.3 V UART, UBX, 115200 default on module |
| `ttyS3` / TELEM3 | UART4 | MTF-01 | 3.3 V UART, MAVLink_PX4, 115200 |
| `ttyS4` / RC | UART6 | Nexus1 CRSF | Full duplex: receiver TX → FC RX6 and receiver RX → FC TX6 |
| `ttyS5` / ESC | UART7 | Integrated ESC | Board-internal ESC communication; do not repurpose |
| `ttyS6` / TELEM4 | UART8 | Spare | Reserve for debug or a later payload |
| I2C1 | I2C | MG-A01 compass | QMC5883L; SDA/SCL plus 5 V/GND at module connector |

## Power domains

| Load | Proposed source | Rule |
|---|---|---|
| AIO and motors | One 3S LAVA pack via XT30/power harness | Add current-rated wiring and observe polarity; use a smoke stopper/current-limited supply for first power-up |
| MG-A01 | AIO regulated 5 V | Confirm connector pinout and common ground |
| MTF-01 | AIO regulated 5 V | Typical published consumption is 500 mW; confirm actual current |
| Nexus1 | AIO regulated 5 V | Receiver is specified for 5 V; protect antenna connector and maintain RF clearance |
| Raspberry Pi | Dedicated regulated 5 V supply | Size for the identified Pi model, transients, peripherals, thermal derating, and cable drop |
| C10 Pro | Dedicated verified supply | Do not connect until the exact variant's maximum input voltage and polarity are confirmed |

All serial links require a common signal ground. Do not tie together independent regulator outputs unless their datasheets explicitly permit it. Power the Pi through one intended input path, not simultaneously through GPIO and USB-C.

## Connector rules

1. Identify pin 1 on both mating halves; never infer it from wire color.
2. With all loads disconnected, check regulator output voltage and polarity using a current-limited bench source.
3. Verify continuity from every harness pin to the AIO pad or schematic label.
4. Cross UART data lines: peripheral TX to FC RX, peripheral RX to FC TX.
5. Keep I2C and GNSS leads short and away from motor phase wires and the battery lead.
6. Twist power/ground pairs where practical, add strain relief, and document every connector in `evidence/`.

The AIO vendor warns that pin 1 of its VTX-HD connector is 12 V. Since TELEM2 is shared with that connector, a custom Pi harness must not accidentally route this pin into a Pi UART or 5 V rail.

## Unallocated camera connection

The official SkyDroid support material says C10 Pro control is available through the SkyDroid app/SDK and that third-party remote controllers cannot directly control the gimbal. The official player demo shows an RTSP example on a SkyDroid network, but the BOM does not list a SkyDroid air receiver or establish that the C10 Pro can attach directly to the Pi. Treat video, storage, gimbal control, telemetry overlay, and time synchronization as an open subsystem.
