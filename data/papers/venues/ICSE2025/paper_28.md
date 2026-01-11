# Neurosymbolic Modular Refinement Type Inference

**Authors**: Sakkas, Georgios and Sahu, Pratyush and Ong, Kyeling and Jhala, Ranjit

**Abstract**:

Refinement types, a type-based generalization of Floyd-Hoare logics, are an expressive and modular means of statically ensuring a wide variety of correctness, safety, and security properties of software. However, their expressiveness and modularity means that to use them, a developer must laboriously annotate all the functions in their code with potentially complex type specifications that specify the contract for that function. We present LHC, a neurosymbolic agent that uses LLMs to automatically generate refinement type annotations for all the functions in an entire package or module, using the refinement type checker LiquidHaskell as an oracle to verify the correctness of the generated specifications. We curate a dataset of three Haskell packages where refinement types are used to enforce a variety of correctness properties from data structure invariants to low-level memory safety and use this dataset to evaluate LHC. Previously these packages required expert users several days to weeks to annotate with refinement types. Our evaluation shows that even when using relatively smaller models like the 3 billion parameter StarCoder LLM, by using fine-tuning and carefully chosen contexts, our neurosymbolic agent generates refinement types for up to 94% of the functions across entire libraries automatically in just a few hours, thereby showing that LLMs can drastically shrink the human effort needed to use formal verification.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/ICSE55347.2025.00090)

**Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)
