ARG PYTORCH="1.5"
ARG CUDA="10.1"
ARG CUDNN="7"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

# Fix expired NVIDIA CUDA repository and GPG keys
RUN rm -f /etc/apt/sources.list.d/cuda.list /etc/apt/sources.list.d/nvidia-ml.list \
    && apt-key del 7fa2af80 || true \
    && apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub || true

RUN apt-get update && apt-get install -y git libglib2.0-0 libsm6 libxrender-dev libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install mmfashion
RUN conda clean --all
RUN git clone --recursive https://github.com/open-mmlab/mmfashion.git /mmfashion
WORKDIR /mmfashion
ENV FORCE_CUDA="1"

# In PyTorch 1.5 image, torch is already pre-installed.
# Install dependencies with fixed versions to prevent pip resolver hang / OOM:
RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    scipy==1.5.4 \
    scikit-image==0.17.2 \
    scikit-learn==0.24.2 \
    matplotlib==3.3.4 \
    torchvision==0.6.0 \
    mmcv==0.5.9

RUN pip install --no-cache-dir --no-deps -e .
