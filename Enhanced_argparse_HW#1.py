import argparse

if __name__ == '__main__':  # a necessary structure
  
  parser = argparse.ArgumentParser(description='Calculate the initial height with given time at free fall')
  parser.add_argument('-t','--time',type=int, help="the time that the ball needed to reach to the ground")
  # add an argument or input option to the user. They should enter "-t" with a number of time
  #    to tell the program what is the time.
  args = parser.parse_args()  #parse the input 
  
  height = 1/2 * 9.8 * args.time**2

  print("Your ball was at rest and was falling from",height,"meters above the gournd")
