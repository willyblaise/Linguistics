
cardata <- read.csv("cars.csv")

cardata_clean <- na.omit(cardata)
print(cardata_clean)

summary(cardata_clean)

cardata_cleanSD<-cardata_clean[c("mpg","hp","wt")]
print(cardata_cleanSD)
sapply(cardata_cleanSD, sd)
sapply(cardata_cleanSD, sum)

hp_wt_ratio <- c(cardata_clean$hp / cardata_clean$wt)
cardata_clean <- cbind(cardata_clean, hp_wt_ratio)
head(cardata_clean)
plot(cardata_clean$wt, cardata_clean$mpg, pch=19, col="blue", xlab="weight", ylab="MPG", ylim = c(0, 35), frame.plot = FALSE)
