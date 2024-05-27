Import("env")

from os.path import join

def merge_action(source, target, env):
    target_elf = join("$BUILD_DIR", "${PROGNAME}.elf")
    target_hex = join("$BUILD_DIR", "${PROGNAME}.hex")
    env.Execute(f"$OBJCOPY -O ihex {target_elf} {target_hex}")
    softdevice_path = f"$PROJECT_DATA_DIR/s140_nrf52_6.1.0_softdevice.hex"
    target_firm = f"$BUILD_DIR/firmware_sd.hex"
    env.Execute(f"mergehex -m {softdevice_path} {target_hex} -o ${target_firm}")


env.AddCustomTarget(
    "merge",
    [join("$BUILD_DIR", "${PROGNAME}.elf")],
    [merge_action],
    title="Merge FW+SD",
    description="Merge the firmware together with softdevice to flash it via the programmer",
    always_build=True
)
