# -*- coding: utf8 -*-
from .subfinder_thread import SubFinderThread as SubFinder
from .run import run

if __name__ == '__main__':
    run(SubFinder)