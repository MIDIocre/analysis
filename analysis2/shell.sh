(cat ../filenames; ls ../../othermusic/*/* | sed 's/\//\t/g' | awk '{FS="\t"; print $5}') > filenames
ls ../../othermusic/*/* | sed 's/\//\t/g' | awk '{FS="\t"; print $5}' | sort | uniq -c | sort -gk1 | awk '{if ($1>1) print $2}' > duplicated
(cat filenames; cat duplicated ) | sort | uniq -c | awk '{if ($1==1) print $2}' > single_filename





ls midis/ | while read x; do echo "echo -ne \"$x\\t\"; midicsv midis/\"$x\" | grep Note_ | sort -nk2 | sed 's/, /\t/g' | ./list5.py | tail -1"; done | parallel -k > sumout
grep -vP "\t"nan sumout | awk '{FS="\t"; OFS="\t"; if (NF=158) print}' > clean.out
awk '{FS="\t"; if ($3~"[a-z]") print}' clean.out  | less -S
# manual clean
awk '{FS="\t"; if (NF==158) print}' clean.out > t
mv t clean.out 

cut -f3-26 clean.out | ./pca.r > res.binmod
cut -f27-154 clean.out | ./pca.r > res.notes
cut -f155-158 clean.out | ./pca.r > res.durhigh
cut -f3- clean.out | ./pca.r > res.all


(awk '{print $1"\t"$3"\tclassical"}' dic_ordered4.clean; ls ../../othermusic/ | while read x; do ls ../../othermusic/$x/ | while read y; do echo -e "$y\t$x\t$x"; done;done) > dic

#---checking for file name correspondance...
cut -f1 clean.out | while read x; do (echo -ne "$x\t"; grep -F "$x" dic | tr '\n' '\t'; echo ""); done | awk -F'\t' '{print NF"\t"$0}' > dictmp
#edit manually --- finaldic


