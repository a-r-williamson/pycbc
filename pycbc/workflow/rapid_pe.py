# Copyright (C) 2017 Andrew R. Williamson
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

#
# =============================================================================
#
#                                   Preamble
#
# =============================================================================
#
"""
This module is used to prepare rapid parameter estimation of candidate events.
For details of this module and its capabilities see here:
https://ldas-jobs.ligo.caltech.edu/~cbc/docs/pycbc/NOTYETCREATED.html
"""

from __future__ import division

import os
import os.path
import logging
import Pegasus.DAX3 as dax
from glue import segments
from pycbc.workflow.core import File, FileList, make_analysis_dir
from pycbc.workflow.jobsetup import select_generic_executable

def setup_rapipe_followup_workflow(workflow, output_dir, tags=None, **kwargs):
    """
    This function aims to be the gateway for running rapid parameter estimation
    in workflows.

    Parameters
    -----------
    workflow : pycbc.workflow.core.Workflow
        The Workflow instance that rapidpe jobs will be added to.
    output_dir : path
        The directory in which output files will be stored.
    tags : list of strings (optional, default = [])
        A list of the tagging strings that will be used for all jobs created
        by this call to the workflow. An example might be ['POSTPROC1'] or
        ['DENTYSNEWPOSTPROC']. This will be used in output names.

    Returns
    --------
    rapidpe_files : pycbc.workflow.core.FileList
        A list of the output from this stage.

    """
    if tags is None:
        tags = []
    logging.info("Entering rapidpe module.")
    make_analysis_dir(output_dir)

    # Parse for options in .ini file
    rapidpe_method = workflow.cp.get_opt_tags("workflow-rapidpe",
                                              "rapidpe-method", tags)

    # Scope here for adding different options/methods here.
    if rapidpe_method == "COH_PTF_WORKFLOW":
        rapidpe_files = setup_rapidpe_coh_PTF_workflow(workflow, output_dir,
                tags=tags, **kwargs)
    else:
        errMsg = "Method not recognized. Must be "
        errMsg += "COH_PTF_WORKFLOW."
        raise ValueError(errMsg)

    logging.info("Leaving rapidpe module.")

    return rapidpe_files


def setup_rapidpe_coh_PTF_workflow(workflow, output_dir, tags=None):
    """
    This module sets up the rapidpe stage as a sub-workflow to a coh_PTF style
    main workflow.
    
    workflow : pycbc.workflow.core.Workflow
        The Workflow instance that the jobs will be added to.
    output_dir : path
        The directory in which output files will be stored.
    tags : list of strings (optional, default = [])
        A list of the tagging strings that will be used for all jobs created
        by this call to the workflow.
   
    Returns
    --------
    
    """
    if tags is None:
        tags = []
    cp = workflow.cp

    rapidpe_outs = FileList([])
    rapidpe_nodes = []

    # Set up needed exe classes
    rapidpe_class = select_generic_executable(workflow, "rapidpe")

    return rapidpe_outs

