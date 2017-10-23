
ls allmid/  > filenames

cat filenames | while read x; do echo -ne "$x\t"; grep "^$x" dic; done > dic_ordered


