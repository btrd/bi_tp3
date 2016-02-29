import numpy as np

class Cluster():
  def __init__(self, name):
    self.observations = []
    self.centroid = []
    self.name = name

  def addObservation(self, observation):
    self.observations.append(observation)

  def updateCentroid(self):
    obs_np = np.array(self.observations)
    obs_np = obs_np.astype(np.float)
    self.centroid = obs_np.mean(axis=0).tolist()

  def deleteObservation(self, obs):
    self.observations.remove(obs)

  def equals(self, other):
    return (self.observations == other.observations) and (self.centroid == other.centroid)
