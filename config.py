import appdirs

# DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING

NAME = "PyMCL"
ICON = ""
LOGO = ""
BACKGROUND = ""
UPDATE_URL = "https://github.com/ModificationStation/PyMCL/raw/master/version.json"
MODPACK_DB = "https://github.com/ModificationStation/PyMCL/raw/master/modpacks.json"
BLOG_BACKGROUND = "blogbackground.png"
BLOG = ""

DEFAULT_LAUNCHER_CONFIG = """
{
    "lastusedname": ""
}
"""

DEFAULT_INSTANCE_CONFIG = """
{
    "maxram": "512m",
    "minram": "256m",
    "javaargs": ""
}
"""

# Debug purposes. If you change this, all users complaining about crashes, etc, becomes your problem.
VER = "v0.5 Alpha"

MC_DIR = appdirs.user_data_dir(".PyMCL", "", roaming=True)
