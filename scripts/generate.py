import subprocess
import os
from pathlib import Path
from typing import List

CUR_DIR = Path(".").resolve()
SCRIPTS_DIR = Path(__file__).parent
STUBS_DIR = Path("../stubs")
GAC_DIR = Path(os.path.expandvars("%windir%/Microsoft.NET/assembly/GAC_MSIL"))

v40_DIR = STUBS_DIR / "dotnet/v4.0"
NETCORE_DIR = Path("C:\Program Files\dotnet\shared")

# .NET FRAMEWORK
print("[*] Locating System and Microsoft assemblies in the GAC")
os.chdir(SCRIPTS_DIR)
targets: List[Path] = []
for path in GAC_DIR.iterdir():
    if path.is_dir() and path.name.split(".")[0] in ["Microsoft", "System"]:
        targets.extend([dll for dll in path.glob("**/*.dll")])

# print("[*] Building stubs for .NET v4.0 System and Microsoft assemblies")
# v40_DIR.mkdir(parents=True, exist_ok=True)
# for target in targets:
#     cmd = f'{SCRIPTS_DIR}\PyStubbler.exe --dest="{v40_DIR.resolve()}" --search="{GAC_DIR}" "{target}"'
#     print(f"**********\n{target.name}\n**********")
#     print(f"CMD: {cmd}")
#     stubs = subprocess.run(cmd, shell=True, check=True)
#     print("**********")

print("[*] Locating .NET Core Assemblies")
for apptype in NETCORE_DIR.iterdir():
    if apptype.is_dir() and apptype.name.endswith("App"):
        print(f"[*] Building stubs for {apptype.name} assemblies")

        for version in apptype.iterdir():
            version_out = Path(STUBS_DIR / f"dotnet-core/{apptype.name}/{version.name}")
            version_out.mkdir(parents=True, exist_ok=True)

            targets: List[Path] = []

            targets.extend([dll for dll in version.glob("Microsoft.*.dll")])
            targets.extend([dll for dll in version.glob("System.*.dll")])
            for target in targets:
                cmd = f'{SCRIPTS_DIR}\PyStubblerCore.exe --dest="{version_out.resolve()}" --search="{version}" "{target}"'
                print(f"**********\n{target.name}\n**********")
                print(f"CMD: {cmd}")
                stubs = subprocess.run(cmd, shell=True, check=True)
                print("**********\n")


os.chdir(CUR_DIR)
