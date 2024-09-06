from datasets import load_dataset
# data = load_dataset("NeelNanda/c4-code-20k", split="train")
# NoCaps_data = load_dataset("sentence-transformers/coco-captions", split="train")
NoCaps_data = load_dataset("HuggingFaceM4/NoCaps", split="all")
Load_Data = 'Nocaps'
if(Load_Data == 'Nocaps'):
    caption_all = []
    for caption_list in NoCaps_data['annotations_captions']:
        if (len(caption_list)!=0):
            caption_all.append('\n'.join(caption_list))
        else:
            print('detect zero list')
            break
        from datasets import Dataset
    data = Dataset.from_dict({"text": caption_all})
    from transformer_lens import HookedTransformer, utils
    # tokenized_data = utils.tokenize_and_concatenate(data, model.tokenizer, max_length=128)
count = 0
caption_list = []
for caption in caption_all:
    # print(caption)
    if ('red panda' in caption):
        caption  = caption.replace('\n','')
        print(caption)
        break
    # if ('red panda' in caption):
    #     count = count + 1
    #     if(count >5):
    #         print(count)
    #         print(''.join(caption_list))
    #         break
    #     else:
    #         caption_list.append(caption)
        
# A red panda is on the grass and under a branch.
# A red panda is on the grass and under a branch.A red panda is walking among some trees outside.A red panda scampers across rocky terrain under a fallen tree branch. A red panda running across shrubs and trees. A red panda is walking next to rocks and a tree.Brown and black fox raccoon running through a wooded areaThe red panda is walking through the grass and rocks near the trees.A fox running on the grass around trees A red panda walks through the grass near some trees. A red panda is on the ground with short green plants, rocks, and tree trunks around it, and a tree branch above it.
import pdb
pdb.set_trace()
