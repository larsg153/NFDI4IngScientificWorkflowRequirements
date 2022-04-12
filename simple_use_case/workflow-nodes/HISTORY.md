# Release history

## 0.15.0 (Unreleased)

* Added gmsh, latexmk, meshio-convert and tectonic node
* Added directory option to workflow-nodes system cp

## 0.14.0 (2022-03-07)

* Made some requirements optional and added appropriate checks to the
  corresponding tools.

## 0.13.0 (2022-01-17)

* Removed the `click_completion` dependency. Autocompletion is now only
  supported for bash, fish and zsh.

## 0.12.0 (2021-11-24)

* Relaxed required Python version again.
* Update kadi-apy and xmlhelpy dependency.

## 0.11.0 (2021-11-12)

* Added option so that `plot-matplotlib` runs with a tokenlist as input.
* Add docs.

## 0.10.1 (2021-11-05)

* Bumped to kadi-apy v0.18.0.

## 0.10.0 (2021-11-04)

* Adjusted the direction parameters in the record visualization commands for
  the newest Kadi version.
* Removed the explicit version of each command. All commands now inherit the
  `workflow-node` group's version, which corresponds to the current package
  version.
* Run-script now supports non-absolute paths and has improved error handling.

## 0.9.0 (2021-10-25)

* Added a node for octave.
* Moved matlab node into misc.
* Added mpirun and ssh environment nodes.
* Added nodes for compressing files/folders and unpacking archives.

## 0.8.0 (2021-07-16)

* Removed pinning of dependencies to allow for more flexibility once again.

## 0.7.1 (2021-07-12)

* Update package dependencies.

## 0.7.0 (2021-07-07)

* Add a node for scp.
* Add a node for ssh.
* Add a script to create new workflow wrapper tools based on an existing
  program.
* Pinned all Python dependencies to ensure reproducible installations.

## 0.6.0 (2021-02-02)

* Bumped to kadi-apy 0.12.0.

## 0.5.0 (2021-05-10)

* Add matlab wrapper node.
* Add wrapper node for xmllint.
* Add handling of exit code to RunScript node.

## 0.4.1 (2021-04-26)

* Add pypi deploy runner.

## 0.4.0 (2021-04-22)

* Add autocompletion.
* Add xml_to_kadi converter.

## 0.3.0 (2021-02-26)

* Add a node for histograms.
* Add simple smtp node.
* Bumped the `kadi-apy` dependency to the correct version.
* Adjust record visualization tools.

## 0.2.1 (2021-02-03)

* Bumped the `kadi-apy` dependency to the correct version.

## 0.2.0 (2021-02-02)

* Added a tool to run a shell script using CMD or Powershell via the WSL.
* Added a tool to merge tables.
* Added a general file converter tool.
* Added tools to visualize records in a Kadi4Mat instance.
* Added a tool for combining files.
* Added a tool to create QR codes.
* Removed the basic Kadi4Mat integration tools, which are replaced by the CLI
  provided by the `kadi-apy` itself.
* Refactored all existing tools to use a single parent command
  `workflow-nodes`.
* Various other fixes and refactorings.

## 0.1.0 (2020-10-16)

* The first few tools for various common use-cases are provided, including
  tools for converting, plotting and analysing data, for generating reports and
  for connecting to a Kadi4Mat instance.
