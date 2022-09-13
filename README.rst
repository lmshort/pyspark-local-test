make sure pyspark version is the same as the spark version (3.2.2 in this case)


Ensure the following variables are specified in the .bashrc
(assuming the spark version is installed)

    # python
    alias python="$(pyenv which python)"
    export PATH="/home/lshort/.local/bin:$PATH"

    # spark stuff
    export SPARK_HOME="/usr/local/spark"
    export PATH="$PATH:/usr/local/spark/bin"

    # temp modified for project
    export PYSPARK_PYTHON="/home/lshort/.cache/pypoetry/virtualenvs/spark-test-0xdx9Ytf-py3.9/bin/python"
    #export PYSPARK_PYTHON=$(which python)

    export PYSPARK_DRIVER_PYTHON="/home/lshort/.cache/pypoetry/virtualenvs/spark-test-0xdx9Ytf-py3.9/bin/python"
    #export PYSPARK_DRIVER_PYTHON=$(which python)


When starting the project, initialise the env:

poetry shell

then run:


poetry run python spark_test/entry_point.py


gitignore added to various cache directories

poetry install

run the following for git pre-commit inclusion
pre-commit install



to run:
poetry run python spark_test/entry_point.py
