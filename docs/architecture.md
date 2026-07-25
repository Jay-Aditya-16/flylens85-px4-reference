# Proposed architecture

This is a logical allocation for bench bring-up, not an as-built wiring diagram. Connector orientation and power pins must be verified against the exact board revision before assembly.

```mermaid
flowchart LR
    TX[RadioMaster Pocket\nELRS variant?] -. 2.4 GHz CRSF .-> RX[Zerodrag Nexus1]
    RX -- UART6 / RC\nCRSF TX + RX --> FC[MicoAir743-AIO-35A\nPX4 v1.17.0]
    GPS[MicoAir MG-A01?] -- UART3 / GPS1\nUBX --> FC
    GPS -- I2C1\nQMC5883L --> FC
    FLOW[MicoAir MTF-01] -- UART4 / TELEM3\nMAVLink v1, 115200 --> FC
    FC -- UART2 / TELEM2\nMAVLink 2 or uXRCE-DDS --> PI[Raspberry Pi 4/5 8 GB?]
    FC -- DShot300 --> ESC[Integrated 4-in-1 ESC]
    ESC --> M1[4 × QPT 1404.5 KV4500]
    CAM[SkyDroid C10 Pro?] -. unverified video/control path .-> PI
    BATT[One LAVA 3S 450 mAh\n13.05 V full] --> FC
    BATT --> REG5[Dedicated 5 V regulator]
    REG5 --> PI
    BATT --> REGCAM[Camera regulator\nonly after input rating is known]
    REGCAM --> CAM
```

## Design choices

- **One battery initially:** the two batteries are treated as two interchangeable packs, not as an authorized series or parallel assembly.
- **Pi on its own regulator:** the AIO's 5 V/2 A BEC is reserved for low-power avionics and cannot cover the recommended supply capacity of a Pi 4/5.
- **MTF-01 on TELEM3:** this leaves TELEM2 for the companion computer and avoids the AIO's TELEM2/VTX-HD sharing problem.
- **CRSF on the RC UART:** full-duplex CRSF needs both TX and RX. It must not be connected as one-wire inverted SBUS if receiver telemetry is required.
- **Camera path unresolved:** no source establishes direct MAVLink camera/gimbal support, a network path to the Pi, or direct gimbal control from the RadioMaster transmitter.

## Physical-layout constraints

The C10 Pro and MTF-01 both need an unobstructed downward/forward view. The GNSS antenna needs sky visibility and separation from motors, ESC switching currents, the ELRS antenna, Pi digital noise, and camera electronics. These needs are difficult to satisfy on an 85 mm frame. Record a dimensioned CAD/layout drawing, center of gravity, antenna placement, sensor rotations, and cable strain relief before fabrication.
