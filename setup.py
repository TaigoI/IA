from setuptools import setup

setup(name='COMP380-IA',
      version='1.0',
      description='Código entregue',
      url='https://github.com/TaigoI/UFAL-COMP380-InteligenciaArtificial',
      author='Taígo Pedrosa',
      author_email='timp1@ic.ufal.br',
      license='AskFirst',
      packages=['ReavAB1', 'ListaAB2'],
      install_requires=[
          'numpy',
          'scikit-fuzzy',
          'matplotlib'
      ],
      zip_safe=False)
