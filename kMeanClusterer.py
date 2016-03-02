import random
import math
import csv
import numpy as np
from cluster import Cluster

class KMeanClusterer():

  def __init__(self, k, datafile, num_class):
    self.clusterNumber = k
    self.clusters = []
    self.datafile = datafile
    self.observations = []
    self.min = []
    self.max = []
    self.col_class = num_class
    self.initialization()

    while self.assignement():
      for c in self.clusters:
        c.updateCentroid()

  def initialization(self):
    for x in xrange(0, self.clusterNumber):
      c = Cluster(self.col_class)
      self.clusters.append(c)

    iris_data_matrix = self.load_csv(self.datafile)

    # add each obs in a random cluster
    i = 0
    for iris in iris_data_matrix:
      i = (i + 1) % self.clusterNumber
      self.clusters[i].addObservation(iris)
      self.observations.append(iris)


    obs_np = np.array(self.observations)
    if self.col_class:
      obs_np = np.delete(obs_np, self.col_class, 1)
    obs_np = obs_np.astype(np.float)
    self.min = obs_np.min(axis=0).tolist()
    self.max = obs_np.max(axis=0).tolist()

    for c in self.clusters:
      c.updateCentroid()

  def load_csv(self, dataFile):
    data_matrix = []
     
    data = open(dataFile,'r')
    reader = csv.reader(data)
    for row in reader:
        data_matrix.append(row)
    return data_matrix

  def assignement(self):
    res = False
    for cluster in self.clusters:
      for obs in cluster.observations:
        nearestCluster = self.nearestCluster(obs)
        if not nearestCluster.equals(cluster):
          nearestCluster.addObservation(obs)
          cluster.deleteObservation(obs)
          res = True
    return res

  def nearestCluster(self, obs):
    res = self.clusters[0]
    dist = self.computeDistance(obs, res.centroid)
    for cluster in self.clusters:
      nDist = self.computeDistance(obs, cluster.centroid)
      if nDist < dist:
        dist = nDist
        res = cluster
    return res

  def computeDistance(self, obs, centroid):
    obs = np.array(obs)
    if self.col_class and self.col_class < len(obs):
      obs = np.delete(obs, self.col_class)
    obs = obs.astype(np.float)

    centroid = np.array(centroid)
    centroid = centroid.astype(np.float)
    
    res = 0
    for i in xrange(0, obs.size):
      res += ((obs[i] - centroid[i]) ** 2) / (self.max[i] - self.min[i])

    return math.sqrt(res)

  def wc(self):
    res = 0
    for cluster in self.clusters:
      for obs in cluster.observations:
        res += self.computeDistance(obs, cluster.centroid)
    return res

  def bc(self):
    res = 0
    for cluster1 in self.clusters:
      for cluster2 in self.clusters:
        res += self.computeDistance(cluster1.centroid, cluster2.centroid)
    return res

  def check_class(self):
    if self.col_class:
      observations = np.array(self.observations)
      class_names = observations[:,self.col_class]
      class_names = np.unique(class_names)
      print(class_names)

      j = 0
      for cluster in self.clusters:
        count_class = [0] * len(class_names)
        for obs in cluster.observations:
          for i in xrange(0,len(class_names)):
            if obs[self.col_class] == class_names[i]:
              count_class[i] += 1
        print("Cluster " + str(j) + " : " + str(count_class))
        j += 1
