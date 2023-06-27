from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tns/__init__.py
from tns import __version__ as version

setup(
	name="tns",
	version=version,
	description="A transformative, AI-powered tool built with the Frappe framework, The Narrative Scribe guides users through self-authoring exercises to foster personal growth. It leverages AI for sentiment analysis, providing insightful feedback on user narratives and fostering self-awareness and goal-setting.",
	author="The Narrative Scribe",
	author_email="tech@narrativescribe.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
