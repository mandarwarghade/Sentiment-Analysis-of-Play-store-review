import transformers

DEVICE = "cuda"
MAX_LEN=512
TRAIN_BATCH_SIZE=4
VALID_BACTH_SIZE=4
EPOCHS=10
MODEL_PATH="model.bin"
TRINING_FILE="C:/Users/Mandar Warghade/Desktop/bert/IMDB.csv"
TOKENIZER=transformers.BertTokenizer.from_pretrained("bert-base-uncased")
