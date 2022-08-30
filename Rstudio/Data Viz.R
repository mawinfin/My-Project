getwd()

library(tidyverse)

##basc plots BASE R
hist(mtcars$mpg)
hist(mtcars$hp)
str(mtcars)

mtcars$am <- factor(mtcars$am,
                 labels = c("Auto","Manual"))
mtcars                

##BBar plot
barplot(table(mtcars$am))

## Box plot
boxplot(mtcars$hp)
fivenum(mtcars$hp)

boxplot(mpg ~ am,data = mtcars,
        col = c("gold", "salmon"))

## Scatter
plot(mtcars$hp,mtcars$mpg, pch =17)









