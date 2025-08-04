# import subprocess
#
# result = subprocess.run(['wmic', 'bios', 'get', 'SMBIOSBIOSVersion'], capture_output=True, text=True)
#
# print("BIOS Version:", result.stdout)


# import subprocess
#
# result = subprocess.run(['wmic', 'os', 'get', 'Caption'], capture_output=True, text=True)
# print("OS Version:", result.stdout.strip())


# import subprocess
#
# result = subprocess.run(['systeminfo'], capture_output=True, text=True)
# output_lines = result.stdout.splitlines()
#
# # Extract line that contains OS Name or Version
# for line in output_lines:
#     if "OS Name" in line or "OS Version" in line:
#         print(line.strip())
#
# import subprocess
#
#
# def get_display_driver_info():
#     print("Fetching Display Driver Info...\n")
#
#     result = subprocess.run(
#         ['wmic', 'path', 'Win32_VideoController', 'get', 'Name,DriverVersion,DriverDate'],
#         capture_output=True, text=True
#     )
#
#     if result.returncode == 0:
#         output = result.stdout.strip()
#         print("Display Driver Info:\n")
#         print(output)
#     else:
#         print("Failed to fetch display driver info.\nError:", result.stderr)
#
#
# get_display_driver_info()


import subprocess
import platform
import datetime

# Set expected version keyword or number (be flexible!)
EXPECTED_VERSION = "1.59"
LOG_FILE = "firmware_validation_log.txt"


def get_firmware_version():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["wmic", "bios", "get", "SMBIOSBIOSVersion"],
                capture_output=True,
                text=True
            )
            lines = result.stdout.strip().split('\n')
            version_lines = [line.strip() for line in lines if line.strip() and "SMBIOS" not in line]
            version = version_lines[0] if version_lines else "UNKNOWN"
        elif platform.system() == "Linux":
            result = subprocess.run(
                ["sudo", "dmidecode", "-s", "bios-version"],
                capture_output=True,
                text=True
            )
            version = result.stdout.strip()
        else:
            version = "Unsupported OS"
    except Exception as e:
        version = f"Error: {e}"
    return version


def log_result(status, current_version):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] Firmware Version: {current_version} | Status: {status}\n"
    with open(LOG_FILE, 'w') as f:
        f.write(line)
    print(line.strip())


def validate_firmware():
    current_version = get_firmware_version()
    # Normalize version strings and check if expected version is contained
    if EXPECTED_VERSION.replace(" ", "") in current_version.replace(" ", ""):
        log_result("PASS", current_version)
    else:
        log_result("FAIL", current_version)


if __name__ == "__main__":
    validate_firmware()
