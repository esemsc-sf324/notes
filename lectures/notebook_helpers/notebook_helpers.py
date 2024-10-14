from setuptools import setup, find_packages

setup(
    name='notebook_helpers',
    version='0.1',
    packages=find_packages(),  # 自动查找并包含 __init__.py 文件的所有包
    description='A helper package for Jupyter notebook notes',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        # 列出包的依赖，例如 'numpy', 'pandas' 等
    ],
)