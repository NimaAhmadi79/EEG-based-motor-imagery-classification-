# Data

This project uses the **BCI Competition IV — dataset 2a**, a motor-imagery EEG
dataset recorded at Graz University of Technology.

- **Task:** 4-class motor imagery — left hand, right hand, both feet, tongue.
- **Subjects:** 9 (A01–A09), each with a training session (`*T`) and an evaluation
  session (`*E`).
- **Channels:** 22 EEG channels (+ 3 EOG), 250 Hz sampling.
- **Event codes used here:** `769 = left hand`, `770 = right hand`, `771 = feet`,
  `772 = tongue` → mapped to classes `0, 1, 2, 3`.
- **Source / terms:** <https://www.bbci.de/competition/iv/> (dataset 2a). The raw
  `.gdf` files are released by the original authors under their own terms and must be
  downloaded from there — they are **not** redistributed in this repository.

## What is committed here

```
data/
├── README.md
└── 2aEvents/
    ├── A01T.xlsx … A09T.xlsx   # per-subject event tables (type, position, duration)
```

The `2aEvents/*.xlsx` files are small event tables (event type, sample position,
duration) extracted from each subject's training `.gdf` file by
[`scripts/getEvents.m`](../scripts/getEvents.m). They are committed because they are
tiny and make the event structure inspectable without the full dataset.

## What is NOT committed

- The raw `.gdf` recordings (the actual EEG). Download them from the BCI Competition IV
  site above.
- Any `datasets/` folder — it is git-ignored.

## How the code expects the data to be laid out

`get_data.py` reads the raw recordings from a `datasets/BCICIV_2a_gdf/` folder located
**one level above** the notebook, i.e.:

```
<parent>/
├── datasets/
│   └── BCICIV_2a_gdf/
│       ├── A01T.gdf  A01E.gdf  …  A09T.gdf  A09E.gdf
└── EEG-based-motor-imagery-classification-/
    ├── main.ipynb
    └── get_data.py
```

If you place the `.gdf` files there, `main.ipynb` will load and preprocess them. The
MATLAB script `scripts/getEvents.m` is an alternative route that exports event tables
to Excel (it uses the Biosig `sload` function); adjust the hard-coded paths at the top
of that script to your machine before running it.
