#!/bin/bash

ls midis/ | while read x; do echo "echo -ne \"$x\\t\"; midicsv midis/\"$x\" | grep Note_ | sort -nk2 | sed 's/, /\t/g' | ./list6.py | tail -1"; done | parallel -k > sumout

# just an estimate of how long processing ....
for i in {1..20}; do date +'%s' | tr '\n' '\t'; wc -l sumout; sleep 5; done > timing  # calculated as about 30 min for all files

grep -vP "\t"nan sumout | awk -F '\t' '{OFS="\t"; if (NF==170) print}' | awk -F '\t' '{if (!($3~"[a-z]")) print}' > clean.out # clean unclear things up as much as possible

# check correctness
cat clean.out | awk -F '\t' '{print NF}' | uniq
cut -f2 clean.out | uniq

# check dictionary correctness
awk -F'\t' '{print NF}' dic | uniq

# get the correct file names and author correspondance
cut -f1 clean.out | while read x; do echo -ne "$x\t"; grep -F "$x" dic | tr '\n' '@' | sed 's/@$//g'; echo ""; done > names.out

# manually check lines with "@"
awk -F'\t' '{if (NF!=4) print}' names.out   # clearly, special characters are messing around with a lot of things
awk -F'\t' '{if (NF!=4) print}' names.out | sed 's/[ÅîäÑçó ]/#/g' | grep -v "#" # this does not work consistently. These stupid special charaters just has to be done manually
# end manual part

(cat head; paste names.out clean.out) > SUMMARY.out
awk -F'\t' '{ print NF}' SUMMARY.out | uniq # final check


