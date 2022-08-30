##install packages
install.packages("dplyr")

#load packages
library(dplyr)

## read csv file
imdb <- read.csv("imdb.csv", stringsAsFactors = FALSE)
View(imdb)

glimpse(imdb)
head(imdb,10)
tail(imdb,10)

select(imdb,MOVIE_NAME,RATING)
select(imdb,1,5)
imdb %>% head(10)
imdb %>% 
  select(name = MOVIE_NAME,release_year = YEAR) %>%
  head(10) %>%
  View()

