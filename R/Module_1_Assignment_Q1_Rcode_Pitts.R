

mydata <- read.csv("week1.csv")

print(mydata)
str(mydata)

data_subset<-mydata[c(2,4,6,8)]
print(data_subset)

write.csv(data_subset, "data_subset.csv")
