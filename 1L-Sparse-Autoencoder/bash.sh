python train.py
# mkdir /workspace/checkpoints
# pip install kaleido
# cp /workspace/1L-Sparse-Autoencoder/. -r /content/drive/MyDrive/Interpretability/1L-Sparse-Autoencoder
fuser -k /dev/nvidia*
rsync -av --exclude='checkpoints' /workspace/1L-Sparse-Autoencoder/ /content/drive/MyDrive/Interpretability/1L-Sparse-Autoencoder
# rsync -av /workspace/1L-Sparse-Autoencoder/ /content/drive/MyDrive/Interpretability/1L-Sparse-Autoencoder