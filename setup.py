from setuptools import setup
setup(
    name="spark-prometheus",
    version="0.1",
    scripts=['src/main.py'],
    install_requires=['pyspark', 'prometheus_client'],
    packages=['src'],
    author="Sanjay Mishra",
    author_email="admin@devrats.com",
    description="This is to demonstrate monitoring using prometheus",
    keywords="pyspark prometheus monitoring",
    url="http://devrats.com",
    project_urls={
        "Source Code": "https://github.com/sanjurm16/spark-prometheus"
    }
)
