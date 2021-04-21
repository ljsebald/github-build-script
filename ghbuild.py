#!/usr/bin/env python2.7
#   GitHub Kernel Build Script
#   Copyright (C) 2016-2021 Lawrence Sebald
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License version 3
#   as published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import sys
import getopt
import re
import subprocess as sp
import os
from operator import itemgetter

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:o:p:l:")
    except:
        print "Missing arguments!"
        sys.exit(2)

    fn = None
    op = None
    p = None
    ld = None

    for o, a in opts:
        if o == '-f':
            fn = a
        elif o == '-o':
            op = a
        elif o == '-p':
            p = a
        elif o == "-l":
            ld = a
        else:
            assert False, "Unknown argument"

    if fn == None or op == None or p == None:
        assert False, "Missing arguments"

    fp = None
    js = None
    try:
        fp = open(fn)
        js = json.load(fp)
    except:
        print "Invalid filename: " + fn
        sys.exit(2)

    r = re.compile(p)

    if op == "print":
        do_print(js, r)
    elif op == "addremotes":
        do_addremotes(js, r)
    elif op == "build":
        do_build(j, r, ld)
    else:
        print "Invalid Operation: " + op
        sys.exit(2)

def do_print(js, r):
    for o in js:
        if r.search(o["name"]):
            print o["name"]

def do_addremotes(js, r):
    for o in js:
        if r.search(o["name"]):
            print "Adding " + o["ssh_url"] + " as " + o["name"]
            sp.call(["git", "remote", "add", o["name"], o["ssh_url"]])
            sp.call(["git", "fetch", o["name"]])

def do_build(js, r, ld):
    mfn = os.path.join(ld, "master.log")
    mfp = open(mfn, "w")

    for o in js:
        if r.search(o["name"]):
            print "Building " + o["name"]
            lf = os.path.join(ld, o["name"] + "-build.log")
            lfp = open(lf, "w")
            rv = sp.call(["git", "checkout", o["name"] + "/master"], stdout=lfp, stderr=lfp)
            if rv != 0:
                print "Checkout failed, attempting recovery"
                mfp.write(o["name"] + " failed checkout!\n")
                rv = sp.call(["git", "reset", "--hard"], stdout=lfp, stderr=lfp)
                rv = sp.call(["git", "checkout", o["name"] + "/master"], stdout=lfp, stderr=lfp)
            if rv != 0:
                print "CHECKOUT FAILED, NOT RECOVERABLE!"
                print "ALL FURTHER BUILDS MAY BE SUSPECT!"
                mfp.write(o["name"] + " requires manual build!\n")
                continue

            rv = sp.call(["make", "-j6", "bindeb-pkg"], stdout=lfp, stderr=lfp)
            if rv != 0:
                print "BUILD FAILED"
                mfp.write(o["name"] + " FAILED\n")
            else:
                print "BUILD SUCCEEDED"
                mfp.write(o["name"] + " succeeded\n")
            lfp.close()
            mfp.flush()
    mfp.close()


if __name__ == "__main__":
    main()
