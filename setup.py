import os
from setuptools import setup, find_packages

# 读取 README 作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linkedin-api",
    version="1.1.1",  # 基于你仓库的最新版本
    description="Unofficial LinkedIn API for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tomquirk",  # 原作者
    author_email="tomquirkacc@gmail.com",  # 推测的作者邮箱
    maintainer="qds1014",  # 你作为维护者
    url="https://github.com/qds1014/linkedin-api",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "lxml>=4.6.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
    keywords="linkedin api scraper social-media professional-network",
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/qds1014/linkedin-api/issues",
        "Source": "https://github.com/qds1014/linkedin-api",
    },
)
