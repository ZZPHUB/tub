from setuptools import setup,find_packages

setup(
    name="tub",
    version="0.1",
    author="Zhang Zhi Peng",
    author_email="3571669089@qq.com",
    url="https://github.com/ZZPHUB/tub",
    description="tub use baidu-api",
    packages=find_packages(),
    install_requires=[
        "requests",
        "urllib3"
    ],
    package_data={
        'tub':['info.json']
    }
)
print(find_packages())