# Bring-up and test plan

Do not skip stages. A failed acceptance item returns the build to the preceding safe state.

## 0. Identify the hardware

- Photograph every label, PCB side, connector, and included harness.
- Record frame revision, AIO silkscreen and MCU/IMU markings, Pi model, Pocket RF variant, receiver name/firmware, camera firmware/label, and battery lot.
- Measure the frame motor pattern, motor base pattern, board envelope, camera envelope, and all connector voltages/polarities.
- Select the exact propeller only after dimensional and guarded propulsion review.

**Gate:** all `exact_*` and label-related items in [open questions](open-questions.md) have evidence.

## 1. Mechanical mock-up

Use inert mass dummies or unpowered parts. Check screw length against windings/PCB, prop clearance, center of gravity, camera and optical-flow fields of view, GNSS/antenna clearance, USB/SD access, cooling, cable bend radius, and crash loads.

**Gate:** dimensioned layout, mass, CG, fastener schedule, and sensor rotations are recorded.

## 2. Power tree on the bench

With all loads disconnected, energize each regulator from a current-limited supply. Verify startup/steady voltage, ripple, polarity, protection, thermal performance, and brownout recovery. Add loads one at a time: FC, receiver, GNSS, MTF-01, Pi, then camera.

**Gate:** every rail stays within device limits across the intended battery range and worst measured transient.

## 3. Flight controller and PX4

Flash the pinned target by USB, confirm SD logging, back up parameters, calibrate voltage/current, check all IMUs/barometer, and record the boot log. Do not connect motors yet.

**Gate:** no unexpected sensor or storage errors; power measurements agree with instruments.

## 4. Sensors and companion

Bring up GNSS, compass, MTF-01, and Pi one at a time. Validate timestamps, update rate, orientation, dropouts, CPU load, serial errors, and log content. Exercise Pi and camera workloads while monitoring sensor noise.

**Gate:** raw data is valid before estimator fusion; GNSS/compass remain usable during worst digital/power load.

## 5. RC and failsafes

Bind with the correct regulatory domain and matching ExpressLRS major version. Verify channel order/range, arming switch, link quality, telemetry, receiver power cycling, and deliberate transmitter/link loss with outputs disabled.

**Gate:** PX4 enters the documented failsafe state every time and cannot arm unexpectedly.

## 6. Motor checks without propellers

Use a smoke stopper/current limit. Confirm motor number, direction, DShot behavior, idle/current balance, disarm, emergency stop, ESC temperature, and that sensor streams remain clean.

**Gate:** mapping and direction match the selected PX4 airframe; no desync, reset, excessive vibration, or hot component.

## 7. Guarded propulsion characterization

Test one exact motor/prop/ESC channel on a thrust stand at 3S, then validate the integrated powertrain behind a barrier. Log voltage, current, thrust, RPM if available, temperature, vibration, and duration. Reject any prop contact, structural resonance, connector heating, excessive battery sag, or unexplained current imbalance.

**Gate:** measured thrust and control margin support the final measured takeoff mass with conservative electrical/thermal headroom.

## 8. Restrained and staged flight tests

Complete estimator checks and actuator tests in a controlled test area. Start with a protected/restrained low-power test, then a brief low hover without optional payloads if the reviewed test plan permits it. Add payloads one at a time; review ULogs between changes.

**Gate:** a responsible operator approves each next envelope step under applicable local rules. A successful hover is not proof of long-duration reliability or airworthiness.
