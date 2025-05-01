from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="automated_earnings_bot",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An automated trading bot for options strategies around earnings announcements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/automated_earnings_bot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "earnings-bot=automated_earnings_bot.scheduler:main",
        ],
    },
)
