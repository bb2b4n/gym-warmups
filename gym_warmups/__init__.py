from gym.envs.registration import register

levels = ["Newbie", "Novice", "Rookie", "Beginner", "Talented", "Skilled", "Intermediate", "Skillful", "Seasoned", "Proficient", "Experienced", "Advanced", "Senior", "Expert", "Master", "Grandmaster"]

for i,level in enumerate(levels):
  register(
      id='Pancakes-%s-v0'%level,
      entry_point='gym_warmups.envs:PancakesEnv',
      kwargs={'pancakes': 4*(i+1)},
      timestep_limit=20000,
  )
