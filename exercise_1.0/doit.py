#!/usr/bin/python
import os
import sys
import tarfile

n="M00002404"

outfile = open(n+"preOut",'w')
outfile.write(n + os.linesep)

tar = tarfile.open("pre-computed_geometries.tar.gz", "r:gz")
for member in tar.getmembers():
    if n in member.name:
        print("Found!");
        f = tar.extractfile(member)
        if f is not None:
            f.readline()
            for line in f.readlines():
                outfile.write(line)
                if('M  END' in line):
                    break

print("All done. Returning ")
