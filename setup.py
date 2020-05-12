from setuptools import setup, find_packages

setup(name='gym_oddsevens',
        version='0.1',
        description='An OpenAI environment for the Odds and Evens game.',
        url='#',
        author='Rafael Neves',
        author_email='rafael@diskless.io',
        license='BSD 2-clause',
        package_dir={'': 'src'},
        install_requires=['gym', 'numpy'],
        zip_safe=False)

