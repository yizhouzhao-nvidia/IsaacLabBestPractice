# Isaac Lab Best Practice

## Fast Isaac Lab/Isaac Sim installation

1. Install [Astral UV](https://docs.astral.sh/uv/getting-started/installation/)

2. Follow the [Isaac Lab Install Instructions](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)
```bash
uv venv env_isaaclab --python=3.10
source env_isaaclab/bin/activate
```

Install torch
```bash
uv pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121
```

```bash
pip install --upgrade pip
pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com
```

The Isaac Sim should be install at: `env_isaaclab/lib/python3.10/site-packages/isaacsim`

```bash
isaacsim
```

Install Isaac Lab
```bash
sudo apt install cmake build-essential
git clone git@github.com:isaac-sim/IsaacLab.git
cd Isaac Lab
./isaaclab.sh --install # or "./isaaclab.sh -i"
```