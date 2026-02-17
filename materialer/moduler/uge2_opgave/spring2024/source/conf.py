
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html



import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Introduktion til python'
copyright = '2024, Claus Bove'
author = 'Claus Bove'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "sphinx_rtd_theme",
        "nbsphinx",
        "recommonmark",
        "sphinx_togglebutton",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_show_sourcelink = False

html_css_files = [
    'css/custom.css',
]

html_context = {
    "display_github": True,
    "github_url" : "https://github.com/python-elective-kea/spring2024",

    # Set the following variables to generate the resulting github URL for each page. 
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}
    #/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    #https://github.com/runawayhorse001/SphinxGithub/blob/master/doc/index.rst
    'github_user': 'python-elective-kea',
    'github_repo': 'spring2024',
    'github_version': 'master/source/' ,

}
