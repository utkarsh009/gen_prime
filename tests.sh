#!/bin/sh
for a in test_cases/* ; do
python gen_prime.py < $a
done
[ $? -eq 0 ] && echo "Tests successfull!"
