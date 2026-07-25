# Compatibility assessment

## Summary matrix

| Pair or subsystem | Status | Evidence and action |
|---|---|---|
| FlyLens 85 ↔ AIO | Plausible | Both document a 25.5 × 25.5 mm FC pattern; check 36 × 36 × 8 mm board envelope, USB access, stack height, and fastener diameter |
| AIO ↔ PX4 | Supported | Original AIO has the mainline target `micoair_h743-aio`; support is documented from PX4 1.16 and present in v1.17.0 |
| Frame ↔ motors | Unresolved | Flywoo pages describe different motor patterns across revisions; measure the actual frame and compare with the manufacturer's motor drawing |
| Frame ↔ propulsion | Not validated | Frame is a 2-inch platform; QPT specifies these motors for 2.5–4-inch props and gives no matched 2-inch test data |
| AIO ↔ 3S LiHV | Electrically within input range | 13.05 V full charge is inside the original AIO's documented 10–27 V range; voltage/current calibration still required |
| Motors ↔ one 3S pack | Unproven | Motor supports 3S, but the exact prop/current curve is absent; pack capability and connector loss need measurement |
| Motors ↔ two packs in series | Incompatible | A 6S LiHV assembly reaches 26.1 V; AIO accepts it, but the motor manufacturer specifies only 3S/4S |
| Pi ↔ AIO 5 V BEC | Inadequate design margin | AIO provides 5 V/2 A; official Pi recommendations are 5 V/3 A for Pi 4 and 5 V/5 A for Pi 5 |
| MG-A01 ↔ PX4 | Plausible | GNSS uses UBX over UART and QMC5883L over I2C; PX4 includes both paths, but the supplied “AG01” identity must be confirmed |
| MTF-01 ↔ PX4 | Supported with configuration | Vendor supplies PX4 MAVLink mode and PX4 1.17-specific protocol guidance; validate flow/range topics and orientation |
| Nexus1 ↔ PX4 | Supported with a custom CRSF build | Full CRSF telemetry requires the PX4 CRSF driver and removal of the generic RC input driver conflict |
| RadioMaster Pocket ↔ Nexus1 | Variant-dependent | Pocket ELRS is direct; Pocket CC2500 needs a compatible external ELRS module; ELRS major version and regulatory domain must match |
| C10 Pro ↔ vehicle power | Blocked | Available C10 Pro material says 7.2–12 V while an official C10 manual says 7.2–72 V; 3S LiHV reaches 13.05 V |
| C10 Pro ↔ Pi/PX4 | Blocked | No verified direct network, serial, MAVLink, or gimbal-control path is established by the listed hardware |

## Propulsion risk

The motor page lists a 14.5 A maximum current and 240 W maximum power, but does not state the battery, propeller, air density, test duration, or thermal limit associated with the headline figures. Four headline currents total 58 A. A battery label calculation gives 0.45 Ah × 75 C = 33.75 A per pack, but the vendor does not identify that label as continuous or burst capability. Neither figure is a safe sizing basis.

Select an exact 2-inch propeller only after checking hub and shaft fit. Run one motor/ESC channel on a guarded thrust stand at 3S across the commanded operating range. Measure thrust, bus voltage, current, RPM if available, vibration, winding/ESC temperature, and transient behavior. Establish a conservative current limit from measured thermal and voltage-sag data.

## Mechanical risk

Flywoo's current frame page lists a 6.6 mm motor-hole dimension with 1.4 mm holes, while its V1.3 change note says support was added for 9 × 9 mm motor mounting. The QPT drawing appears to show a four-M2 rear pattern on a 9 mm pitch circle. These are not interchangeable descriptions. Measure hole-center geometry and screw clearance on the actual parts; do not drill or force-fit carbon or motor windings based on the product names.

## Software compatibility caveat

The Zerodrag manual's page labelled “PX4 / ARDUPILOT” shows an ArduPilot `SERIAL1_PROTOCOL=RCIN` instruction. That is not a PX4 v1.17 parameter and must not be used for this build. Follow the [PX4 CRSF procedure](px4-integration.md) instead.
