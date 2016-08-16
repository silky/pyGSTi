#!/usr/bin/env python3
from __future__                  import print_function, division, unicode_literals, absolute_import
from helpers.automation_tools    import directory, get_changed_packages
import subprocess, argparse, shutil, sys, os

'''
Script for running the test suite.

see pyGSTi/doc/repotools/test.md, or try running ./runTests.py -h

'''
'''
echo "Parallel tests started..."
cp mpi/setup.cfg.mpi setup.cfg #stage setup.cfg
mv .coverage output/coverage.mpi
rm setup.cfg #unstage setup.cfg
echo "MPI Output written to coverage_tests_mpi.out"

cp output/coverage.serial .coverage.serial
cp output/coverage.mpi    .coverage.mpi
coverage combine
coverage report -m --include="*/pyGSTi/packages/pygsti/*" > output/coverage_tests.out 2>&1
echo "Combined Output written to coverage_tests.out"
'''

def run_mpi_tests(nproc=4, version=None):
    shutil.copy('mpi/setup.cfg.mpi', 'setup.cfg')

    mpicommands = ('time mpiexec -np %s python%s mpi/runtests.py -v ' % (str(nproc), '' if version is None else version)+
                   '--with-coverage --cover-package=pygsti --cover-erase mpi/testmpi*.py  ' +
                   '> ../output/coverage_tests_mpi.out 2>&1')

    with open('../output/mpi_output.txt', 'w') as output:
        returned = subprocess.call(mpicommands, shell=True, stdout=output, stderr=output)
    with open('../output/mpi_output.txt', 'r') as output:
        print(output.read())
    shutil.move('.coverage', '../output/mpi_coverage')
    os.remove('setup.cfg')
    return returned

def create_html(dirname):
    subprocess.call(['coverage', 'html', '--directory=%s' % dirname])

default   = ['tools', 'io', 'objects', 'construction', 'drivers', 'report', 'algorithms', 'optimize', 'mpi']
slowtests = ['report', 'drivers']

def run_tests(testnames, version=None, fast=False, changed=False, coverage=True,
              parallel=False, failed=False, cores=None, coverdir='../output/coverage', html=False,
              threshold=90, outputfile=None):

    with directory('test_packages'):

        # Don't run report or drivers
        if fast:
            for slowtest in slowtests:
                testnames.remove(slowtest)

        # Specify the versions of your test :)
        if version is None:
            # The version this file was run/imported with
            pythoncommands = ['python%s.%s' % (sys.version_info[0], sys.version_info[1])]
        else:
            # The version specified
            pythoncommands = ['python%s' % version]
        # Always use nose
        pythoncommands += ['-m', 'nose', '-v']

        # Since last commit to current branch
        if changed:
            testnames = [name for name in testnames if name in get_changed_packages()]

        if len(testnames) == 0:
            print('No tests to run')
            sys.exit(0)

        # testnames should be final at this point
        print('Running tests:\n%s' % ('\n'.join(testnames)))

        runmpi = 'mpi' in testnames # Run mpi tests differently
        if runmpi:
            testnames.remove('mpi')

        postcommands = []
        # Use parallelism native to nose
        if parallel:
            if cores is None:
                pythoncommands.append('--processes=-1')
                # (-1) will use all cores
            else:
                pythoncommands.append('--processes=%s' % cores)
            # Some tests take up to an hour
            pythoncommands.append('--process-timeout=14400') # Four hours
        else:
            # Use the failure monitoring native to nose
            postcommands = ['--with-id']
            if failed:
                postcommands = ['--failed']# ~implies --with-id

        if coverage:
            # html coverage is prettiest
            pythoncommands += ['--with-coverage',
                               '--cover-erase',
                               '--cover-package=pygsti',
                               '--cover-min-percentage=%s' % threshold]

        returned = 0
        if len(testnames) > 0:
            commands = pythoncommands + testnames + postcommands
            print(commands)

            if outputfile is None:
                returned = subprocess.call(commands)

            else:
                with open(outputfile, 'w') as testoutput:
                    returned = subprocess.call(commands, stdout=testoutput, stderr=testoutput)
                with open(outputfile, 'r') as testoutput:
                    print(testoutput.read())

        if parallel:
            #Only combine when run in parallel mode, since this
            # causes nose tests to create .coverage.<processid>
            # files instead of just a single .coverage file, which
            # "coverage combine" will overwrite with no-data (eek!).
            subprocess.call(['coverage', 'combine'])

        if runmpi:
            print('Running mpi')
            # Combine serial/parallel coverage
            shutil.copy2('.coverage', '../output/temp_coverage')
            run_mpi_tests(version=version)
            shutil.copy2('../output/temp_coverage', '.coverage.serial')
            shutil.copy2('../output/mpi_coverage', '.coverage.parallel')
            subprocess.call(['coverage', 'combine'])

        create_html(coverdir)

        sys.exit(returned)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run tests for pygsti')
    parser.add_argument('tests', nargs='*', default=default, type=str,
                        help='list of packages to run tests for')
    parser.add_argument('--version', '-v', type=str,
                        help='version of python to run the tests under')
    parser.add_argument('--changed', '-c', action='store_true', help='run only the changed packages')
    parser.add_argument('--fast', '-f', action='store_true',
                        help='run only the faster packages')
    parser.add_argument('--failed', action='store_true',
                        help='run last failed tests only')
    parser.add_argument('--html', action='store_true',
                        help='generate html')
    parser.add_argument('--parallel', '-p', action='store_true',
                        help='run tests in parallel')
    parser.add_argument('--cover', action='store_true',
                        help='skip coverage')
    parser.add_argument('--cores', type=int, default=None,
                        help='run tests with n cores')
    parser.add_argument('--coverdir', type=str, default='../output/coverage',
                        help='put html coverage report here')
    parser.add_argument('--threshold', type=int, default=90,
                        help='coverage percentage to beat')
    parser.add_argument('--output', type=str, default=None,
                        help='outputfile')

    parsed = parser.parse_args(sys.argv[1:])

    run_tests(parsed.tests, parsed.version, parsed.fast, parsed.changed, parsed.cover,
              parsed.parallel, parsed.failed, parsed.cores, parsed.coverdir,
              parsed.html, parsed.threshold, parsed.output)
