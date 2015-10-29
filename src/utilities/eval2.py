#-*- coding: utf-8 -*-
import sys
import os
import subprocess

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'USAGE: python eval2.py <input dir> <output dir>'
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        s = ['python', 'laf2tab.py', input_dir, '%s/%s' % (output_dir, '1.tab')]
        print s
        subprocess.call(s)
        s = ['python', 'segment2document.py', '%s/%s' % (output_dir, '1.tab'), '%s/%s' % (output_dir, '2.tab')]
        print s
        subprocess.call(s)
