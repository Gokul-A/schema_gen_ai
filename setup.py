from setuptools import setup, find_packages

setup(
    name='schema_gen_ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic>=2.11.7',
        'openai>=2.6.1',
        'anthropic>=0.71.0',
        'google-genai>=1.46.0',
    ],
    author='Gokulakrishnan Anand',
    author_email='gokula04@gmail.com', 
    description='A Python tool to generate Pydantic response schemas using various LLM APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Gokul-A/schema_gen_ai',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)