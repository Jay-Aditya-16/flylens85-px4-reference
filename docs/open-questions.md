# Open questions and required evidence

These questions block a reproducible final wiring diagram or flight configuration.

## Identity

- [ ] Which Raspberry Pi model and board revision is the 8 GB board? On the Pi, capture `tr -d '\\0' </proc/device-tree/model`.
- [ ] Does the GNSS label say `MG-A01`, `AG01`, or something else? Photograph both sides and its harness.
- [ ] Does the AIO silkscreen identify original `MicoAir743-AIO-35A` or `MicoAir743V2-AIO-35A`?
- [ ] Is the RadioMaster Pocket the internal 2.4 GHz ELRS or CC2500 variant? Record firmware and regulatory-domain choice without publishing a binding phrase.
- [ ] Is the receiver a Nexus1? Record its target, ExpressLRS major version, antenna type, and firmware options.
- [ ] What exact C10 Pro label, connector set, firmware, and manual accompanied the unit?
- [ ] What FlyLens frame revision is present?

## Mechanical and propulsion

- [ ] What are the measured motor-hole geometry and fastener diameters on the frame and motor?
- [ ] What exact propeller manufacturer, model, diameter, pitch, blade count, hub bore, and rotation are proposed?
- [ ] What thrust/current/temperature results does that motor/prop combination produce across one 3S pack's operating voltage?
- [ ] What are the complete takeoff mass, CG, principal dimensions, and estimated inertia with one battery?
- [ ] How are camera, Pi, GNSS, optical flow, antennas, cooling, and strain relief mounted without blocked fields of view or prop contact?

## Electrical and data

- [ ] Are the two batteries alternatives, a parallel pair, or intended for series? Series is currently rejected.
- [ ] Which dedicated Pi regulator meets transient, thermal, ripple, and brownout requirements?
- [ ] What is the exact safe C10 Pro input range and pinout? Do not infer it from the C10 manual.
- [ ] Does the camera require a SkyDroid air unit, and can the specific unit expose RTSP/control directly to the Pi?
- [ ] Is gimbal control app/SDK-only, or is there a documented serial/network protocol suitable for a companion adapter?
- [ ] Will TELEM2 carry MAVLink or uXRCE-DDS?
- [ ] Does `MAV_PROTO_VER=1` for MTF-01 coexist reliably with the selected companion protocol?

## Software and operations

- [ ] What custom PX4 board diff enables CRSF while removing the generic RC input conflict?
- [ ] What airframe geometry, actuator mapping, control gains, and estimator settings follow from the measured vehicle?
- [ ] What are the verified lost-RC, lost-position, low-battery, companion-loss, and geofence behaviors?
- [ ] Which applicable mass, radio-domain, registration, operating-area, and flight rules govern the intended location?

Close an item by linking measured evidence, a primary source, and the resulting design decision. Preserve superseded evidence rather than rewriting history.
