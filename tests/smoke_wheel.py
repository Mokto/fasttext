from pathlib import Path
from tempfile import TemporaryDirectory

import fasttext
import numpy as np

with TemporaryDirectory() as directory:
    corpus = Path(directory) / "corpus.txt"
    corpus.write_text(
        ("__label__en hello world\n__label__da hej blå verden\n") * 20,
        encoding="utf-8",
    )
    model = fasttext.train_supervised(
        str(corpus), dim=8, minCount=1, bucket=100, epoch=10, thread=1, verbose=0
    )
    labels, probabilities = model.predict("hello world", k=2)
    assert set(labels) == {"__label__en", "__label__da"}
    assert probabilities.shape == (2,)
    assert np.isfinite(probabilities).all()
    assert np.isclose(probabilities.sum(), 1, atol=1e-4)
    batch_labels, batch_probabilities = model.predict(["hello world", "hej verden"], k=2)
    assert len(batch_labels) == 2
    assert np.asarray(batch_probabilities).shape == (2, 2)
    assert np.isfinite(batch_probabilities).all()

    saved = Path(directory) / "model.bin"
    model.save_model(str(saved))
    loaded = fasttext.load_model(str(saved))
    loaded_labels, loaded_probabilities = loaded.predict("hello world", k=2)
    assert loaded_labels == labels
    np.testing.assert_allclose(loaded_probabilities, probabilities)

    vectors = fasttext.train_unsupervised(
        str(corpus), dim=8, minCount=1, bucket=100, epoch=1, thread=1, verbose=0
    )
    assert vectors.get_word_vector("hello").shape == (8,)
    assert np.isfinite(vectors.get_word_vector("hello")).all()

print("Installed-wheel training, prediction, vectors and model round-trip passed")
