from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leadpage_text_manager",
    version="0.1.0",
    author="Hiteshkumar Gupta",
    author_email="hiteshgupta2198@gmail.com",
    description="A tool to extract and replace text in JSON files for LeadPages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hmgtech/leadpage-test",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'annotated-types==0.7.0',
        'cachetools==5.3.3',
        'certifi==2024.6.2',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'google-ai-generativelanguage==0.6.6',
        'google-api-core==2.19.1',
        'google-api-python-client==2.135.0',
        'google-auth==2.30.0',
        'google-auth-httplib2==0.2.0',
        'google-generativeai==0.7.1',
        'googleapis-common-protos==1.63.2',
        'grpcio==1.64.1',
        'grpcio-tools==1.64.1',
        'httplib2==0.22.0',
        'idna==3.7',
        'proto-plus==1.24.0',
        'protobuf==5.27.2',
        'pyasn1==0.6.0',
        'pyasn1-modules==0.4.0',
        'pydantic==2.7.4',
        'pydantic-core==2.18.4',
        'pyparsing==3.1.2',
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'rsa==4.9',
        'tqdm==4.66.4',
        'typing-extensions==4.12.2',
        'uritemplate==4.1.1',
        'urllib3==2.2.2',
    ],
    entry_points={
        'console_scripts': [
            'leadpage-text-manager=main:main',
        ],
    },
)
