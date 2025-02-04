__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts

bcftools_opts = get_bcftools_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "bcftools view {bcftools_opts} "
    "{extra} "
    "{snakemake.input[0]} "
    "-o {snakemake.output} "
    "{log}"
)
