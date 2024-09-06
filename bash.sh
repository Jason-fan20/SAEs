python3 -V


mkdir /workspace
cp /content/drive/MyDrive/Interpretability/1L-Sparse-Autoencoder -r /workspace/1L-Sparse-Autoencoder 
cd /workspace/1L-Sparse-Autoencoder 
fuser -v /dev/nvidia*

pip install transformer_lens
pip install gradio
chmod /content/drive/MyDrive/Interpretability/azcopy
mkdir /content/data
# /content/drive/MyDrive/Interpretability/azcopy copy 'https://biglmdiag.blob.core.windows.net/vinvl/datasets/coco_caption' /content/data --recursive
# /content/drive/MyDrive/Interpretability/azcopy copy 'https://biglmdiag.blob.core.windows.net/vinvl/datasets/nocaps' /content/data --recursive