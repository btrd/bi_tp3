import sys
from kMeanClusterer import KMeanClusterer

if __name__ == "__main__":
  if len(sys.argv) == 3:
    kMeanClusterer = KMeanClusterer(int(sys.argv[1]), sys.argv[2])
    print("BC:\t" + str(kMeanClusterer.bc()))
    print("WC:\t" + str(kMeanClusterer.wc()))
    print("WC/BC: \t" + str(kMeanClusterer.bc()/kMeanClusterer.wc()))

  else:
    print("Usage: kmean.py <nb_cluster> <input_file>")
  