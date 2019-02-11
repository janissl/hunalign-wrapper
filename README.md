# hunalign-wrapper
A set of scripts to build parallel corpora using hunalign
<hr>

## Usage
##### File system structure:
<pre><code>
${corpus_title}
|-- source
    |-- snt
            ${title}_${lang}.snt
|-- work
    |-- ${source_lang}-${target_lang}
            ${title}_${lang}.snt.aligned
|-- aligned_idx
    |-- ${source_lang}-${target_lang}
            ${title}.${lang}.idx
|-- result
        ${corpus_title}.${source_lang}-${target_lang}.${source_lang}
        ${corpus_title}.${source_lang}-${target_lang}.${target_lang}
        ${corpus_title}.unique.${source_lang}-${target_lang}.${source_lang}
        ${corpus_title}.unique.${source_lang}-${target_lang}.${target_lang}
</code></pre>

* Additional Python dependency: PyYAML. Install it using the `python -m pip install PyYAML` command if necessary.
* The _hunalign_ executable must be present on your machine (see _References_ below).
* Before running the shell script, put your source files in _${corpus\_title}/source/snt_ directory.
* The content of source files must be segmented in sentences (one sentence per line).
* Filenames of input files must have the following pattern: _${title}\_${lang}.snt_ (e.g. _document\_en.snt_).
* Parallel files must have identical titles (e.g. _article\_001\_en.snt_, _article\_001\_fr.snt_).
* _hunalign_batch.txt_ will be created automatically during alignment process. Only specify the desired path (the parent directory must exist).
* _null.dic_ is an empty file. It must exist before running the shell script.
* There are two source data directories - _'original_source_data_directory'_ and _'source_data_directory'_ - specified in the YAML file.
The 'original_source_data_directory' is used for files containing sentences in natural language (i.e. unmodified sentences).
The _'source_data_directory'_ is used for additionaly preprocessed files originated from the 'original_source_data_directory' (e.g. stemmed files, additionally tokenized files etc.).
In both directories, files must be stored in the _'snt'_ subfolder.
The sentence alignment itself is done using the content from the _'source_data_directory'_.
On the contrary, the building of parallel corpora is done using the content from _'original_source_data_directory'_.
If no additional preprocessing has been made on source files, both paths must be equal.
* The _'work'_, _'aligned_idx'_ and _'result'_ directories are created automatically.
* Aligned corpora are placed in the _'result'_ directory.<br>

__Note:__ It is not necessary to keep all subdirectories (_work_, _aligned_idx_, _result_) under the same root but it is much easier to track the alignment process in this way.

##### An example of a configuration file (YAML):
(for running on Windows OS; replace values in square brackets with actual paths; see also _io\_args.yml.sample_)
<pre><code>
source_language: en
target_language: fr

corpus_title: aligned_corpora
batch_filepath: [...]\aligned_corpora\hunalign_batch.txt

hunalign_exe: [/path/to/hunalign/binary]
hunspell_null_dic: [/path/to/hunspell]\null.dic

original_source_data_directory: [...]\aligned_corpora\source
source_data_directory: [...]\aligned_corpora\source
work_directory: [...]\aligned_corpora\work
alignment_index_directory: [...]\aligned_corpora\aligned_idx
output_data_directory: [...]\aligned_corpora\result

alignment_threshold: 0
</code></pre>


### Running the shell script
* Enter the actual values for parameters in the configuration YAML file (see above).
* Specify the name of the configuration (YAML) file in the _run\_hunalign.bat_ file (the value of _config_file_). The YAML file must reside in the script directory.
* Execute the following command (on Windows):<br>
`.\run_hunalign.bat`
<br><br>

__Note:__ The current set of scripts may be also run under UNIX/Linux OS.
For this purpose, a Bash file similar to _run\_hunalign.bat_ must be executed.
<hr>

##### References:
* [hunalign](https://github.com/danielvarga/hunalign)
* [hunalign (a version adapted for MinGW-w64)](https://github.com/janissl/hunalign)
