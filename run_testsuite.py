import sys
import nose


if __name__ == '__main__':
    argv = sys.argv[:]
    argv.extend(['--exclude=vendor', '--with-doctest', '--verbose'])
    nose.main(argv=argv)
