import subprocess


def get_display_adapters():
    try:
        # Run WMIC to get display adapter name and driver version
        result = subprocess.run(
            ['wmic', 'path', 'win32_videocontroller', 'get', 'name, driverversion'],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split('\n')
        headers = lines[0].strip()
        adapter_lines = lines[1:]

        print(f"{headers}")
        for line in adapter_lines:
            if line.strip():
                print(line.strip())

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    get_display_adapters()
