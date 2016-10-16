This gym contains several games to warmup with when learning to use openai's gym.

#The Basics
To use one of these gyms to warmup, you must firs tinstall the openai gyms by running

```
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
```

If you have trouble with that, please visit [openai gym](https://github.com/openai/gym) for additional installation help.

```
git clone https://github.com/bb2b4n/gym-warmups.git
cd gym-warmups
pip install -e .
```

There are some examples of how warmup in the notebooks directory.

# The Gyms
## Pancakes
This is an environment for the openai gym. The problem requires that we sort a stack of P pancakes. The P pancakes are all different sizes. The only tool available is a spatula that can be inserted between any pancake and another pancake or the plate. There is a more detailed tutorial in the notebooks directory.

```
import gym
import gym_warmups
env = gym.make('Pancakes-Grandmaster-v0')
env.reset()
env.render()
```

Copyright © 2016 Back 2 Basics Gym. All Rights Reserved.
