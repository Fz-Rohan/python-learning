sequence = "ATGCGATACGCTTGA"
gc_count = sequence.count("G") + sequence.count("C")
gc_percent = (gc_count / len(sequence)) * 100
print(f"Sequence length: {len(sequence)} bp")
print(f"GC Content: {gc_percent:.2f}%")