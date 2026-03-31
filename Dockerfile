# clean base image containing only comfyui, comfy-cli and comfyui-manager
FROM runpod/worker-comfyui:5.5.1-base

# install custom nodes into comfyui (first node with --mode remote to fetch updated cache)
RUN comfy node install --exit-on-fail sdvn_comfy_node@2.3.23 --mode remote

# download models into comfyui
RUN comfy model download --url https://huggingface.co/stabilityai/stable-cascade/resolve/main/text_encoder/model.safetensors --relative-path models/clip --filename model.safetensors
RUN comfy model download --url https://huggingface.co/lightx2v/Wan2.2-Lightning/resolve/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1/high_noise_model.safetensors --relative-path models/loras --filename Wan22-I2V-A14B-4steps-lora-rank64-Seko-V1-high.safetensors
RUN comfy model download --url https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/resolve/main/flux-2-klein-9b.safetensors --relative-path models/diffusion_models --filename Flux2-klein-9b.safetensors

# copy all input data (like images or videos) into comfyui (uncomment and adjust if needed)
# COPY input/ /comfyui/input/
