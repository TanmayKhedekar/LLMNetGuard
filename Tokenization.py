from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

# Initialize tokenizer
tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()

# Train tokenizer on the dataset
files = ["output.csv"]
trainer = BpeTrainer(special_tokens=["<unk>", "<pad>", "<s>", "</s>"])
tokenizer.train(files, trainer)

# Save tokenizer for reuse
tokenizer.save("pcap_tokenizer.json")
