import pickle
import json
import numpy as np

if __name__ == "__main__":
    with open('vectordb.pkl', 'rb') as f:  # open a text file
        items = pickle.load(f)  # deserialize using load()
        for key in items:
            print("Processing ", key)
            with open(f'vectordb-{key}.json', 'w') as data:
                if key == "embeds":
                    embeds_array = np.array(items[key])
                    print("Embeddings Shape - ", embeds_array.shape)
                    print("Embeddings Type - ", embeds_array.dtype)
                    data.write(json.dumps(embeds_array.tolist()))
                else:
                    data.write(json.dumps(items[key]))
