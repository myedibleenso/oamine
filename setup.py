from setuptools import find_packages, setup
import os

from oamine import info


# use requirements.txt as deps list
with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

# get readme
with open("README.md", "r") as f:
    readme = f.read()

test_deps = required + ["green==3.3.0", "coverage==6.2", "mypy==0.931"]
# NOTE: <packagename> @ allows installation of git-based URLs
dev_deps = test_deps + [
    "black==21.12b0",
    "wheel==0.37.1",
    # "black @ git+git://github.com/psf/black.git",
    "mkdocs==1.2.3",
    # "portray @ git+git://github.com/myedibleenso/portray.git@issue/83",
    # "portray @ git+git://github.com/myedibleenso/portray.git@avoid-regressions",
    # "mkapi==1.0.14",
    "pdoc3==0.10.0",
    "mkdocs-git-snippet==0.1.1",
    "mkdocs-git-revision-date-localized-plugin==0.11.1",
    "mkdocs-git-authors-plugin==0.6.3",
    "mkdocs-rtd-dropdown==1.0.2",
    #"pre-commit==2.16.0",
]

setup(
    name="oamine",
    python_requires=">=3.8",
    version=info.version,
    # declare your packages
    packages=find_packages(where="oamine", exclude=("test",)),
    package_dir={"": "oamine"},
    keywords=["nlp"],
    # see https://setuptools.pypa.io/en/latest/userguide/datafiles.html#subdirectory-for-data-files
    package_data={
      "oamine.candidate_generation.data": ["*.txt"],
      "oamine.candidate_generation.data.model": [""],
    },
    description=info.description,
    long_description=readme,
    long_description_content_type="text/markdown",
    url=info.repo,
    download_url=info.download_url,
    author=" and ".join(info.authors),
    author_email=info.contact,
    license=info.license,
    # see https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
    scripts=[os.path.join("bin", file) for file in os.listdir("bin")],
    install_requires=required,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
    ],
    tests_require=test_deps,
    extras_require={
        "test": test_deps,
        "all": dev_deps
    },
    include_package_data=True,
    zip_safe=False,
)