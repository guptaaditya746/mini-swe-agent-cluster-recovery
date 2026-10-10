#!/bin/bash
#SBATCH --job-name=qwen_vllm
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err
#SBATCH --gres=gpu:ampere:1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=20:20:00

# Optional: Add your email for notifications
# #SBATCH --mail-type=BEGIN,END,FAIL
# #SBATCH --mail-user=your.email@example.com

echo "Starting vLLM SLURM job: $SLURM_JOB_ID"
echo "Assigned Node: $SLURM_JOB_NODELIST"

# 1. Load any required modules (if applicable on your cluster)
# module load cuda/11.8 

# 2. Activate your python environment 
# Assuming you are using conda/mamba based on your prompt "(query_to_kg)"
# source ~/.bashrc



# 3. Ensure we are in the correct directory
cd ~/thesis/thesis-kumar-gupta/experiments/query_to_kg/vllm
source ../.venv/bin/activate
# 4. Execute the launcher script
bash serve_qwen35_litellm.sh
