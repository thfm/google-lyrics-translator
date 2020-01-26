from setuptools import setup

setup(
    name="google-lyrics-translator",
    version="0.1",
    description="A fun little program that destroys the lyrics of " +
    "your favourite songs using Google Translate.",
    long_description=open("README.md").read(),
    py_modules=["translator"],
    install_requires=["click", "googletrans"],
    entry_points="""
        [console_scripts]
        translate=translator:translate_lyrics
    """
)
