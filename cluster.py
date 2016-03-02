import numpy as np

class Cluster():
  def __init__(self, col_class):
    self.observations = []
    self.centroid = []
    self.col_class = col_class

  def addObservation(self, observation):
    self.observations.append(observation)

  def updateCentroid(self):
    obs_np = np.array(self.observations)
    if self.col_class:
      obs_np = np.delete(obs_np, self.col_class, 1)
    obs_np = obs_np.astype(np.float)
    self.centroid = obs_np.mean(axis=0).tolist()

  def deleteObservation(self, obs):
    self.observations.remove(obs)

  def equals(self, other):
    return (self.observations == other.observations) and (self.centroid == other.centroid)
