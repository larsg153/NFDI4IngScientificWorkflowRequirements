.. _userstories:

User Stories
============
        "A user story is an informal, general explanation of a software feature written from the perspective of the end user.
        Its purpose is to articulate how a software feature will provide value to the customer." 
        
        "As a [persona], I [want to], [so that]."
        (Source: `Atlassian <https://www.atlassian.com/agile/project-management/user-stories>`_)

Based on the concept of user stories as a component of agile software development, we aim to deduce :ref:`requirements` from challenges posed in the respective user stories below.

.. _user_story_1:

Reproducible paper
------------------
        *As a researcher, I want to share my paper, such that others are able to reproduce the results.*

In this user story, the main objective is to guarantee reproducibility of the results described in a scientific publication.
To do so, other scientists need to be able to comprehend and rerun each process involved in the research workflow (numerical analysis, postprocessing, etc.).

There are several challenges in meeting the goal above.
First of all, the code has to be published.
This can happen in the form of a tarball (e.g. via `Zenodo <https://zenodo.org>`_), or by employing version control on the code base and making the repository publicly accessible (e.g. via `GitHub <https://github.com>`_).
This makes it possible to refer to a particular version of the code used at the time of publication.
As research software is also understood as research data, appropriate metadata regarding the code and dependencies on third-party libraries should be provided.
The metadata should contain all information necessary for peers to reinstantiate the compute environment to make the workflow usable.
However, since software becomes out of date rather quickly this is a minimum requirement and it is preferred to build containers that package up all required pieces of software in a way that is portable, reproducible and ensures machine-independent execution.
Finally, the fully automated implementation of the entire workflow is required to avoid any manual steps.
Ideally, the whole paper can be reproduced by running a single command and the progress of the execution is monitored by the workflow tool.


.. _user_story_2:

Research group collaboration
----------------------------
        *As part of a research group, I want to be able to interconnect and reuse components of several different workflows so that everyone may benefit from their colleagues' work.*

Similar to the first user story the output of the workflow could be a scientific paper. 
However, with this example interdisciplinary workflows are addressed and the reusability of single components/modules is essential. 
Each process in the workflow may require a different expertise and hence modularity and a common framework are necessary features for efficient collaboration.
Moreover, joint software development and the development of the scientific workflow itself play an important role.

Herein, the following challenges might occur.
First, the workflow may consist of heterogeneous models, such as HPC computational model, calibration model or preprocessing of experimental data potentially even running on different machines. 
These models then need to be embedded into a common framework. 
Without a common framework/interface the exchange of data between processes is not possible (except for file based workflows).
Second, during joint development of the workflow, it needs to be executable indepent of the local machine.
Therefore, the workflow tool must provide means to control (automatically install) the compute environment for specific processes of the workflow.
This greatly enhances the reusability of a process and/or modules (chain of processes) of the workflow and guarantees the machine-independent execution.
Another challenge are high computational costs.
Here, the seamless integration of HPC systems is of high value.
Moreover, for complex workflows containing computationally expensive processes caching of results becomes relevant.
Upon changes in the workflow only parts of the workflow which are not up-to-date are rerun.
This saves computation time and may lead to a significant speed up in the time needed for development of the workflow.


.. _user_story_3:

High-throughput simulations
---------------------------
        *As a materials scientist, I want to be able to automate and manage complex workflows so I can keep track of all associated data.*

In cases where screening or parameter sweeps are required, involving thousands of simulations, running these one by one is not feasible.
Moreover, besides the automation of running the calculations their inputs and outputs need to be stored.
Not only the data and calculations should be stored to achieve reproducibility, but also the causal relationships between them, i.e. the full provenance.

Given the large amount of data (inputs/outputs) manually keeping track of the full provenance becomes infeasible.
Therefore, the workflow tool must automatically track and record inputs, outputs and metadata of all processes in a database.
Furthermore, fast queries of the database and automatic generation of the provenance graph are required features of the workflow tool.
Due to the large computational effort the seamless integration of HPC systems is as well vital for this use case.
