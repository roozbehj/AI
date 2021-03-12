from setuptools import setup, find_packages

setup(
    name='acrtest',
    version='1.0',
    packages=find_packages(),
    url='',
    license='NielsenIQ',
    author='Roozbeh Jalali',
    author_email='roozbeh.jalali@nielseniq.com',
    description='wrapper api',
    install_requires=[
        'uvicorn==0.13.3',
        'fastapi==0.63.0',
        'setuptools==52.0.0',
        'requests==2.25.1',
        'pydantic==1.7.3',
        'slack-sdk==3.4.0'

    ],
    python_requires='>=3,<3.9',
    entry_points={'console_scripts':['acrtest=source:runner']}
)
