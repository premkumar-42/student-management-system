import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "manage.py",
        "dumpdata",
        "home",
        "students",
        "--natural-foreign",
        "--natural-primary",
        "--indent",
        "2"
    ],
    capture_output=True
)

if result.returncode != 0:
    print(result.stderr.decode())
    sys.exit(1)

with open("app_data.json", "wb") as file:
    file.write(result.stdout)

print("app_data.json created successfully")