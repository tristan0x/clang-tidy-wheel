from skbuild import setup


setup(
    name="clang-format",
    version="0.0.6",
    author="Dominic Kempf",
    author_email="ssc@iwr.uni-heidelberg.de",
    packages=["clang_format"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "clang-format=clang_format:clang_format"
        ]
    },
    classifiers=[
        "Programming Language :: C",
        "Programming Language :: C++",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
    ],
    license="Apache 2.0"
)
