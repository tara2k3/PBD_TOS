### R Calculator
# Set variable test_mode to TRUE in order to test the functions.
# 
#
###
test_mode = TRUE
#test_mode = FALSE

functions.factorial <- function(x) {
  if (x <= 1)
    return(1)
  else
    return(x * functions.factorial(x - 1))
}

functions.add <- function (a, b) {
  return(a + b)
}

functions.substract <- function (a, b) {
  return (a - b)
}

functions.multiply <- function(a, b) {
  return (a * b)
}

functions.divide <- function(a, b) {
  return (a / b)
}

functions.exponent <- function(x, y) {
  return (x ^ y)
}

functions.sqrt <- function(x) {
  return (x ^ 0.5)
}

functions.squared <- function(x) {
  return (x ^ 2)
}

functions.cubed <- function(x) {
  return (x ^ 3)
}

functions.sin <- function(x) {
  return(sin(x))
}

functions.cos <- function(x) {
  return(cos(x))
}

functions.tan <- function (x) {
  retun(tan(x))
}

read_one_number <- function () {
  input <- readline("Enter first number : ")
  value <- as.numeric(input)
  return(value)
}

read_two_numbers <- function () {
  input <- readline("Enter first number : ")
  value1 <- as.numeric(input)
  input <- readline("Enter second number : ")
  value2 <- as.numeric(input)
  return(c(value1, value2))
}

if (test_mode == FALSE) {
  print("Hello, welcome to the super R calculator.")
  print(" 1 - Add")
  print(" 2 - Substract")
  print("	3 - Multiply")
  print("	4 - Division")
  print("	5 - Expo")
  print("	6 - Squareroot")
  print("	7 - Sin")
  print("	8 - Tan")
  print("	9 - Cos")
  
  choice = readline("Enter choice (1/2/3/4/5/6/7/8/9) : ")
  
  if (choice == "1") {
    numbers = read_two_numbers()
    
    cat(" the sum of ",
        numbers[1],
        " and ",
        numbers[2],
        " is ",
        functions.add(numbers[1], numbers[2]))
  } else if (choice == "2") {
    numbers = read_two_numbers()
    
    cat(
      " the substraction of ",
      numbers[1],
      " and ",
      numbers[2],
      " is ",
      functions.substract(numbers[1], numbers[2])
    )
  } else if (choice == "3") {
    numbers = read_two_numbers()
    
    cat(
      " the multiplication of ",
      numbers[1],
      " by ",
      numbers[2],
      " is ",
      functions.multiply(numbers[1], numbers[2])
    )
  } else if (choice == "4") {
    numbers = read_two_numbers()
    
    cat(
      " the division of ",
      numbers[1],
      " by ",
      numbers[2],
      " is ",
      functions.divide(numbers[1], numbers[2])
    )
  } else if (choice == "5") {
    numbers = read_two_numbers()
    
    cat(
      " the exponent of ",
      numbers[1],
      " to ",
      numbers[2],
      " is ",
      functions.exponent(numbers[1], numbers[2])
    )
  } else if (choice == "6") {
    number = read_one_number()
    
    cat(" the square root of ", number, " is ", functions.sqrt(number))
  } else if (choice == "7") {
    number = read_one_number()
    
    cat(" the sine of ", number, " is ", functions.sin(number))
  } else if (choice == "8") {
    number = read_one_number()
    
    cat(" the tangent of ", number, " is ", functions.tan(number))
  } else if (choice == "9") {
    number = read_one_number()
    
    cat("the cosine of ", number, " is ", functions.cos(number))
  } else {
    print("Adahh!!, You entered an invalid option.")
  }
  
} else {
  assertEqual <- function(a,b) {
    if (a != b)
      cat("ERROR: Expected", a, " value ", b)
  }
  
  assertEqual( 2 , functions.add(1,1))
  assertEqual( 2 , functions.substract(3,1))
  assertEqual( 49 , functions.multiply(7,7))
  assertEqual( 49 , functions.squared(7))
  assertEqual( 7 , functions.sqrt(49))
}

