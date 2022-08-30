##gg plot
library(tidyverse)
ggplot(data = mtcars, mapping = aes(x =hp, y = mpg)) + 
  geom_point() +
  geom_smooth() +
  geom_rug()

ggplot(mtcars,aes(hp,mpg)) + 
  geom_point(size = 3, col = "salmon", alpha = 0.5)

ggplot(mtcars,aes(hp)) +
  geom_histogram(bins = 10, fill = "blue", alpha = 0.5)

p <- ggplot(mtcars, aes(hp))
p + geom_density()
p + geom_boxplot()

##
diamonds %>%
  count(cut)

ggplot(diamonds,aes(cut,fill=color)) +
  geom_bar(position = "dodge")


small_di <- sample_n(diamonds, 5000)
ggplot(small_di, aes(carat, price)) +
  geom_point() +
  geom_smooth() +
  facet_wrap(~color, ncol=2) +
  theme_minimal() +
  labs(title = "Relation")

###final example
ggplot(small_di, aes(carat, price,col=color)) +
  geom_point() +
  facet_wrap(~cut, ncol=2) +
  theme_minimal() +
  labs(title = "Relation")

