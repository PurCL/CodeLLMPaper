# Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles

**Authors**: Molinelli, Davide and Martin-Lopez, Alberto and Zackrone, Elliott and Eken, Beyza and Ernst, Michael D. and Pezz\`{e}, Mauro

**Abstract**:

This paper presents Tratto, a neuro-symbolic approach that generates assertions (boolean expressions) that can serve as axiomatic oracles, from source code and documentation. The symbolic module of Tratto takes advantage of the grammar of the programming language, the unit under test, and the context of the unit (its class and available APIs) to restrict the search space of the tokens that can be successfully used to generate valid oracles. The neural module of Tratto uses transformers fine-tuned for both deciding whether to output an oracle or not and selecting the next lexical token to incrementally build the oracle from the set of tokens returned by the symbolic module. Our experiments show that Tratto outperforms the state-of-the-art axiomatic oracle generation approaches, with 73\% accuracy, 72\% precision, and 61\% F1-score, largely higher than the best results of the symbolic and neural approaches considered in our study (61\%, 62\%, and 37\%, respectively). Tratto can generate three times more axiomatic oracles than current symbolic approaches, while generating 10 times less false positives than GPT4 complemented with few-shot learning and Chain-of-Thought prompting.

**Link**: [Read Paper](https://doi.org/10.1145/3728960)

**Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)
