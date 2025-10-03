from setuptools import setup, find_packages

setup(
    name="agentlang",
    version="0.1.0",
    description="A programming language where text has semantic properties",
    author="Lexical Mathical",
    packages=find_packages(),
    install_requires=[
        "polycli",  # Assuming PolyCLI is installable
    ],
    entry_points={
        'console_scripts': [
            'agentlang=agentlang.cli:main',
            'al=agentlang.cli:main',
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)