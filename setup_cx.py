import sys
from cx_Freeze import setup, Executable
from setup import NAME, VERSION, DESCRIPTION


PATH_ICON = "resources/images/icone.ico"

# run: "python setup_cx.py build" to build the exe
# run: "python setup_cx.py bdist_msi" to build the msi (installer for windows)

build_exe_options = {
    "packages": [],
    "optimize": 0,
    "excludes": ["tkinter", "ssl", "bz2", "numpy.random._examples"],
    "include_files": ['resources/']
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

msi_data = {
    "ProgId": [
        ("Prog.Id", None, None, DESCRIPTION, "IconId", None),
    ],
    "Icon": [
        ("IconId", PATH_ICON),
    ],
}

bdist_msi_options = {
    "add_to_path": False,
    "data": msi_data,
}

executables = [
    Executable(
        "main.py",
        targetName=NAME,
        base=base,
        icon=PATH_ICON,
        shortcut_name=NAME,
        shortcut_dir="DesktopFolder"
    ),
    Executable(
        "otimizador.py",
        targetName="otimizador",
        base=None,
        shortcut_name="otimizador",
    )
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables
)
