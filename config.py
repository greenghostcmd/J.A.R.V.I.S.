class GPTConfig:
    # configs for the gpt model
    block_size: int = 256  # context length
    vocab_size: int = 65  # 26 lowercase  26 uppercase 10 digits newline and space
    n_embd: int = 384
    n_head: int = 6
    n_layer: int = 6
    dropout: float = 0.2
    bias: bool = True  # bias in layernorm and linear layers
