from paver.tasks import task, BuildFailure, needs
from paver.easy import sh


@task
def acceptance_tests():
    sh('behave tests/acceptance --tags=-pending')


@task
def unit_system_tests():
    sh('py.test -v -r f --cov-report term-missing --cov=bank_app/ tests/')


@task
def run_pylint():
    try:
        sh('pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" bank/ > pylint.txt'
           )
    except BuildFailure:
        pass


@task
def format_python_code():
    sh('yapf  -i -r -p -e venv .')


@needs('unit_system_tests', 'acceptance_tests', 'run_pylint',
       'format_python_code')
@task
def default():
    pass
