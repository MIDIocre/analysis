#!/usr/bin/Rscript
input=file('stdin')
d=read.table(input)

library('MASS')
res=lda(d[,1]~.,data=d[,2:ncol(d)])

# percent var
write.table(t(res$sdev**2/sum(res$sdev**2)),'',col.name=F,row.name=F,sep='\t')

# scores plot
#plot(res$x[,1],res$x[,2])

write.table(res$x[,1:10],"",col.name=F,row.name=F,sep='\t')


