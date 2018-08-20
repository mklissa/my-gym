# My-Gym: an implementation of sparse rewards environements

This code is used by the Diffusion-Based Approximate Value Function [implementation](https://github.com/mklissa/DAVF).
To install the available environments, simply proceed with:

```python
pip install -e .
```

You will also need to install the mujoco-py binaries and license key, as indicated [here](https://github.com/openai/mujoco-py/tree/0.5). To use the available environments in your code, you need to write these lines:

```python
import gym
import my-gym

env = gym.make("SparseMountainCar-v0")
```
