from setuptools import setup, find_packages

setup(
    name="practical_college",  # Your package name
    version="0.1.0",           # Initial version
    author="Your Name",        # Replace with your name
    author_email="your.email@example.com",  # Your email
    description="A practical college project",  # Brief description
    long_description=open("README.md").read(),  # Optional: README as description
    long_description_content_type="text/markdown",
    url="https://github.com/Tochage143/college",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically include all Python packages
    python_requires=">=3.6",   # Minimum Python version
)
