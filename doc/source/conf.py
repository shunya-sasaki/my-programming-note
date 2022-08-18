import platform

platform_name = platform.system()  # Windows, Darwin, Linux

project = "My programming note"
copyright = "Shunya Sasaki"
author = "Shunya Sasaki"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.blockdiag",
]
language = "ja"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# blockdiag
blockdiag_html_image_format = "SVG"
blockdiag_html_image_format = "SVG"
if platform_name == "Darwin":
    blockdiag_fontpath = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    # 'style_nav_header_background': '#aaaaaa',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}