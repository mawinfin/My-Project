##Project - Rock Scissors Paper GAME
play <- function() {
  message("Welcome to the game write your name and let fun!!")
  #name <- readline("Name: ")
  r="rock"
  s="scissior"
  p="paper"
  game <- c(r,s,p)
  w <- 0
  l <- 0
  t <- 0
  R <- 0
  while(TRUE) {
    R <- R+1
    message("Choose your hand rock, paepr, scissior")
    cat("Round",R,"\n")
    user <- readline("Hand :")
    com  <- sample(game,1)
    if (user == r & com == s) {
      print("You win!!")
      w <- w+1
    } else if  (user == s & com == p) {
      print("You win!!")
      w <- w+1
    } else if  (user == p & com == r) {
      print("You win!!")
      w <- w+1
    } else if  (user == com) {
      print("Tie!! play again")
      t <- t+1
    } else if  (user == "stop") {
      print("Score")
      cat("win:",w,
          "lose:",l,
          "tie:",t)
      break
    } else {
      print("You lose!!")
      l <- l+1
    }
    message("Result")
    cat("PC Hand: ",com,"\n")
    cat("Your Hand: ", user,"\n")
  }
}
