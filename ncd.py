#!/usr/bin/python
# -*- coding: utf-8 -*-

import snappy
import bz2
import zlib


class NormalizedCompressionDistance(object):

    def __init__(self, compressor):
        self.compressor = compressor
    
    def ncd(self, a, b):
        compressed_a = self.compressor.compress(a)
        compressed_b = self.compressor.compress(b)
        return (float(len(self.compressor.compress(a + b)) - len(min(compressed_a, compressed_b)))) / float(len(max(compressed_a,
                                                                                                         compressed_b)))

s1= "the waiter was not eager"
s2 = 'computer graphic memory'
s3 = 'hardware computer engineer'
s4 = 'the service was bad'

n = NormalizedCompressionDistance(snappy)

print 'lesser, the better =====>'
print
print n.ncd(s1,s2)
print n.ncd(s1,s3)
print n.ncd(s1,s4)
print n.ncd(s2,s3)
print n.ncd(s2,s4)
print n.ncd(s3,s4)
