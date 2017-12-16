from setuptools import setup, find_packages


version = "0.1.3"

setup(
    name='chartjspy',
    packages=find_packages(),
    version=version,
    description='Generate Chartjs charts from python',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/chartjspy',
    download_url='https://github.com/synw/chartjspy/releases/tag/' + version,
    keywords=['charts', 'chartjs'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    install_requires=[
        'pandas'
    ],
)
