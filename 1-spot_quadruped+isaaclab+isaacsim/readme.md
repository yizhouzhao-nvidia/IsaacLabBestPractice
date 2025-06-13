# Training a Spot Quadruped robot: IsaacLab (train) + IsaacSim (deploy)

![robot](./imgs/robot.png)

## 0. Motivation

This tutorial demonstrates a novel approach to reinforcement learning workflows that addresses the inherent differences between training and testing phases. In current IsaacLab reinforcement learning pipelines, training and testing are often treated similarly, which can lead to several challenges:

1. **Training vs Testing Objectives**: During training, we prioritize efficiency and simplicity to accelerate learning. However, testing requires comprehensive evaluation across diverse scenarios and edge cases.

2. **Team Collaboration**: The current IsaacLab workflows often combine training and testing into a single process, which can hinder effective collaboration between different teams (e.g., simulation engineers, ML researchers, and testing engineers).

3. **Flexibility and Extensibility**: A rigid workflow makes it difficult to adapt to new requirements or incorporate different testing scenarios without modifying the core training pipeline.

This tutorial introduces a "double-blinded" approach that:
- Separates the concerns of 3D scene creation, training, and testing
- Enables different teams to work independently on their respective components
- Provides a flexible and extensible framework for both training and testing
- Maintains the integrity of the testing process by keeping it independent from the training pipeline

By decoupling these components, we create a more robust and maintainable workflow that better reflects real-world deployment scenarios while facilitating better team collaboration.

## 1. Training [IsaacLab]

Follow this tutorial to [train a Spot Quadruped Robot](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/03_envs/run_rl_training.html)

```bash
# execute from the root directory of the repository
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task Isaac-Velocity-Flat-Spot-v0 --num_envs 4096 --headless --video --enable_cameras
```

Under root directory of IsaacLab, you can see the trained nn policy under `logs/rsl_rl/spot_flat/<data_time>/model_*.pt`


Play the trained policy
```bash
# execute from the root directory of the repository
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py --task Isaac-Velocity-Flat-Spot-v0 --num_envs 32 --use_pretrained_checkpoint
```


## 3. View in Isaac Sim

