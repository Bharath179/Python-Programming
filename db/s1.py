import datetime
import platform
import subprocess

EXPECTED_DRIVER_VERSION = "12.19.1.37"
EXPECTED_DEVICE_KEYWORD = "Intel"
LOG_FILE = "network_driver_validation_log.txt"
INFO_FILE = "system_info.txt"


def get_network_adapter_info():
    try:
        # Get all network adapter names
        result = subprocess.run(
            ['wmic', 'nic', 'get', 'Name'],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split('\n')
        adapter_names = [line.strip() for line in lines if line.strip() and "Name" not in line]
        # Check if expected adapter is present
        for name in adapter_names:
            if EXPECTED_DEVICE_KEYWORD.lower() in name.lower():
                return name
        return "Not Found"
    except Exception as e:
        return f"Error: {e}"


def get_driver_version(device_keyword):
    try:
        # Query device driver version for matching device
        query = f"wmic path win32_pnpsigneddriver where \"devicename like '%{device_keyword}%'\" get devicename, driverversion"
        result = subprocess.run(query, capture_output=True, text=True, shell=True)
        lines = result.stdout.strip().split('\n')
        version_lines = [line.strip() for line in lines if line.strip() and "DriverVersion" not in line]
        if version_lines:
            # Return the first matching version
            return version_lines[0]
        return "UNKNOWN"
    except Exception as e:
        return f"Error: {e}"


def save_system_info():
    try:
        with open(INFO_FILE, 'w') as f:
            result = subprocess.run(['systeminfo'], capture_output=True, text=True)
            f.write(result.stdout)
    except Exception as e:
        print("Failed to collect system info:", e)


def log_result(status, device_name, driver_info):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] Adapter: {device_name} | Driver Info: {driver_info} | Status: {status}\n"
    with open(LOG_FILE, 'a') as f:
        f.write(log_line)
    print(log_line.strip())


def validate_network_driver():
    device_name = get_network_adapter_info()
    if device_name == "Not Found":
        log_result("FAIL", "None", "Adapter not found")
        return

    driver_info = get_driver_version(EXPECTED_DEVICE_KEYWORD)
    if EXPECTED_DRIVER_VERSION in driver_info:
        log_result("PASS", device_name, driver_info)
    else:
        log_result("FAIL", device_name, driver_info)
        print("ALERT: Outdated driver detected!")

    save_system_info()


if __name__ == "__main__":
    if platform.system() == "Windows":
        validate_network_driver()
    else:
        print("Only Windows is supported in this script.")
