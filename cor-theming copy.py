import os 

from tutor import hooks

################# Configuration
config = {
    # Add here your new settings
    "defaults": {
        "VERSION": "1.0",
        "WELCOME_MESSAGE": "Licensing & Training. Simplified",
        "PRIMARY_COLOR": "#54698C", 
        # Footer links are dictionaries with a "title" and "url"
        # To remove all links, run:
        # tutor config save --set INDIGO_FOOTER_NAV_LINKS=[] --set INDIGO_FOOTER_LEGAL_LINKS=[]
        "FOOTER_NAV_LINKS": [
            {"title": "About", "url": "https://adjusterpro.com/about/"},
            {"title": "Contact", "url": "https://adjusterpro.com/support/"},
            {"title": "Privacy Policy", "url": "https://adjusterpro.com/privacy-policy/"},
        ],
        "FOOTER_LEGAL_LINKS": [
            {"title": "Terms of service", "url": "/tos"},
            {
                "title": "COR theme for Open edX",
                "url": "https://github.com/AdjusterPro/cor-tutor-indigo",
            },
        ],
    },
    "unique": {},
    "overrides": {
        "PLATFORM_NAME": "COR Learning Classroom Demo",
    },
}

# Theme templates
current_dir = os.path.abspath(".")

hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    current_dir + "/theme-templates/"
)
# This is where the theme is rendered in the openedx build directory
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("cor-theme", "build/openedx/themes"),
    ],
)

# Force the rendering of scss files, even though they are included in a "partials" directory
hooks.Filters.ENV_PATTERNS_INCLUDE.add_item(
    r"cor-theme/lms/static/sass/partials/lms/theme/"
)

# Load all configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["defaults"].items()]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [(f"INDIGO_{key}", value) for key, value in config["unique"].items()]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(
    [(f"{key}", value) for key, value in config["overrides"].items()]
)

   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;jkcdfhbvdfikbdfkuzhndikufbh ≥≤≈πø©ƒøπ©®ƒ∂πø®†µ©bhbg/6j054/-69 4sÍÍÍÍÍÍÍÍßßßÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ-––––§–“¢∞≠¢≠≠¢–¢¿˘”ﬂ¿¿¿¿¿¿¿¿¿¿¿ﬂ—ﬂ—–==