# My-Gym: an implementation of sparse rewards environements

This code is used by the Diffusion-Based Approximate Value Function [implementation](https://github.com/mklissa/DAVF).
To install the available environments, simply proceed with:

```python
pip install -e .
```

To use the available environments in your code, you need to write these lines:

```python
import gym
import my-gym

env = gym.make("SparseMountainCar-v0")
```
