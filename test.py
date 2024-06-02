import gym
import numpy as np

env = gym.make('FrozenLake-v1',is_slippery=False)

q_table=np.zeros((env.observation_space.n,env.action_space.n))

learning_rate=0.1
epsilon=1
discount_factor=1

episodes=10000
success_count=0

UP, RIGHT, DOWN, LEFT=0, 1, 2, 3

holes=[5,7,11,12]
destination=15
def reset():
  return 0

def chose_random_action():
  return np.random.randint(0,4)

reward_normal=0
reward_destination=1
def move(state, action):
  #returns next state
  reward=reward_normal
  done=False
  if action==UP:
    if state>3:
      state-=4
  elif action==RIGHT:
    if state%4<3:
      state+=1
  elif action==DOWN:
    if state<12:
      state+=4
  elif action==LEFT:
    if state%4>0:
      state-=1

  for hole in holes:
    if state==hole:
      done=True
  if state==destination:
    done=True
    reward=reward_destination
  return state,reward, done

for episode in range(episodes):
  state = reset()
  done=False
  if episode%100==0:
    print("success rate for the last 100:",success_count)
    success_count=0
  while not done:
    if epsilon>np.random.uniform(0,1):
      action=chose_random_action()
    else:
      action=np.argmax(q_table[state])

    next_state, reward, done= move(state, action)#change this

    old_value = q_table[state, action]
    next_max = np.max(q_table[next_state])
    new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
    q_table[state, action] = new_value
    if done:
      if reward == 1:
        success_count += 1

    state = next_state

  if epsilon > 0.01:
    epsilon -= 0.001