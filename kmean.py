import sys
from kMeanClusterer import KMeanClusterer

# Iris:     python kmean.py 3 iris.csv 4
# Square:   python kmean.py 4 square.csv
# Titanic:  python kmean.py 4 titanic.csv 0
if __name__ == "__main__":
  if len(sys.argv) == 3:
    kMeanClusterer = KMeanClusterer(int(sys.argv[1]), sys.argv[2], -1)
  elif len(sys.argv) == 4:
    kMeanClusterer = KMeanClusterer(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
  else:
    sys.exit("Usage: python kmean.py <nb_cluster> <input_file> <optional: num_column>")

  print("BC:\t" + str(kMeanClusterer.bc()))
  print("WC:\t" + str(kMeanClusterer.wc()))
  print("WC/BC: \t" + str(kMeanClusterer.bc()/kMeanClusterer.wc()))
  kMeanClusterer.check_class()
