#! /usr/bin/env python

from __future__ import division
import sys, time, random, getopt

def progress(width, percent):
    print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent // 100 * '='), percent),
    if percent >= 100:
        print
        sys.stdout.flush()

def usage():
    sys.stderr.write("""USAGE: %s [options]
    simulation luoshen, then get two cards, check
    whether can get at least one peach
    options:
    -l, --loop=LOOP_NUMBER: do how many times test
    -s:                     skip luoshen
    -h, --help:             show the help message
""" % (sys.argv[0], ))
if __name__ == '__main__':
    loop = 100000
    skip = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "hl:s",
                                   ["help", "loop="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-l", "--loop"):
            try:
                loop = int(a)
            except ValueError:
                raise ValueError, "loop number must be a integer number, not %r" % a
        elif o in ("-s"):
            skip = True


    black_number = 52
    red_exclude_peach = 44
    peach_number = 8

    cards =[]

    # 'b' means black
    # 'r' means red but not peach
    # 'p' means peach
    for x in range(0, black_number):
        cards.extend('b')
    for x in range(0, red_exclude_peach):
        cards.extend('r')
    for x in range(0, peach_number):
        cards.extend('p')

    hit = 0
    last_percent = 0
    for i in range(0, loop):
        random.shuffle(cards)

        index = 0
        if (skip == False):
            # do luoshen
            for x in cards:
                if (x != 'b'):
                    break
                index += 1
            # skip the red card
            index += 1

        if (cards[index] == 'p' or cards[index+1] == 'p'):
            hit = hit + 1;

        percent = int((i + 1) * 100 / loop)
        if (percent > last_percent):
            last_percent = percent
            progress(50, percent)

    print "loop=%d hit=%d percent=%f" % (loop, hit, hit/loop)
