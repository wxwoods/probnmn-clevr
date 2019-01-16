from allennlp.data import Vocabulary

from tbd.models.seq2seq_base import Seq2SeqBase


class QuestionReconstructor(Seq2SeqBase):
    """
    Convenience wrapper over ``tbd.models.seq2seq_base.Seq2SeqBase``. This Seq2Seq model
    accepts tokenized and padded program sequences and converts them to question sequences.

    # TODO (kd): can make a fancy encoder here and pass it to the super class.
    """

    def __init__(self,
                 vocabulary: Vocabulary,
                 embedding_size: int = 128,
                 hidden_size: int = 64,
                 dropout: float = 0.0,
                 max_decoding_steps: int = 45):  # 45 is max_question_length in CLEVR v1.0 train
        super().__init__(
            vocabulary,
            source_namespace="programs",
            target_namespace="questions",
            embedding_size=embedding_size,
            hidden_size=hidden_size,
            dropout=dropout,
            max_decoding_steps=max_decoding_steps
        )

