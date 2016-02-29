from kMeanClusterer import KMeanClusterer

if __name__ == "__main__":
  k = 3
  datafile = "iris.csv"

  kMeanClusterer = KMeanClusterer(k, datafile)
  