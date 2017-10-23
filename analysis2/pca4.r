#!/usr/bin/Rscript
d=read.table('clean.out')
#x=d[,c(16:27,168:179)]
#x=d[,c(16:27)]
x=d[,c(1:158)]


res=prcomp(x,scale=T)

# percent var
res$sdev**2/sum(res$sdev**2)

# scores plot
#plot(res$x[,1],res$x[,2])

write.table(res$x[,1:10],'pcout4',col.name=F,row.name=F,sep='\t')


