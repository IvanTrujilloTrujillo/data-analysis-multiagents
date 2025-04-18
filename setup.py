# Setup file

from setuptools import setup, find_packages

from version import __version__

setup(
    name="data_analysis_multiagents",
    version=__version__,
    description="Multi-agent system for data analysis",
    author="Ivan Trujillo",
    author_email="ivtrujillo12@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "langchain>=0.3.20",
        "langchain-core",
        "langchain-openai",
        "pydantic",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "ruff",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
