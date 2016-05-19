# Open Black Holes Catalog #

This repository is a collection of blackhole data, including metadata, light curves, and spectra. The catalog is displayed in tabular form on [holes.space](https://holes.space). Individual event data can be downloaded by navigating to the individual-bh folder and downloading the '.json' file associated with a given event; however it might be easier to use the search function on the table displayed on [holes.space](https://holes.space) to find the event you're looking for.

## Contributing Data ##

## Format of Data Files ##

The data files are in JSON format. Below is an example datafile for 0402+379:

```json
{
    "0402+379": {
        "name": "0402+379",
        "aliases": [
            "0402+379", "4C+37.11"
        ],
        "sources": [
            {
                "name": "<a href='http://http://adsabs.harvard.edu/abs/2006ApJ...646...49R'>2006ApJ...646...49R</a>",
                "alias": "1"
            },
            {
                "name": "<a href='http://http://adsabs.harvard.edu/abs/2009ApJ...697...37R'>2009ApJ...697...37R</a>",
                "alias": "2"
            }
            {
                "name:" "<a href='http://adsabs.harvard.edu/cgi-bin/bib_query?2009A%26A...496L...9M'>2009A&A...496L...9M</a>",
                "alias": "3"
            }
        ],
        "bhtype": "massive",
        "binary": "yes",
        "binary_method": ["resolved", "spectroscopic"],
        "binary_separation": "7.3",
        "binary_mass": "1.5e8",
        "binary_notes": "Resolved dual-AGN system (with VLBI).  A 'red shoulder' in the H-Alpha line suggests two components with 300 km/s separation.  Given the observed separation, this suggests total mass of 1.5e8 Msol (highly uncertain).  Proper motion cannot be resolved.",
        "galaxy_classification": ["Sy", "NLRG"],
        "jet": "yes",
        "redshift": "0.055046",
        "redshift_sigma": "0.000078",
        "galra": "040549.2",
        "galdec": "+380332",
    }
}
```

Fields:
- `bhtype`: Mass-based type of blackhole
    - {'stellar', 'intermediate', 'massive'}
- `binary`: If there is a claimed binary to the blackhole
    - {'yes', 'no', 'maybe'}, where 'maybe' means a companion is claimed and 'yes' means that it has been confirmed, or is generally agreed upon.
- `binary_mass`: fiducial total mass of the binary system
- `binary_method`: method by which binary was detected/inferred
    - 'resolved': secondary system photometrically resolved (e.g. via VLBI)
    - 'spectroscopic': distinct velocity components interpreted as a dynamic signature.
    - 'variable': inferred based on periodicity/variability signatures
- `binary_separation`: fiducial separation between binary components, [parsecs]
- `jet`: evidence for a relativistic jet

At the moment, the only mandatory field for a given blackhole is its name.
