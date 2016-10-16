import gym,sys
from gym import error, spaces, utils
from gym.utils import seeding
from gym import spaces
import numpy as np
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class PancakesEnv(gym.Env):
  metadata = {'render.modes': ['human', 'ansi', 'rgb_array']}

  def __init__(this, pancakes=10):
    this.number_of_pancakes=pancakes
    this._seed()
    this._reset();

  def _step(this, action):
    # perform the flip action.
    if action >-1 and action < this.number_of_pancakes:
      start = action
      end = this.number_of_pancakes-1
      while start < end:
        t=this.pancakes[start];
        this.pancakes[start] = this.pancakes[end];
        this.pancakes[end] = t;
        start+=1;
        end-=1;
    current_reward = this._calc_reward();

    return (this.pancakes,       # Currently observable pancake stack
            current_reward,      # Reward for current stack
            current_reward == 0, # Completion is marked by sorted stack
            {})

  # reward is negative, 0 reward is when pancake is completely sorted.
  def _calc_reward(this):
    reward = 0;
    for i in range(this.number_of_pancakes):
      reward += abs(this.pancakes[i] - (this.number_of_pancakes - i - 1));
    return reward;
      
  ## The pancake is stored in an array plate first.
  def _reset(this):
    this.action_space=spaces.Discrete(this.number_of_pancakes) # flip starting and including this pancake high
    this.observation_space=spaces.Tuple(spaces.Discrete(this.number_of_pancakes) for _ in range(this.number_of_pancakes))
    this.pancakes=[i for i in range(this.number_of_pancakes)]
    this.reward_range = (this._calc_reward(), 0)
    np.random.shuffle(this.pancakes)

  def _render(this, mode='human', close=False):
    width = 2*this.number_of_pancakes + 1;
    if mode=='rgb_array':
      arr = []
      for p in reversed(this.pancakes):
        arr.append([ [float(p)/this.number_of_pancakes,1.-p/this.number_of_pancakes,1.] if c == 'p' else [0,0,0] for c in str.center('p'*(2*p+1),width)])
      return arr
    else:
      outfile = StringIO() if mode == 'ansi' else sys.stdout
      for p in reversed(this.pancakes):
        outfile.write(str.center('p'*(2*p+1),width));
        outfile.write('\n');

      return outfile

  def _seed(self, seed=None):
      self.np_random, seed = seeding.np_random(seed)
      return [seed]

