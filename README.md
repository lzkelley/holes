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
                "name": "<a href='http://adsabs.harvard.edu/abs/2006ApJ...646...49R'>2006ApJ...646...49R</a>",
                "alias": "1"
            },
            {
                "name": "<a href='http://adsabs.harvard.edu/abs/2009ApJ...697...37R'>2009ApJ...697...37R</a>",
                "alias": "2"
            }
            {
                "name:" "<a href='http://adsabs.harvard.edu/cgi-bin/bib_query?2009A%26A...496L...9M'>2009A&A...496L...9M</a>",
                "alias": "3"
            }
        ],
        "bhtype": "massive",
        "multiplicity": {
            "number": "2",
            "method": [
                {
                    "type":"resolved",
                    "source":["1", "2"]
                },
                {
                    "type": "spectroscopic",
                    "source": "2",
                }
            ],
            "separation": {
                "value": "7.3",
                "source": "2",
            },
            "mass_total": "1.5e8",
            "galaxies": "none",
            "notes": "Resolved dual-AGN system (with VLBI).  A 'red shoulder' in the H-Alpha line suggests two components with 300 km/s separation.  Given the observed separation, this suggests total mass of 1.5e8 Msol (highly uncertain).  Proper motion cannot be resolved.",
        },
        "galaxy": {
            "classification": ["Sy", "NLRG"],
            "redshift": {
                "value": "0.055046",
                "sigma": ["0.000078", "0.000078"],
                "source": "3",
            },
            "ra": "040549.2",
            "dec": "+380332",
        },
        "jet": "yes",
    }
}
```

Fields:
- `bhtype`: Mass-based type of blackhole
    - {'stellar', 'intermediate', 'massive', 'limit'}, where 'limit' refers to an upper limit on the presence of a BH.
- `multiplicity`: If there is claimed multiplicity to the blackhole / system
    - `mass_total`: fiducial total mass of the binary system
    - `method`: method by which binary was detected/inferred
        - 'resolved': secondary system photometrically resolved (e.g. via VLBI)
        - 'spectroscopic': distinct velocity components interpreted as a dynamic signature.
        - 'variable': inferred based on periodicity/variability signatures
    - `separation`: fiducial separation between binary components, [parsecs]
- `galaxy`: properties of the host galaxy/galaxies.
- `jet`: evidence for a relativistic jet

At the moment, the only mandatory field for a given blackhole is its name.
